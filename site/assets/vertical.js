// OpenCCman vertical card tool (#17). The card is drawn on a canvas one character
// per grid cell, right to left, so the preview is exactly what the PNG export
// contains. Everything runs in the browser; the text never leaves the device.
(() => {
  const root = document.querySelector("[data-vertical]");
  const form = document.querySelector("[data-form]");
  if (!root || !form) return;

  const canvas = root.querySelector("[data-canvas]");
  const frame = root.querySelector("[data-frame]");
  const status = root.querySelector("[data-status]");
  const warn = root.querySelector("[data-warn]");
  const exportButton = root.querySelector("[data-export]");
  const result = root.querySelector("[data-result]");
  const out = root.querySelector("[data-out]");
  const shareButton = root.querySelector("[data-share]");
  const download = root.querySelector("[data-download]");
  const perOutput = form.querySelector("[data-per]");
  const previewLabel = canvas.getAttribute("aria-label");
  const reduced = () => window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Card geometry and paper ------------------------------------------------ */

  const SIZES = { "34": [1080, 1440], "11": [1080, 1080], "916": [1080, 1920] };
  const THEMES = {
    paper: { bg: "#f3ecdf", ink: "#2a231f", sub: "rgba(42, 35, 31, 0.78)", noise: "#3a2f25" },
    grid: { bg: "#f7f9f6", ink: "#1b2433", sub: "rgba(27, 36, 51, 0.75)", rule: "#b7dac6", frame: "#2f8b63" },
    ink: { bg: "#121714", ink: "#e6ede8", sub: "rgba(230, 237, 232, 0.72)", noise: "#e6ede8" },
  };
  const SEAL = { fill: "#cf3a2d", ink: "#fff6f2" };

  // Faces are unicode-range slices from scripts/vertical_fonts.py; the browser
  // fetches only the slices that cover the characters on the card.
  const FACES = {
    "serif-sc": { sheets: ["serif-sc"], names: ["OpenCCman Card Serif SC"],
      stack: '"OpenCCman Card Serif SC", "Songti SC", "Noto Serif CJK SC", serif' },
    "serif-tc": { sheets: ["serif-tc", "serif-sc"], names: ["OpenCCman Card Serif TC", "OpenCCman Card Serif SC"],
      stack: '"OpenCCman Card Serif TC", "OpenCCman Card Serif SC", "Songti TC", "Noto Serif CJK TC", serif' },
    hand: { sheets: ["hand"], names: ["OpenCCman Card Hand"],
      stack: '"OpenCCman Card Hand", "Kaiti SC", "STKaiti", "BiauKai", serif' },
    system: { sheets: [], names: [], stack: null },
  };

  // Vertical punctuation: CORNER sits top right (mainland) or centred (Taiwan),
  // CENTER stays upright in the middle, ROTATE turns 90° with the column.
  const CORNER = new Set([..."，。、．,."]);
  const CENTER = new Set([..."！？!?"]);
  const ROTATE = new Set([..."：；:;「」『』（）《》〈〉【】〔〕［］｛｝()[]{}<>—―…‥～~-ー_｜|→←"]);
  const NO_START = new Set([..."，。、．：；！？」』）》〉】〕］｝…‥—―～ー,.:;!?)]}>"]);
  const NO_END = new Set([..."「『（《〈【〔［｛([{<"]);

  /* State ------------------------------------------------------------------ */

  const STORE = "openccman-vertical-card";
  const fields = form.elements;

  function readState() {
    const pick = (name) => form.querySelector(`input[name="${name}"]:checked`)?.value;
    return {
      text: fields.text.value, sig: fields.sig.value, seal: fields.seal.value,
      font: pick("font"), punct: pick("punct"), paper: pick("paper"), size: pick("size"), scale: pick("scale"),
      quotes: fields.quotes.checked, auto: fields.auto.checked, per: Number(fields.per.value),
    };
  }

  function restore() {
    let saved;
    try { saved = JSON.parse(localStorage.getItem(STORE)); } catch (error) { return; }
    if (!saved || typeof saved !== "object") return;
    for (const key of ["text", "sig", "seal"]) if (typeof saved[key] === "string") fields[key].value = saved[key];
    for (const key of ["font", "punct", "paper", "size", "scale"]) {
      const input = form.querySelector(`input[name="${key}"][value="${CSS.escape(String(saved[key]))}"]`);
      if (input) input.checked = true;
    }
    for (const key of ["quotes", "auto"]) if (typeof saved[key] === "boolean") fields[key].checked = saved[key];
    if (Number.isFinite(saved.per)) fields.per.value = saved.per;
  }

  function persist(state) {
    try { localStorage.setItem(STORE, JSON.stringify(state)); } catch (error) { /* private mode */ }
  }

  /* Fonts ------------------------------------------------------------------ */

  const sheets = {};
  function linkSheet(key) {
    if (!sheets[key]) {
      sheets[key] = new Promise((resolve, reject) => {
        const link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = `/assets/vertical/${key}.css`;
        link.addEventListener("load", resolve, { once: true });
        link.addEventListener("error", () => { delete sheets[key]; link.remove(); reject(new Error(key)); }, { once: true });
        document.head.append(link);
      });
    }
    return sheets[key];
  }

  async function loadFonts(state, text) {
    const face = FACES[state.font] || FACES["serif-sc"];
    await Promise.all(face.sheets.map(linkSheet));
    await Promise.all(face.names.map((name) => document.fonts.load(`400 64px "${name}"`, text)));
  }

  function stack(state) {
    const face = FACES[state.font] || FACES["serif-sc"];
    if (face.stack) return face.stack;
    return state.punct === "tw"
      ? '"PingFang TC", "PingFang SC", "Microsoft JhengHei", sans-serif'
      : '"PingFang SC", "PingFang TC", "Microsoft YaHei", sans-serif';
  }

  /* Text ------------------------------------------------------------------- */

  function normalize(text, quotes) {
    let s = text.replace(/\r\n?/g, "\n");
    if (quotes) {
      s = s.replace(/“/g, "「").replace(/”/g, "」").replace(/‘/g, "『").replace(/’/g, "』");
      let open = true;
      s = s.replace(/"/g, () => { const c = open ? "「" : "」"; open = !open; return c; });
    }
    return s;
  }

  function tokenize(s) {
    const units = [];
    const re = /\n|[A-Za-z0-9](?:[A-Za-z0-9.:%\/+\-_ ]*[A-Za-z0-9%])?|[\s\S]/gu;
    for (const [t] of s.matchAll(re)) {
      if (t === "\n") { units.push({ k: "nl" }); continue; }
      if (/^[A-Za-z0-9]/.test(t)) {
        if (/^\d{1,2}$/.test(t)) units.push({ k: "tcy", t });
        else if (/^\d+$/.test(t)) [...t].forEach((d) => units.push({ k: "digit", t: d }));
        else units.push({ k: "latin", t });
        continue;
      }
      if (t === " " || t === "\t") continue;
      if (t === "　") units.push({ k: "space", t });
      else if (CORNER.has(t)) units.push({ k: "corner", t });
      else if (CENTER.has(t)) units.push({ k: "center", t });
      else if (ROTATE.has(t)) units.push({ k: "rot", t });
      else units.push({ k: "cjk", t });
    }
    return units;
  }

  /* Layout: a grid with line-breaking rules -------------------------------- */

  function geom(W, H, N) {
    const mx = W * 0.1, mt = H * 0.09, mb = H * 0.11;
    const s = (H - mt - mb) / N;
    const pitch = s * 1.3;
    const C = Math.max(0, Math.floor((W - 2 * mx - s) / pitch) + 1);
    return { mx, mt, mb, s, pitch, C };
  }

  function columns(units, N, latinCells) {
    const cols = [];
    let col = { items: [], hang: null }, row = 0;
    const next = () => { cols.push(col); col = { items: [], hang: null }; row = 0; };
    for (const u of units) {
      if (u.k === "nl") { next(); continue; }
      const span = u.k === "latin" ? Math.min(N, latinCells(u.t)) : 1;
      if (row + span > N) {
        // A full column hangs its closing punctuation below the last cell.
        if (span === 1 && row === N && NO_START.has(u.t) && !col.hang) { col.hang = u; continue; }
        // An opening bracket moves with what follows it.
        const last = col.items[col.items.length - 1];
        const carry = col.items.length > 1 && last.span === 1 && NO_END.has(last.u.t) ? col.items.pop() : null;
        next();
        if (carry) { col.items.push({ u: carry.u, row: 0, span: 1 }); row = 1; }
      }
      col.items.push({ u, row, span });
      row += span;
      if (row === N && span === 1 && NO_END.has(u.t) && col.items.length > 1) {
        col.items.pop(); next(); col.items.push({ u, row: 0, span: 1 }); row = 1;
      }
    }
    if (col.items.length || col.hang) cols.push(col);
    return cols;
  }

  const measure = document.createElement("canvas").getContext("2d");
  function layout(state) {
    const [W, H] = SIZES[state.size] || SIZES["34"];
    const units = tokenize(normalize(state.text, state.quotes));
    const side = Boolean(state.sig.trim() || state.seal.trim());
    const family = stack(state);
    const attempt = (N) => {
      const g = geom(W, H, N);
      measure.font = `400 ${g.s * 0.84 * 0.8}px ${family}`;
      const cols = columns(units, N, (t) => Math.ceil((measure.measureText(t).width + g.s * 0.2) / g.s));
      const need = cols.length + (side ? 1 : 0);
      return { ...g, N, cols, need, fits: need <= g.C && g.s <= W - 2 * g.mx };
    };
    let L;
    if (state.auto) {
      for (let N = 5; N <= 28; N++) { L = attempt(N); if (L.fits) break; }
    } else {
      L = attempt(Math.min(28, Math.max(5, state.per)));
    }
    const blockW = Math.max(0, L.need - 1) * L.pitch + L.s;
    L.xRight = state.paper === "grid" ? W - L.mx : (W + blockW) / 2;
    Object.assign(L, { W, H, top: L.mt, side });
    return L;
  }

  const colX = (L, i) => L.xRight - i * L.pitch - L.s / 2;

  /* Drawing ---------------------------------------------------------------- */

  // Punctuation is placed by its ink, measured off-screen: WebKit's measureText
  // boxes disagree with Chrome's under centred alignment, which left commas in the
  // middle of the cell on iPhone.
  const inkCache = new Map();
  const REF = 200;
  function inkCenter(ch, family, size) {
    const key = `${family}|${ch}`;
    let ink = inkCache.get(key);
    if (!ink) {
      const c = document.createElement("canvas");
      c.width = c.height = REF * 2;
      const x = c.getContext("2d", { willReadFrequently: true });
      x.font = `400 ${REF}px ${family}`;
      x.textBaseline = "alphabetic";
      const ox = REF * 0.5, oy = REF * 1.3;
      x.fillText(ch, ox, oy);
      const d = x.getImageData(0, 0, c.width, c.height).data;
      let minX = c.width, minY = c.height, maxX = -1, maxY = -1;
      for (let y = 0; y < c.height; y++) {
        for (let i = 0; i < c.width; i++) {
          if (d[(y * c.width + i) * 4 + 3] > 40) {
            if (i < minX) minX = i;
            if (i > maxX) maxX = i;
            if (y < minY) minY = y;
            if (y > maxY) maxY = y;
          }
        }
      }
      ink = maxX < 0 ? { x: REF * 0.5, y: -REF * 0.35 } : { x: (minX + maxX) / 2 - ox, y: (minY + maxY) / 2 - oy };
      // Cache only once the face is ready, so a fallback glyph is never remembered.
      if (document.fonts.check(`400 ${REF}px ${family}`, ch)) inkCache.set(key, ink);
    }
    const k = size / REF;
    return { x: ink.x * k, y: ink.y * k };
  }

  function drawUnit(ctx, u, cx, top, s, span, family, punct) {
    const f = s * 0.84, cy = top + s / 2;
    ctx.font = `400 ${f}px ${family}`;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    switch (u.k) {
      case "space": break;
      case "cjk": ctx.fillText(u.t, cx, cy); break;
      case "digit":
        ctx.font = `400 ${f * 0.86}px ${family}`;
        ctx.fillText(u.t, cx, cy);
        break;
      case "tcy": {
        ctx.save();
        ctx.font = `400 ${f * 0.86}px ${family}`;
        const w = ctx.measureText(u.t).width;
        ctx.translate(cx, cy);
        ctx.scale(Math.min(1, (s * 0.9) / w), 1);
        ctx.fillText(u.t, 0, 0);
        ctx.restore();
        break;
      }
      case "rot":
        if (u.t === "—" || u.t === "―") {
          // Rotated dash glyphs leave a gap; a full-cell rule joins two dashes into one line.
          ctx.save();
          ctx.strokeStyle = ctx.fillStyle;
          ctx.lineWidth = Math.max(1.5, s * 0.045);
          ctx.beginPath();
          ctx.moveTo(cx, top);
          ctx.lineTo(cx, top + s);
          ctx.stroke();
          ctx.restore();
          break;
        }
        ctx.save();
        ctx.translate(cx, cy);
        ctx.rotate(Math.PI / 2);
        ctx.fillText(u.t, 0, 0);
        ctx.restore();
        break;
      case "latin": {
        ctx.save();
        ctx.font = `400 ${f * 0.8}px ${family}`;
        const w = ctx.measureText(u.t).width;
        ctx.translate(cx, top + (span * s - w) / 2);
        ctx.rotate(Math.PI / 2);
        ctx.textAlign = "left";
        ctx.fillText(u.t, 0, 0);
        ctx.restore();
        break;
      }
      case "corner":
      case "center": {
        const ink = inkCenter(u.t, family, f);
        const corner = u.k === "corner" && punct === "cn";
        ctx.textAlign = "left";
        ctx.textBaseline = "alphabetic";
        ctx.fillText(u.t, (corner ? cx + s * 0.24 : cx) - ink.x, (corner ? top + s * 0.26 : cy) - ink.y);
        break;
      }
    }
  }

  function mulberry32(seed) {
    let a = seed;
    return () => {
      a |= 0; a = (a + 0x6d2b79f5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function roundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
  }

  function sealBox(state, L) {
    const n = [...state.seal.trim()].length;
    if (!n) return null;
    const z = L.s * 0.92;
    return { n, z, w: n === 2 ? z * 0.62 : z, h: z };
  }

  function drawSeal(ctx, state, L, cx, bottom, family, bg) {
    const b = sealBox(state, L);
    if (!b) return;
    const chars = [...state.seal.trim()].slice(0, 4);
    const x = cx - b.w / 2, y = bottom - b.h;
    ctx.save();
    ctx.fillStyle = SEAL.fill;
    roundRect(ctx, x, y, b.w, b.h, b.z * 0.06);
    ctx.fill();
    ctx.strokeStyle = SEAL.ink;
    ctx.globalAlpha = 0.9;
    ctx.lineWidth = b.z * 0.03;
    const p = b.z * 0.07;
    roundRect(ctx, x + p, y + p, b.w - 2 * p, b.h - 2 * p, b.z * 0.03);
    ctx.stroke();
    ctx.globalAlpha = 1;
    ctx.fillStyle = SEAL.ink;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    if (b.n === 1) {
      ctx.font = `400 ${b.z * 0.6}px ${family}`;
      ctx.fillText(chars[0], cx, y + b.h / 2);
    } else if (b.n === 2) {
      ctx.font = `400 ${b.z * 0.34}px ${family}`;
      ctx.fillText(chars[0], cx, y + b.h * 0.31);
      ctx.fillText(chars[1], cx, y + b.h * 0.69);
    } else {
      // Seals read right column first, top to bottom.
      ctx.font = `400 ${b.z * 0.34}px ${family}`;
      const rx = cx + b.w * 0.2, lx = cx - b.w * 0.2;
      ctx.fillText(chars[0], rx, y + b.h * 0.31);
      ctx.fillText(chars[1], rx, y + b.h * 0.69);
      if (chars.length === 4) {
        ctx.fillText(chars[2], lx, y + b.h * 0.31);
        ctx.fillText(chars[3], lx, y + b.h * 0.69);
      } else {
        ctx.save();
        ctx.translate(lx, y + b.h / 2);
        ctx.scale(1, 1.8);
        ctx.fillText(chars[2], 0, 0);
        ctx.restore();
      }
    }
    // Seal paste never prints evenly: a few pale specks.
    const rnd = mulberry32(7);
    ctx.fillStyle = bg;
    ctx.globalAlpha = 0.35;
    for (let i = 0; i < 26; i++) {
      ctx.beginPath();
      ctx.arc(x + rnd() * b.w, y + rnd() * b.h, b.z * (0.006 + rnd() * 0.016), 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();
  }

  function draw(target, state, L, scale) {
    const th = THEMES[state.paper] || THEMES.paper;
    const family = stack(state);
    target.width = Math.round(L.W * scale);
    target.height = Math.round(L.H * scale);
    const ctx = target.getContext("2d");
    ctx.setTransform(scale, 0, 0, scale, 0, 0);
    ctx.fillStyle = th.bg;
    ctx.fillRect(0, 0, L.W, L.H);
    if (th.noise) {
      const rnd = mulberry32(42);
      ctx.fillStyle = th.noise;
      for (let i = 0; i < 5000; i++) {
        ctx.globalAlpha = 0.02 + rnd() * 0.05;
        ctx.fillRect(rnd() * L.W, rnd() * L.H, 1 + rnd() * 1.6, 1 + rnd() * 1.6);
      }
      ctx.globalAlpha = 1;
    }
    if (th.rule) {
      ctx.strokeStyle = th.rule;
      ctx.lineWidth = 1.6;
      for (let j = 0; j < L.C; j++) {
        for (let r = 0; r < L.N; r++) ctx.strokeRect(L.W - L.mx - j * L.pitch - L.s, L.top + r * L.s, L.s, L.s);
      }
      const left = L.W - L.mx - (L.C - 1) * L.pitch - L.s;
      ctx.strokeStyle = th.frame;
      ctx.lineWidth = 3;
      ctx.strokeRect(left - 10, L.top - 10, L.W - L.mx - left + 20, L.N * L.s + 20);
    }
    ctx.fillStyle = th.ink;
    L.cols.forEach((col, i) => {
      const cx = colX(L, i);
      col.items.forEach((it) => drawUnit(ctx, it.u, cx, L.top + it.row * L.s, L.s, it.span, family, state.punct));
      if (col.hang) drawUnit(ctx, col.hang, cx, L.top + L.N * L.s, L.s, 1, family, state.punct);
    });
    if (L.side) {
      const cx = colX(L, L.cols.length);
      const box = sealBox(state, L);
      const bottom = L.top + L.N * L.s;
      const sigBottom = box ? bottom - box.h - L.s * 0.3 : bottom;
      const s2 = L.s * 0.62;
      const units = tokenize(normalize(state.sig.trim(), state.quotes)).filter((u) => u.k !== "nl");
      ctx.fillStyle = th.sub;
      units.forEach((u, k) => drawUnit(ctx, u.k === "latin" ? { k: "rot", t: u.t } : u, cx,
        sigBottom - (units.length - k) * s2, s2, 1, family, state.punct));
      drawSeal(ctx, state, L, cx, bottom, family, th.bg);
    }
  }

  /* Preview ---------------------------------------------------------------- */

  let current = null;
  let seq = 0;
  let timer = 0;

  async function render() {
    const id = ++seq;
    const state = readState();
    persist(state);
    fields.per.disabled = state.auto;
    const text = normalize(state.text, state.quotes) + state.sig + state.seal;
    const slow = setTimeout(() => { status.hidden = false; }, 150);
    try {
      await loadFonts(state, text);
    } catch (error) {
      // A missing slice falls back to the system serif; the card still renders.
    }
    clearTimeout(slow);
    if (id !== seq) return;
    status.hidden = true;
    const L = layout(state);
    current = { state, L };
    frame.style.aspectRatio = `${L.W} / ${L.H}`;
    const scale = Math.min(1, Math.max(0.3, (frame.clientWidth * (window.devicePixelRatio || 1)) / L.W));
    draw(canvas, state, L, scale);
    const sep = document.documentElement.lang === "en" ? ": " : "：";
    canvas.setAttribute("aria-label", `${previewLabel}${sep}${state.text.trim().slice(0, 120)}`);
    perOutput.textContent = String(L.N);
    if (state.auto) fields.per.value = L.N;
    warn.textContent = L.fits ? "" : root.dataset.overflow.replace("{need}", L.need).replace("{cols}", L.C);
    exportButton.disabled = false;
  }

  function schedule(delay) {
    clearTimeout(timer);
    timer = setTimeout(render, delay);
  }

  /* Export ----------------------------------------------------------------- */

  let lastUrl = null;
  let lastFile = null;

  function toBlob(target) {
    return new Promise((resolve, reject) => {
      target.toBlob((blob) => (blob ? resolve(blob) : reject(new Error("toBlob"))), "image/png");
    });
  }

  async function exportCard() {
    if (!current) return;
    exportButton.disabled = true;
    try {
      const { state, L } = current;
      const target = document.createElement("canvas");
      draw(target, state, L, Number(state.scale) || 1);
      const blob = await toBlob(target);
      target.width = target.height = 0;
      if (lastUrl) URL.revokeObjectURL(lastUrl);
      lastUrl = URL.createObjectURL(blob);
      lastFile = new File([blob], "vertical-card.png", { type: "image/png" });
      out.src = lastUrl;
      download.href = lastUrl;
      shareButton.hidden = !(navigator.canShare && navigator.canShare({ files: [lastFile] }));
      result.hidden = false;
      result.scrollIntoView({ behavior: reduced() ? "auto" : "smooth", block: "nearest" });
    } catch (error) {
      warn.textContent = root.dataset.failed.replace("{error}", error.message || error.name);
    } finally {
      exportButton.disabled = false;
    }
  }

  async function shareCard() {
    if (!lastFile) return;
    try {
      await navigator.share({ files: [lastFile] });
    } catch (error) {
      if (error.name !== "AbortError") warn.textContent = root.dataset.failed.replace("{error}", error.message || error.name);
    }
  }

  /* Wiring ----------------------------------------------------------------- */

  restore();
  form.addEventListener("submit", (event) => event.preventDefault());
  form.addEventListener("input", (event) => schedule(event.target.matches("textarea, input[type=text]") ? 220 : 0));
  form.addEventListener("change", () => schedule(0));
  form.querySelectorAll(".vc-sample").forEach((button) => button.addEventListener("click", () => {
    fields.text.value = button.dataset.text;
    fields.sig.value = button.dataset.sig;
    fields.seal.value = button.dataset.seal;
    schedule(0);
  }));
  exportButton.addEventListener("click", exportCard);
  shareButton.addEventListener("click", shareCard);
  download.addEventListener("click", (event) => { if (!lastUrl) event.preventDefault(); });
  let width = frame.clientWidth;
  window.addEventListener("resize", () => {
    if (frame.clientWidth !== width) { width = frame.clientWidth; schedule(120); }
  });
  render();
})();
