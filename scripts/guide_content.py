"""Editorial source for the three-language, published-version user guides."""

LOCALES = {
    "en": {
        "label": "Guides",
        "home": "Home",
        "support": "Support",
        "privacy": "Privacy policy",
        "changelog": "Changelog",
        "language": "Language",
        "skip": "Skip to content",
        "hub_title": "OpenCCman guides",
        "hub_description": "Guides to OpenCC, Chinese conversion, regional presets, UTF-8 TXT files and Mac selection shortcuts in OpenCCman.",
        "hub_lede": "Start with a real task. These guides explain what to tap, what changes, and where you may need to review the result.",
        "start": "Start here",
        "read": "Read the guide →",
        "order_title": "A useful order",
        "order": [
            "Convert a short sample and compare the source with the result.",
            "Choose the preset for the audience: OpenCC Traditional, Taiwan or Hong Kong.",
            "Bring in a TXT document only after checking its encoding and size.",
            "On Mac, set up selection shortcuts when you want to work across apps.",
            "Learn how the upstream OpenCC project powers the app and where its scope differs.",
        ],
        "scope": "These steps describe the publicly available 2.0 app on iPhone, iPad and Mac. Features still being tested for 2.1 are listed separately in the changelog.",
        "related": "More guides",
        "back": "All guides",
        "cta_title": "Ready to try it?",
        "cta_body": "OpenCCman converts on your device. Download it for iPhone, iPad or Mac, or check support if a step does not work as described.",
        "download": "Download on the App Store",
    },
    "zh-Hans": {
        "label": "使用指南",
        "home": "首页",
        "support": "联系支持",
        "privacy": "隐私政策",
        "changelog": "更新记录",
        "language": "语言",
        "skip": "跳到正文",
        "hub_title": "OpenCCman 使用指南",
        "hub_description": "了解 OpenCC 开源项目，并学习用 OpenCCman 转换简繁中文、选择地区预设、处理 TXT 文件及设置 Mac 快捷键。",
        "hub_lede": "从要完成的事情开始：在哪里操作、结果会怎样变化，以及哪些地方需要自己校对。",
        "start": "从这里开始",
        "read": "阅读指南 →",
        "order_title": "推荐顺序",
        "order": [
            "先转换一小段文字，对照原文和结果。",
            "按读者选择 OpenCC 繁体、台湾或香港预设。",
            "处理 TXT 文稿前，先检查编码和文件大小。",
            "需要跨 App 工作时，再设置 Mac 选中文字快捷键。",
            "了解提供转换能力的 OpenCC 原始项目，以及它和 App 的区别。",
        ],
        "scope": "以下步骤对应已公开的 iPhone、iPad、Mac 2.0 版。仍在验收的 2.1 功能单独列于更新记录。",
        "related": "继续阅读",
        "back": "所有指南",
        "cta_title": "开始转换",
        "cta_body": "OpenCCman 在设备本地转换文字。可下载 iPhone、iPad、Mac 版；如果步骤与实际画面不符，请联系支持。",
        "download": "在 App Store 下载",
    },
    "zh-Hant": {
        "label": "使用指南",
        "home": "首頁",
        "support": "聯絡支援",
        "privacy": "隱私權政策",
        "changelog": "更新記錄",
        "language": "語言",
        "skip": "跳到正文",
        "hub_title": "OpenCCman 使用指南",
        "hub_description": "認識 OpenCC 開源專案，並學習用 OpenCCman 轉換簡繁中文、選擇地區預設、處理 TXT 檔案及設定 Mac 快捷鍵。",
        "hub_lede": "從要完成的事開始：在哪裡操作、結果如何改變，以及哪些地方需要自行校對。",
        "start": "從這裡開始",
        "read": "閱讀指南 →",
        "order_title": "建議順序",
        "order": [
            "先轉換一小段文字，對照原文與結果。",
            "依讀者選擇 OpenCC 繁體、臺灣或香港預設。",
            "處理 TXT 文件前，先檢查編碼與檔案大小。",
            "需要跨 App 工作時，再設定 Mac 所選文字快捷鍵。",
            "認識提供轉換能力的 OpenCC 原始專案，以及它與 App 的差別。",
        ],
        "scope": "以下步驟對應已公開的 iPhone、iPad、Mac 2.0 版。仍在驗收的 2.1 功能另列於更新記錄。",
        "related": "繼續閱讀",
        "back": "所有指南",
        "cta_title": "開始轉換",
        "cta_body": "OpenCCman 在裝置本機轉換文字。可下載 iPhone、iPad、Mac 版；若步驟與實際畫面不符，請聯絡支援。",
        "download": "在 App Store 下載",
    },
}

