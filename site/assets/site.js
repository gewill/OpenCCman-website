// OpenCCman site behaviour. Every feature is an enhancement: the server-rendered
// page is complete without this file.
(() => {
  const doc = document.documentElement;
  const lang = doc.lang || "en";
  const reduced = () => window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const svgNS = "http://www.w3.org/2000/svg";

  const el = (tag, cls, text) => {
    const node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text != null) node.textContent = text;
    return node;
  };

  const svg = (cls, viewBox, d, extra = {}) => {
    const node = document.createElementNS(svgNS, "svg");
    node.setAttribute("class", cls);
    node.setAttribute("viewBox", viewBox);
    node.setAttribute("aria-hidden", "true");
    node.setAttribute("focusable", "false");
    Object.entries(extra).forEach(([k, v]) => node.setAttribute(k, v));
    const path = document.createElementNS(svgNS, "path");
    path.setAttribute("d", d);
    path.setAttribute("pathLength", "100");
    node.append(path);
    return node;
  };

  /* Proof desk ------------------------------------------------------------ */

  const data = window.OCCMAN;

  function ring(n, variant) {
    const set = data.rings[String(Math.min(n, data.maxRing))];
    const d = set[variant % set.length];
    return svg("ring", `0 0 ${n * 100 + 29} 129`, d, { preserveAspectRatio: "none" });
  }

  function render(fig, state) {
    const t = data.i18n[lang] || data.i18n.en;
    const spec = data.specimens.find((s) => s.id === state.ids[state.index]);
    const v = spec.variants[state.preset];
    const srcLang = state.preset === "t2s" ? "zh-Hant" : "zh-Hans";
    const outLang = data.outLang[state.preset];

    const line = fig.querySelector(".line");
    line.lang = srcLang;
    const out = fig.querySelector(".out");
    out.lang = outLang;
    const notes = fig.querySelector(".proof-notes");

    const segNodes = [];
    const outNodes = [];
    const noteNodes = [];
    let mark = 0;
    let j = 0;

    v.segs.forEach((seg) => {
      const kind = seg.k;
      const node = el("span", `seg k-${kind}`);
      const fix = el("span", "fix", kind === "same" || kind === "keep" ? "" : seg.o);
      fix.lang = outLang;
      const cells = el("span", "cells");
      [...seg.s].forEach((ch, i) => {
        const cell = el("span", null, ch);
        if (kind === "keep" && seg.keep && seg.keep.includes(i)) {
          cell.append(svg("keep", "0 0 14 12", data.keep));
        }
        cells.append(cell);
      });
      node.append(fix, cells);
      if (kind !== "same") {
        node.style.setProperty("--i", String(mark));
        if (kind !== "keep") node.append(ring(seg.s.length, mark));
        node.append(el("span", "why", t.kinds[kind]));
        mark += 1;

        const li = el("li", `k-${kind}`);
        li.append(el("span", "from", seg.s));
        if (kind !== "keep") {
          li.append(svg("arrow", "0 0 16 8", "M1 4H14M10.5 1L14.5 4L10.5 7"));
          li.append(el("span", "vh", t.to));
          const to = el("span", "to", seg.o);
          to.lang = outLang;
          li.append(to);
        }
        li.append(el("span", "kind", t.kinds[kind]));
        if (seg.alt) {
          const alt = el("span", "alt", t.alt.replace("{}", seg.alt));
          li.append(alt);
        }
        noteNodes.push(li);
      } else {
        node.append(el("span", "why", ""));
      }
      segNodes.push(node);

      const changed = kind !== "same" && kind !== "keep";
      [...seg.o].forEach((ch) => {
        const cell = el("span", changed ? "chg" : null, ch);
        cell.style.setProperty("--j", String(j));
        j += 1;
        outNodes.push(cell);
      });
    });

    line.replaceChildren(...segNodes);
    out.replaceChildren(...outNodes);
    notes.replaceChildren(...noteNodes);

    const summary = fig.querySelector("[data-summary]");
    if (summary) summary.textContent = t.summary.replace("{src}", v.src).replace("{out}", v.out);

    const live = fig.querySelector("[data-live]");
    if (live && state.announce) {
      live.textContent = t.live
        .replace("{preset}", t.presets[state.preset])
        .replace("{out}", v.out)
        .replace("{n}", String(noteNodes.filter((li) => !li.classList.contains("k-keep")).length));
    }
  }

  function initProof(fig) {
    if (!data) return;
    const ids = (fig.dataset.specimens || "").split(" ").filter(Boolean);
    const state = { ids, index: 0, preset: fig.querySelector("input:checked")?.value || "s2twp", announce: false };

    fig.addEventListener("change", (event) => {
      if (event.target.name !== fig.dataset.group) return;
      state.preset = event.target.value;
      state.announce = true;
      fig.classList.add("is-live");
      render(fig, state);
    });

    const next = fig.querySelector(".proof-next");
    if (next) {
      next.hidden = ids.length < 2;
      next.addEventListener("click", () => {
        state.index = (state.index + 1) % ids.length;
        state.announce = true;
        fig.classList.add("is-live");
        render(fig, state);
      });
    }
  }

  /* Source and result layout demo ------------------------------------------ */

  function initLayout(fig) {
    const group = fig.querySelector(".seg-toggle");
    if (group) group.hidden = false;
    const buttons = [...fig.querySelectorAll("[data-layout-to]")];
    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        const next = button.dataset.layoutTo;
        if (fig.dataset.layout === next) return;
        const apply = () => {
          fig.dataset.layout = next;
          buttons.forEach((b) => b.setAttribute("aria-pressed", String(b === button)));
        };
        if (document.startViewTransition && !reduced()) document.startViewTransition(apply);
        else apply();
      });
    });
  }

  /* Click-to-play film ------------------------------------------------------ */

  function initFilm(plate) {
    const video = plate.querySelector("video");
    const play = plate.querySelector(".film-play");
    if (!video || !play) return;
    video.controls = false;
    play.hidden = false;
    play.addEventListener("click", () => {
      play.hidden = true;
      video.controls = true;
      video.focus();
      const started = video.play();
      if (started) started.catch(() => { video.controls = true; });
    });
  }

  /* Manuscript word count in the colophon ------------------------------------ */

  function initCount(node) {
    const main = document.querySelector("main");
    if (!main) return;
    const text = main.innerText || "";
    let n;
    if (lang.startsWith("zh")) {
      n = (text.match(/[㐀-鿿豈-﫿]/g) || []).length;
      n = Math.round(n / 10) * 10;
    } else {
      n = text.split(/\s+/).filter((w) => /[A-Za-z0-9]/.test(w)).length;
      n = Math.round(n / 10) * 10;
    }
    node.textContent = node.dataset.count.replace("{n}", n.toLocaleString(lang));
    node.hidden = false;
  }

  document.querySelectorAll("[data-proof]").forEach(initProof);
  document.querySelectorAll("[data-layout]").forEach(initLayout);
  document.querySelectorAll("[data-film]").forEach(initFilm);
  document.querySelectorAll("[data-count]").forEach(initCount);
})();