# The article body is authored HTML. Its headings, lists, and links are reviewed
# as product copy; the renderer only supplies common metadata and navigation.
ARTICLES = {
    "convert-chinese": {
        "en": {
            "title": "Convert Chinese text on iPhone, iPad or Mac",
            "description": "A first OpenCCman conversion: enter text, choose a preset, compare source and result, then copy the text you need.",
            "card": "Convert your first paragraph",
            "summary": "Enter or paste text, choose a direction, and compare the result before using it.",
            "lede": "You do not need a file or a second device. Start with a short paragraph so you can see how the selected preset changes it.",
            "body": """
<section><h2>Convert a short passage</h2><ol class="guide-steps">
<li><strong>Enter your text.</strong> Type or paste into Source. If the workspace contains an example, replace it with your own words.</li>
<li><strong>Choose a conversion preset.</strong> Select Simplified Chinese, Traditional · OpenCC, Taiwan · Standard + Idioms, or Hong Kong · Traditional. If you are unsure, read the <a href="choose-preset.html">preset guide</a> first.</li>
<li><strong>Choose Convert.</strong> The converted text appears in Result. On iPhone the action sits beside the source area; Mac and iPad can show the two panes side by side or stacked.</li>
<li><strong>Compare before copying.</strong> Review names, specialist terms and sentences where more than one Chinese form is possible. Copy or export only the result you want to use.</li>
</ol></section>
<section><h2>What the result means</h2><p>OpenCC converts character forms and dictionary phrases. It does not translate between languages or rewrite a sentence for a different audience. The Simplified preset is not a complete reverse conversion of Taiwan-specific vocabulary. If you change the preset after converting, run Convert again to produce a result using the new choice.</p><p>Free use includes 12 conversions from the home workspace each day. A conversion that fails or is canceled does not use an allowance; Pro has no home-workspace limit.</p></section>
<aside class="guide-note"><strong>Working with a document?</strong> Import one UTF-8 TXT file instead of pasting a long draft. See the <a href="convert-txt.html">TXT guide</a> for the 10 MiB limit and export behavior.</aside>
""",
        },
        "zh-Hans": {
            "title": "在 iPhone、iPad 或 Mac 转换简繁中文",
            "description": "OpenCCman 入门：输入文字、选择预设、对照原文和结果，再复制需要使用的内容。",
            "card": "转换第一段文字",
            "summary": "输入或粘贴文字，选择转换方向，并在使用前对照结果。",
            "lede": "不需要准备文件或第二台设备。先用一小段文字试转换，便于看清所选预设带来的变化。",
            "body": """
<section><h2>转换一小段文字</h2><ol class="guide-steps">
<li><strong>填入原文。</strong>在“原文”区域输入或粘贴文字。如果工作区已有示例，可先用自己的文字替换。</li>
<li><strong>选择预设。</strong>可选“简体中文”“繁体 · OpenCC”“台湾正体＋台湾词组”“香港繁体”。不确定适用哪项时，先看<a href="choose-preset.html">预设指南</a>。</li>
<li><strong>点击“转换”。</strong>转换后在“结果”区域查看。iPhone 的操作按钮靠近原文区域；Mac 和 iPad 可将原文与结果左右或上下排列。</li>
<li><strong>对照后再使用。</strong>检查人名、品牌、专业术语，以及可能有多种写法的句子；确认后再复制或导出结果。</li>
</ol></section>
<section><h2>结果能做什么</h2><p>OpenCC 转换字形和词典中的词组，不负责语言翻译，也不会自动把整句话改写为另一地区的表达。“简体”预设并非台湾词汇的完整反向转换。转换后若切换预设，需要再次点击“转换”，才会得到新配置下的结果。</p><p>免费版每天可在主页转换 12 次。失败或取消的转换不计次；Pro 不受主页次数限制。</p></section>
<aside class="guide-note"><strong>要处理文稿？</strong>可以导入单个 UTF-8 TXT 文件，不必把长文全部粘贴进来。文件容量和导出方式见 <a href="convert-txt.html">TXT 指南</a>。</aside>
""",
        },
        "zh-Hant": {
            "title": "在 iPhone、iPad 或 Mac 轉換簡繁中文",
            "description": "OpenCCman 入門：輸入文字、選擇預設、對照原文與結果，再複製需要使用的內容。",
            "card": "轉換第一段文字",
            "summary": "輸入或貼上文字，選擇轉換方向，並在使用前對照結果。",
            "lede": "不必準備檔案或第二部裝置。先用一小段文字試轉換，較容易看清所選預設帶來的變化。",
            "body": """
<section><h2>轉換一小段文字</h2><ol class="guide-steps">
<li><strong>填入原文。</strong>在「原文」區域輸入或貼上文字。若工作區已有範例，可先以自己的文字取代。</li>
<li><strong>選擇預設。</strong>可選「簡體中文」「繁體 · OpenCC」「臺灣正體＋臺灣詞組」「香港繁體」。不確定適用哪項時，先看<a href="choose-preset.html">預設指南</a>。</li>
<li><strong>點選「轉換」。</strong>轉換後在「結果」區域查看。iPhone 的操作按鈕靠近原文區域；Mac 和 iPad 可將原文與結果左右或上下排列。</li>
<li><strong>對照後再使用。</strong>檢查人名、品牌、專業術語，以及可能有多種寫法的句子；確認後再複製或匯出結果。</li>
</ol></section>
<section><h2>結果能做什麼</h2><p>OpenCC 轉換字形及詞典中的詞組，不負責語言翻譯，也不會自動把整句話改寫成另一地區的表達。「簡體」預設並非臺灣詞彙的完整反向轉換。轉換後若切換預設，須再次點選「轉換」，才會得到新設定下的結果。</p><p>免費版每天可在首頁轉換 12 次。失敗或取消的轉換不計次；Pro 不受首頁次數限制。</p></section>
<aside class="guide-note"><strong>要處理文件？</strong>可以匯入單個 UTF-8 TXT 檔案，不必把長文全部貼進來。檔案容量與匯出方式見 <a href="convert-txt.html">TXT 指南</a>。</aside>
""",
        },
    },
    "choose-preset": {
        "en": {
            "title": "Choose between Traditional, Taiwan and Hong Kong presets",
            "description": "Understand OpenCC Traditional, Taiwan Standard with idioms, Hong Kong Traditional and Simplified presets in OpenCCman.",
            "card": "Choose the right Chinese preset",
            "summary": "Decide whether you need general Traditional forms, Taiwan vocabulary, Hong Kong forms or Simplified text.",
            "lede": "“Traditional Chinese” is not one uniform output. Choose a preset for your readers, then review the terms that matter to them.",
            "body": """
<section><h2>The four presets</h2><dl class="guide-definitions">
<dt>Simplified Chinese</dt><dd>Produces Simplified characters. It is not a complete reverse conversion of Taiwan-specific words or phrases.</dd>
<dt>Traditional · OpenCC</dt><dd>Uses OpenCC's standard Traditional form. This is an internal conversion standard, not a promise to match every Taiwan or Hong Kong usage.</dd>
<dt>Taiwan · Standard + Idioms</dt><dd>Applies Taiwan character variants and Taiwan phrase conversion as well as Simplified-to-Traditional conversion. Choose it when the intended readers use Taiwan writing conventions.</dd>
<dt>Hong Kong · Traditional</dt><dd>Applies Hong Kong character variants. The preset does not add a separate Hong Kong idiom option in OpenCCman.</dd>
</dl></section>
<section><h2>A practical choice</h2><ol class="guide-steps"><li><strong>Know your audience.</strong> For Taiwan-facing copy start with Taiwan Standard with idioms; for Hong Kong-facing copy start with Hong Kong Traditional.</li><li><strong>Keep an original.</strong> Compare the source and result, especially for names, brands, quotations and technical terms.</li><li><strong>Use advanced controls only when needed.</strong> Other combinations appear as Custom. Change one setting at a time and reconvert so you can see its effect.</li></ol></section>
<aside class="guide-note">OpenCC's <a href="https://github.com/BYVoid/OpenCC/blob/master/DESIGN_PRINCIPLES.md">design principles</a> explain why its `t`, `tw` and `hk` modes are conversion conventions rather than guarantees of a particular style guide.</aside>
""",
        },
        "zh-Hans": {
            "title": "怎么选 OpenCC 繁体、台湾和香港预设",
            "description": "了解 OpenCCman 四个转换预设的适用场景：简体、OpenCC 繁体、台湾正体加词组与香港繁体。",
            "card": "选对简繁与地区预设",
            "summary": "分清通用繁体、台湾词组、香港字形与简体输出。",
            "lede": "“繁体中文”不是唯一的输出形式。先按读者选择预设，再校对对方在意的用词。",
            "body": """
<section><h2>四个预设分别做什么</h2><dl class="guide-definitions">
<dt>简体中文</dt><dd>输出简化字；不代表能把所有台湾地区用语完整反向转换。</dd>
<dt>繁体 · OpenCC</dt><dd>使用 OpenCC 标准繁体。这是转换用的中间标准，不保证逐项符合台湾或香港的实际用字。</dd>
<dt>台湾正体＋台湾词组</dt><dd>在简转繁之外，应用台湾字形和地区词组转换。面向台湾读者时，可从这里开始。</dd>
<dt>香港繁体</dt><dd>应用香港字形。OpenCCman 的这项预设没有另加独立的香港惯用词选项。</dd>
</dl></section>
<section><h2>如何做选择</h2><ol class="guide-steps"><li><strong>先看读者。</strong>面向台湾的文案先试“台湾正体＋台湾词组”；面向香港的文案先试“香港繁体”。</li><li><strong>保留原文对照。</strong>特别检查人名、品牌、引文和专业词汇。</li><li><strong>需要时再用高级选项。</strong>其他组合会显示“自定义”。一次调整一项并重新转换，便于看出差异。</li></ol></section>
<aside class="guide-note">OpenCC 的<a href="https://github.com/BYVoid/OpenCC/blob/master/DESIGN_PRINCIPLES.md">设计原则</a>说明 `t`、`tw`、`hk` 是转换模式，并非符合特定地区编辑规范的保证。</aside>
""",
        },
        "zh-Hant": {
            "title": "如何選擇 OpenCC 繁體、臺灣和香港預設",
            "description": "了解 OpenCCman 四個轉換預設的適用情境：簡體、OpenCC 繁體、臺灣正體加詞組與香港繁體。",
            "card": "選對簡繁與地區預設",
            "summary": "分清通用繁體、臺灣詞組、香港字形與簡體輸出。",
            "lede": "「繁體中文」不是唯一的輸出形式。先依讀者選擇預設，再校對對方在意的用詞。",
            "body": """
<section><h2>四個預設分別做什麼</h2><dl class="guide-definitions">
<dt>簡體中文</dt><dd>輸出簡化字；不代表能把所有臺灣地區用語完整反向轉換。</dd>
<dt>繁體 · OpenCC</dt><dd>使用 OpenCC 標準繁體。這是轉換用的中間標準，不保證逐項符合臺灣或香港的實際用字。</dd>
<dt>臺灣正體＋臺灣詞組</dt><dd>在簡轉繁之外，套用臺灣字形與地區詞組轉換。面向臺灣讀者時，可從這裡開始。</dd>
<dt>香港繁體</dt><dd>套用香港字形。OpenCCman 的這項預設沒有另加獨立的香港慣用詞選項。</dd>
</dl></section>
<section><h2>如何做選擇</h2><ol class="guide-steps"><li><strong>先看讀者。</strong>面向臺灣的文案先試「臺灣正體＋臺灣詞組」；面向香港的文案先試「香港繁體」。</li><li><strong>保留原文對照。</strong>特別檢查人名、品牌、引文與專業詞彙。</li><li><strong>需要時再用進階選項。</strong>其他組合會顯示「自訂」。一次調整一項並重新轉換，便於看出差異。</li></ol></section>
<aside class="guide-note">OpenCC 的<a href="https://github.com/BYVoid/OpenCC/blob/master/DESIGN_PRINCIPLES.md">設計原則</a>說明 `t`、`tw`、`hk` 是轉換模式，並非符合特定地區編輯規範的保證。</aside>
""",
        },
    },
    "convert-txt": {
        "en": {
            "title": "Convert a UTF-8 TXT file without losing your draft",
            "description": "Import or drop one UTF-8 TXT file up to 10 MiB in OpenCCman, convert it, and export the latest result as UTF-8.",
            "card": "Convert a TXT document",
            "summary": "Check encoding and size, import one file, then export the converted result.",
            "lede": "Use the file workflow for a document you want to keep as a TXT file. The public 2.0 app handles one UTF-8 file at a time, up to 10 MiB.",
            "body": """
<section><h2>Before importing</h2><p>Save the document as plain-text <code>.txt</code> in UTF-8. A UTF-8 byte-order mark (BOM) is accepted. The app does not guess Big5, GBK or another encoding. If the file exceeds 10 MiB, reduce it or split it before using the public 2.0 workflow.</p></section>
<section><h2>Import, convert, export</h2><ol class="guide-steps"><li><strong>Import one file.</strong> Choose Import TXT in the workspace, or drop a single TXT file onto it. A successful import replaces the source text.</li><li><strong>Choose a preset and convert.</strong> Read the source and result together; a new file is not saved automatically.</li><li><strong>Choose Export TXT.</strong> The app exports the latest successful result as UTF-8 without a BOM. For example, <code>essay.txt</code> suggests <code>essay-converted.txt</code>; choose the save location in the system panel.</li></ol></section>
<section><h2>If something goes wrong</h2><p>An oversized or invalidly encoded import keeps the previous draft. A failed or canceled conversion does not replace the last successful result. The file flow preserves line endings, blank lines, Emoji, combining characters and embedded U+0000; still inspect the converted words before sharing the document.</p><p>Large-file Pro conversion is described in the <a href="../changelog.html">2.1 candidate notes</a> and is not part of this public 2.0 guide.</p></section>
""",
        },
        "zh-Hans": {
            "title": "如何转换 UTF-8 TXT 文稿并导出结果",
            "description": "在 OpenCCman 中导入或拖入不超过 10 MiB 的单个 UTF-8 TXT 文件，转换后导出最新成功结果。",
            "card": "转换 TXT 文稿",
            "summary": "检查编码和大小，导入单个文件，再导出转换结果。",
            "lede": "要把文稿继续保存为 TXT，可使用文件工作流。已公开的 2.0 版每次处理一个 UTF-8 文件，上限 10 MiB。",
            "body": """
<section><h2>导入前先检查</h2><p>把文稿存为 UTF-8 编码的纯文本 <code>.txt</code>。可以带 UTF-8 BOM。应用不会猜测 Big5、GBK 等其他编码。如果文件超过 10 MiB，请先缩小或拆分，再使用已公开的 2.0 工作流。</p></section>
<section><h2>导入、转换、导出</h2><ol class="guide-steps"><li><strong>导入一个文件。</strong>在工作区选择“导入 TXT”，或把单个 TXT 文件拖入工作区。导入成功后会替换原文。</li><li><strong>选择预设并转换。</strong>对照原文和结果；转换完成不会自动保存新文件。</li><li><strong>选择“导出 TXT”。</strong>应用把最近一次成功结果存为不带 BOM 的 UTF-8。例如导入 <code>essay.txt</code> 时，建议文件名是 <code>essay-converted.txt</code>；保存位置由系统面板选择。</li></ol></section>
<section><h2>遇到错误时</h2><p>文件过大或编码无效时，原有文稿不会被覆盖。转换失败或取消也不会替换最近一次成功结果。文件流程保留换行、空行、Emoji、组合字符和 U+0000；分享前仍应校对转换后的用词。</p><p>大文件 Pro 转换见<a href="../changelog.html">2.1 候选版说明</a>，不属于已公开的 2.0 指南。</p></section>
""",
        },
        "zh-Hant": {
            "title": "如何轉換 UTF-8 TXT 文件並匯出結果",
            "description": "在 OpenCCman 匯入或拖入不超過 10 MiB 的單個 UTF-8 TXT 檔案，轉換後匯出最近一次成功結果。",
            "card": "轉換 TXT 文件",
            "summary": "檢查編碼與大小，匯入單個檔案，再匯出轉換結果。",
            "lede": "要把文件繼續儲存為 TXT，可使用檔案流程。已公開的 2.0 版每次處理一個 UTF-8 檔案，上限 10 MiB。",
            "body": """
<section><h2>匯入前先檢查</h2><p>把文件儲存為 UTF-8 編碼的純文字 <code>.txt</code>。可以包含 UTF-8 BOM。App 不會猜測 Big5、GBK 等其他編碼。若檔案超過 10 MiB，請先縮小或拆分，再使用已公開的 2.0 流程。</p></section>
<section><h2>匯入、轉換、匯出</h2><ol class="guide-steps"><li><strong>匯入一個檔案。</strong>在工作區選擇「匯入 TXT」，或把單個 TXT 檔案拖入工作區。匯入成功後會取代原文。</li><li><strong>選擇預設並轉換。</strong>對照原文與結果；轉換完成不會自動儲存新檔案。</li><li><strong>選擇「匯出 TXT」。</strong>App 把最近一次成功結果存成不帶 BOM 的 UTF-8。例如匯入 <code>essay.txt</code> 時，建議檔名為 <code>essay-converted.txt</code>；儲存位置由系統面板選擇。</li></ol></section>
<section><h2>遇到錯誤時</h2><p>檔案過大或編碼無效時，原有文件不會被覆蓋。轉換失敗或取消也不會取代最近一次成功結果。檔案流程保留換行、空行、Emoji、組合字元與 U+0000；分享前仍應校對轉換後的用詞。</p><p>大檔案 Pro 轉換見<a href="../changelog.html">2.1 候選版說明</a>，不屬於已公開的 2.0 指南。</p></section>
""",
        },
    },
    "mac-shortcuts": {
        "en": {
            "title": "Convert selected Chinese text with a Mac shortcut",
            "description": "Set up OpenCCman Mac global shortcuts and Services to convert selected text across apps, with Accessibility and safe fallback explained.",
            "card": "Use Mac selection shortcuts",
            "summary": "Configure a shortcut, grant Accessibility access, and choose between replacement and opening the selection in OpenCCman.",
            "lede": "The Mac app can work with selected text in another app. Use the open action when you want to inspect the result before changing the original document.",
            "body": """
<section><h2>Set up the shortcuts</h2><ol class="guide-steps"><li><strong>Open Settings → Global Shortcut.</strong> Grant Accessibility permission when prompted, then return to the app and choose Refresh to confirm the status.</li><li><strong>Enable and record the keys.</strong> Turn on the global shortcut switch. Record separate key combinations for Convert Selected Text and Open Selected Text; change them if they conflict with another app.</li><li><strong>Select text in the source app.</strong> Put focus in the document, select the Chinese text, then use your chosen shortcut. The Open action brings the selection into OpenCCman for review. The Convert action attempts to replace an editable selection and also shows the result in OpenCCman.</li></ol></section>
<section><h2>When replacement does not happen</h2><p>Automatic replacement depends on Accessibility permission and the source app's selection and editing support. If the selection or destination cannot be confirmed safely, use the result in OpenCCman and paste it yourself. The original app may also reserve the same key combination, so try another recording if the shortcut never fires.</p><p>macOS Services provide another route: select text, open the source app's Services menu, then choose an OpenCCman conversion or open action if that app exposes Services. The open action is a good choice for read-only fields.</p></section>
<aside class="guide-note">Global shortcuts and Services are Mac features. On iPhone or iPad, use the <a href="convert-chinese.html">in-app conversion workflow</a>.</aside>
""",
        },
        "zh-Hans": {
            "title": "用 Mac 全局快捷键转换其他 App 选中的中文",
            "description": "设置 OpenCCman Mac 全局快捷键和系统服务，了解辅助功能权限、自动替换条件与安全回退方式。",
            "card": "设置 Mac 选中文字快捷键",
            "summary": "配置快捷键和辅助功能权限，在自动替换与打开 App 校对之间选择。",
            "lede": "Mac 版可以处理其他 App 中选中的文字。若想先检查结果再修改原稿，可用“打开选中文字”操作。",
            "body": """
<section><h2>设置快捷键</h2><ol class="guide-steps"><li><strong>打开“设置 → 全局快捷键”。</strong>按提示授予辅助功能权限，回到 App 后点击“刷新”，确认权限状态。</li><li><strong>开启并录入组合键。</strong>打开全局快捷键开关，分别在“转换选中文本快捷键”和“打开选中文本快捷键”录入组合键；若与别的 App 冲突，可改用其他组合。</li><li><strong>在来源 App 选中文字。</strong>让文稿获得焦点，选中中文后按快捷键。“打开”会带着原文进入 OpenCCman，供你校对；“转换”会尝试替换可编辑的选区，也会在 OpenCCman 显示结果。</li></ol></section>
<section><h2>未能自动替换怎么办</h2><p>自动替换取决于辅助功能权限，以及来源 App 是否支持读取和编辑选区。如果无法安全确认选区或目标，可以在 OpenCCman 查看结果，再手动复制粘贴。若快捷键完全没有反应，也要检查组合键是否被其他 App 占用。</p><p>还可以试 macOS 系统服务：选中文字后，在来源 App 的“服务”菜单中选择 OpenCCman 的转换或打开操作，前提是该 App 提供相关服务入口。只读区域更适合使用“打开”操作。</p></section>
<aside class="guide-note">全局快捷键和系统服务是 Mac 功能。在 iPhone 或 iPad 上，请使用<a href="convert-chinese.html">应用内转换流程</a>。</aside>
""",
        },
        "zh-Hant": {
            "title": "用 Mac 全域快捷鍵轉換其他 App 所選中文",
            "description": "設定 OpenCCman Mac 全域快捷鍵及系統服務，了解輔助使用權限、自動取代條件與安全回退方式。",
            "card": "設定 Mac 所選文字快捷鍵",
            "summary": "設定快捷鍵及輔助使用權限，在自動取代與開啟 App 校對之間選擇。",
            "lede": "Mac 版可以處理其他 App 中選取的文字。若想先檢查結果再修改原稿，可使用「開啟所選文字」操作。",
            "body": """
<section><h2>設定快捷鍵</h2><ol class="guide-steps"><li><strong>開啟「設定 → 全域快速鍵」。</strong>依提示授予輔助使用權限，回到 App 後點選「重新整理」，確認權限狀態。</li><li><strong>啟用並錄入組合鍵。</strong>開啟全域快速鍵開關，分別在「轉換選中文本快速鍵」與「打開選中文本快速鍵」錄入組合鍵；若與其他 App 衝突，可改用其他組合。</li><li><strong>在來源 App 選取文字。</strong>讓文件取得焦點，選取中文後按快捷鍵。「開啟」會把原文帶進 OpenCCman 供你校對；「轉換」會嘗試取代可編輯的選區，也會在 OpenCCman 顯示結果。</li></ol></section>
<section><h2>未能自動取代怎麼辦</h2><p>自動取代取決於輔助使用權限，以及來源 App 是否支援讀取與編輯選區。若無法安全確認選區或目標，可以在 OpenCCman 查看結果，再手動複製貼上。若快捷鍵完全沒有反應，也要檢查組合鍵是否被其他 App 佔用。</p><p>也可試 macOS 系統服務：選取文字後，在來源 App 的「服務」選單中選擇 OpenCCman 的轉換或開啟操作，前提是該 App 提供相關服務入口。唯讀區域較適合使用「開啟」操作。</p></section>
<aside class="guide-note">全域快捷鍵與系統服務是 Mac 功能。在 iPhone 或 iPad 上，請使用<a href="convert-chinese.html">App 內轉換流程</a>。</aside>
""",
        },
    },
    "about-opencc": {
        "en": {
            "title": "What is OpenCC? Meet the open-source project behind OpenCCman",
            "description": "Learn what Open Chinese Convert provides, how dictionary-based conversion differs from translation, and how OpenCCman uses the upstream project.",
            "card": "Meet the OpenCC project",
            "summary": "See what the open-source conversion engine does and how it relates to the Apple app.",
            "lede": "Open Chinese Convert (OpenCC) is the open-source project that supplies the conversion engine and dictionaries used by OpenCCman.",
            "scope": "This article introduces the upstream project. OpenCCman exposes a selected set of its capabilities; see the other guides for the app's actual controls and limits.",
            "body": """
<section><h2>What does OpenCC provide?</h2><p>OpenCC provides conversion dictionaries, a reusable library, command-line tools and dictionary-building tools. Its configurable conversion chains distinguish Simplified and Traditional characters, character variants, and some regional word choices for Mainland China, Taiwan and Hong Kong. The conversion is dictionary-based and deterministic; it can run offline without a generative AI service.</p><p>OpenCC also documents limited Japanese character-form conversion. That upstream capability is separate from the presets described in this site's <a href="choose-preset.html">OpenCCman preset guide</a>.</p></section>
<section><h2>How does OpenCCman relate to it?</h2><p><a href="https://github.com/BYVoid/OpenCC">OpenCC</a> is the upstream open-source project. <a href="https://github.com/gewill/OpenCCman">OpenCCman</a> is a separate iPhone, iPad and Mac app that integrates the engine through a Swift package. The app adds an Apple-platform interface, presets, TXT import and export, and Mac selection shortcuts. It is not an official OpenCC app and does not expose every upstream configuration or command-line feature.</p><p>If you want to convert text in the app, start with the <a href="convert-chinese.html">first-conversion guide</a>. If you need to develop against OpenCC itself, use the upstream repository and documentation.</p></section>
<section><h2>What are the limits, and where can I read more?</h2><p>OpenCC changes character forms and dictionary phrases. It does not translate between languages such as Mandarin and Cantonese, and its output is not a substitute for reviewing names, quotations or specialist terms. Which regional forms appear depends on the selected conversion configuration.</p><p>Read the upstream <a href="https://github.com/BYVoid/OpenCC#readme">README</a> for supported tools and configurations, its <a href="https://github.com/BYVoid/OpenCC/blob/master/DESIGN_PRINCIPLES.md">design principles</a> for conversion rules, and the <a href="https://github.com/BYVoid/OpenCC/blob/master/LICENSE">Apache 2.0 license</a> for the project's terms. OpenCCman has its own <a href="https://github.com/gewill/OpenCCman">source repository</a>.</p></section>
""",
        },
        "zh-Hans": {
            "title": "OpenCC 是什么？认识 OpenCCman 使用的开源项目",
            "description": "介绍 Open Chinese Convert 的词库与转换工具、它和语言翻译的区别，以及 OpenCCman 与原始项目的关系。",
            "card": "认识 OpenCC 原始项目",
            "summary": "了解开源转换引擎能做什么，以及它和 Apple 平台 App 的关系。",
            "lede": "OpenCC（Open Chinese Convert，开放中文转换）是提供 OpenCCman 所用转换引擎与词库的开源项目。",
            "scope": "本文介绍 OpenCC 原始项目。OpenCCman 只提供其中一部分能力；App 的实际操作和限制请以其他指南为准。",
            "body": """
<section><h2>OpenCC 提供什么？</h2><p>OpenCC 提供转换词库、可复用的程序库、命令行工具和词库生成工具。它通过可配置的转换链区分简繁字形、异体字，以及中国大陆、台湾、香港的部分地区用词。转换由词典规则决定，可离线运行，不依赖生成式 AI 服务。</p><p>上游还记录了有限的日文字形转换能力；这不等于 OpenCCman 的<a href="choose-preset.html">预设</a>提供日文转换。</p></section>
<section><h2>它和 OpenCCman 是什么关系？</h2><p><a href="https://github.com/BYVoid/OpenCC">OpenCC</a> 是原始开源项目；<a href="https://github.com/gewill/OpenCCman">OpenCCman</a> 是通过 Swift 软件包接入引擎的独立 iPhone、iPad 和 Mac 应用。App 增加了 Apple 平台界面、转换预设、TXT 导入导出和 Mac 选中文字快捷键。OpenCCman 不是 OpenCC 官方 App，也没有开放上游的全部配置和命令行能力。</p><p>想在 App 中转换文字，可先看<a href="convert-chinese.html">入门指南</a>；要开发或使用 OpenCC 原始工具，请看上游仓库与文档。</p></section>
<section><h2>转换的边界与官方资料</h2><p>OpenCC 处理字形和词典中的词组，不负责普通话与粤语等语言之间的翻译。人名、引文和专业术语仍值得人工校对；具体地区写法取决于所选转换配置。</p><p>从上游 <a href="https://github.com/BYVoid/OpenCC#readme">README</a> 查看工具与配置，阅读<a href="https://github.com/BYVoid/OpenCC/blob/master/DESIGN_PRINCIPLES.md">设计原则</a>了解转换规则，或查看该项目的 <a href="https://github.com/BYVoid/OpenCC/blob/master/LICENSE">Apache 2.0 许可协议</a>。OpenCCman 的源码在<a href="https://github.com/gewill/OpenCCman">独立仓库</a>。</p></section>
""",
        },
        "zh-Hant": {
            "title": "OpenCC 是什麼？認識 OpenCCman 使用的開源專案",
            "description": "介紹 Open Chinese Convert 的詞庫與轉換工具、它與語言翻譯的差別，以及 OpenCCman 和原始專案的關係。",
            "card": "認識 OpenCC 原始專案",
            "summary": "了解開源轉換引擎能做什麼，以及它與 Apple 平台 App 的關係。",
            "lede": "OpenCC（Open Chinese Convert，開放中文轉換）是提供 OpenCCman 所用轉換引擎與詞庫的開源專案。",
            "scope": "本文介紹 OpenCC 原始專案。OpenCCman 只提供其中一部分能力；App 的實際操作與限制請以其他指南為準。",
            "body": """
<section><h2>OpenCC 提供什麼？</h2><p>OpenCC 提供轉換詞庫、可重用的程式庫、命令列工具及詞庫生成工具。它透過可設定的轉換鏈區分簡繁字形、異體字，以及中國大陸、臺灣、香港的部分地區用詞。轉換由詞典規則決定，可離線執行，不依賴生成式 AI 服務。</p><p>上游也記錄了有限的日文字形轉換能力；這不表示 OpenCCman 的<a href="choose-preset.html">預設</a>提供日文轉換。</p></section>
<section><h2>它與 OpenCCman 是什麼關係？</h2><p><a href="https://github.com/BYVoid/OpenCC">OpenCC</a> 是原始開源專案；<a href="https://github.com/gewill/OpenCCman">OpenCCman</a> 是透過 Swift 套件接入引擎的獨立 iPhone、iPad 和 Mac App。App 加入了 Apple 平台介面、轉換預設、TXT 匯入匯出及 Mac 所選文字快捷鍵。OpenCCman 不是 OpenCC 官方 App，也未提供上游的全部設定與命令列功能。</p><p>想在 App 中轉換文字，可先看<a href="convert-chinese.html">入門指南</a>；若要開發或使用 OpenCC 原始工具，請參考上游儲存庫及文件。</p></section>
<section><h2>轉換的邊界與官方資料</h2><p>OpenCC 處理字形及詞典中的詞組，不負責國語與粵語等語言之間的翻譯。人名、引文及專業術語仍應人工校對；具體地區寫法取決於所選轉換設定。</p><p>從上游 <a href="https://github.com/BYVoid/OpenCC#readme">README</a> 查看工具與設定，閱讀<a href="https://github.com/BYVoid/OpenCC/blob/master/DESIGN_PRINCIPLES.md">設計原則</a>了解轉換規則，或查看該專案的 <a href="https://github.com/BYVoid/OpenCC/blob/master/LICENSE">Apache 2.0 授權條款</a>。OpenCCman 的原始碼在<a href="https://github.com/gewill/OpenCCman">獨立儲存庫</a>。</p></section>
""",
        },
    },
}
