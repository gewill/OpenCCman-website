"""Reviewed copy for the home, changelog, support, privacy, 404 and language pages.

Guides live in guide_content.py. Facts, limits and the privacy wording are owner
approved: change them only with the owner. build_site.py renders everything.
"""

UI = {
    "zh-Hans": {
        "skip": "跳到正文",
        "nav": "网站导航",
        "langs": "语言",
        "foot": "网站链接",
        "home": "首页",
        "guides": "使用指南",
        "changelog": "更新记录",
        "support": "联系支持",
        "privacy": "隐私政策",
        "download": "在 App Store 下载",
        "count": "本页约 {n} 字",
        "imprint": "中文转换 · 为 Apple 设备而作",
        "note": "注"
    },
    "zh-Hant": {
        "skip": "跳到正文",
        "nav": "網站導覽",
        "langs": "語言",
        "foot": "網站連結",
        "home": "首頁",
        "guides": "使用指南",
        "changelog": "更新紀錄",
        "support": "聯絡支援",
        "privacy": "隱私權政策",
        "download": "在 App Store 下載",
        "count": "本頁約 {n} 字",
        "imprint": "中文轉換 · 為 Apple 裝置而作",
        "note": "註"
    },
    "en": {
        "skip": "Skip to content",
        "nav": "Site",
        "langs": "Language",
        "foot": "Site links",
        "home": "Home",
        "guides": "Guides",
        "changelog": "Changelog",
        "support": "Support",
        "privacy": "Privacy policy",
        "download": "Download on the App Store",
        "count": "About {n} words",
        "imprint": "Chinese conversion · Made for Apple devices",
        "note": "Note"
    }
}

LANG_CELLS = [
    [
        "zh-Hans",
        "简",
        "简体中文"
    ],
    [
        "zh-Hant",
        "繁",
        "繁體中文"
    ],
    [
        "en",
        "EN",
        "English"
    ]
]

# Proof desk labels; the conversions themselves come from specimens.json.
PROOF = {
    "zh-Hans": {
        "presets": {
            "t2s": "简体中文",
            "s2t": "繁体 · OpenCC",
            "s2twp": "台湾正体＋台湾词组",
            "s2hk": "香港繁体"
        },
        "kinds": {
            "char": "字形",
            "phrase": "词组",
            "keep": "保留",
            "twp": "台湾用语",
            "twv": "台湾字形",
            "hkv": "香港字形"
        },
        "src": "原文",
        "out": "结果",
        "next": "换一句",
        "legend": "转换预设",
        "to": "改为",
        "alt": "逐字会成「{}」",
        "notes": "校对记录",
        "live": "{preset}：{out}。改动 {n} 处。",
        "summary": "原文：{src}。结果：{out}。",
        "caption": "示例：OpenCC 1.4.2 的实际转换结果，并非 App 截图。"
    },
    "zh-Hant": {
        "presets": {
            "t2s": "簡體中文",
            "s2t": "繁體 · OpenCC",
            "s2twp": "臺灣正體＋臺灣詞組",
            "s2hk": "香港繁體"
        },
        "kinds": {
            "char": "字形",
            "phrase": "詞組",
            "keep": "保留",
            "twp": "臺灣用語",
            "twv": "臺灣字形",
            "hkv": "香港字形"
        },
        "src": "原文",
        "out": "結果",
        "next": "換一句",
        "legend": "轉換預設",
        "to": "改為",
        "alt": "逐字會成「{}」",
        "notes": "校對記錄",
        "live": "{preset}：{out}。改動 {n} 處。",
        "summary": "原文：{src}。結果：{out}。",
        "caption": "範例：OpenCC 1.4.2 的實際轉換結果，並非 App 截圖。"
    },
    "en": {
        "presets": {
            "t2s": "Simplified Chinese",
            "s2t": "Traditional · OpenCC",
            "s2twp": "Taiwan · Standard + Idioms",
            "s2hk": "Hong Kong · Traditional"
        },
        "kinds": {
            "char": "Char",
            "phrase": "Phrase",
            "keep": "Kept",
            "twp": "TW term",
            "twv": "TW form",
            "hkv": "HK form"
        },
        "src": "Source",
        "out": "Result",
        "next": "Another sentence",
        "legend": "Conversion preset",
        "to": "becomes",
        "alt": "char by char: {}",
        "notes": "Proof notes",
        "live": "{preset}: {out}. {n} changes.",
        "summary": "Source: {src}. Result: {out}.",
        "caption": "Example: actual OpenCC 1.4.2 output, not an app screenshot."
    }
}

HOME = {
    "zh-Hans": {
        "title": "OpenCCman — 让中文，恰如其分。",
        "description": "OpenCCman 2.0 支持 Mac 全局快捷键、TXT 导入导出，以及 iPhone、iPad、Mac 上的原文结果对照。基于 OpenCC，在设备本地转换简繁与地区用语。",
        "h1": [
            "让中文，",
            "恰如其分。"
        ],
        "intro": "OpenCCman 2.0 支持 Mac 全局快捷键、TXT 导入导出，以及 iPhone、iPad、Mac 上的原文结果对照。基于 OpenCC，在设备本地转换简繁与地区用语。",
        "platforms": "iPhone · iPad · Mac",
        "features_title": "熟悉的文字，合适的表达。",
        "features": [
            [
                "Mac 全局快捷键",
                "在其他应用中选中文字，可直接转换并替换可编辑内容，或送到 OpenCCman 检查。替换需辅助功能权限及来源应用支持。"
            ],
            [
                "原文结果同屏",
                "Mac 与 iPad 可左右或上下对照；四个预设让常用的简体、繁体及地区用语转换更容易开始。"
            ],
            [
                "带上 TXT 文稿",
                "导入或拖入单个 UTF-8 TXT 文件，转换后导出结果。支持不超过 10 MiB 的文件，正文在本机处理。"
            ]
        ],
        "fig": {
            "other_app": "其他 App",
            "key": "快捷键",
            "replace": "转换并替换",
            "open": "送到 OpenCCman 检查",
            "app_line": "原文 · 结果",
            "fig_caption": "示例 · 台湾正体＋台湾词组",
            "side": "左右",
            "stacked": "上下",
            "layout_label": "排列方式",
            "src": "原文",
            "out": "结果",
            "local": "正文在本机处理",
            "chips": [
                "单个文件",
                "UTF-8",
                "不超过 10 MiB"
            ]
        },
        "film_title": "看看 OpenCCman 2.0 如何工作。",
        "film_lead": "选择预设，对照原文与结果，在 iPhone、iPad 和 Mac 上处理 TXT 文稿。OpenCCman 2.0 已在 App Store 上架。",
        "film_note": "产品视频 · 25 秒 · 含音乐",
        "film_load": "点击后才加载 · 约 3 MB",
        "film_play": "播放产品视频",
        "film_download": "下载视频",
        "guides_title": "从手头的文字开始。",
        "guides_body": "了解如何选择预设、转换 TXT 文稿，以及使用 Mac 选中文字快捷键。每篇都写明需要注意的限制。",
        "guides_link": "查看使用指南",
        "closing_title": "把注意力留给文字。",
        "closing_break": "把注意力",
        "closing_body": "下载 OpenCCman，开始你的下一次中文转换。"
    },
    "zh-Hant": {
        "title": "OpenCCman — 讓中文，恰如其分。",
        "description": "OpenCCman 2.0 支援 Mac 全域快速鍵、TXT 匯入匯出，以及 iPhone、iPad、Mac 上的原文結果對照。以 OpenCC 在裝置本機轉換簡繁與地區用語。",
        "h1": [
            "讓中文，",
            "恰如其分。"
        ],
        "intro": "OpenCCman 2.0 支援 Mac 全域快速鍵、TXT 匯入匯出，以及 iPhone、iPad、Mac 上的原文結果對照。以 OpenCC 在裝置本機轉換簡繁與地區用語。",
        "platforms": "iPhone · iPad · Mac",
        "features_title": "熟悉的文字，合適的表達。",
        "features": [
            [
                "Mac 全域快速鍵",
                "在其他 App 中選取文字，可直接轉換並取代可編輯內容，或送到 OpenCCman 檢查。取代需輔助使用權限及來源 App 支援。"
            ],
            [
                "原文結果同屏",
                "Mac 與 iPad 可左右或上下對照；四個預設讓常用的簡體、繁體及地區用語轉換更容易開始。"
            ],
            [
                "帶上 TXT 文稿",
                "匯入或拖入單一 UTF-8 TXT 檔案，轉換後匯出結果。支援不超過 10 MiB 的檔案，正文在本機處理。"
            ]
        ],
        "fig": {
            "other_app": "其他 App",
            "key": "快速鍵",
            "replace": "轉換並取代",
            "open": "送到 OpenCCman 檢查",
            "app_line": "原文 · 結果",
            "fig_caption": "範例 · 臺灣正體＋臺灣詞組",
            "side": "左右",
            "stacked": "上下",
            "layout_label": "排列方式",
            "src": "原文",
            "out": "結果",
            "local": "正文在本機處理",
            "chips": [
                "單一檔案",
                "UTF-8",
                "不超過 10 MiB"
            ]
        },
        "film_title": "看看 OpenCCman 2.0 如何運作。",
        "film_lead": "選擇預設，對照原文與結果，在 iPhone、iPad 和 Mac 上處理 TXT 文稿。OpenCCman 2.0 已於 App Store 上架。",
        "film_note": "產品影片 · 25 秒 · 含音樂",
        "film_load": "點擊後才載入 · 約 3 MB",
        "film_play": "播放產品影片",
        "film_download": "下載影片",
        "guides_title": "從手邊的文字開始。",
        "guides_body": "了解如何選擇預設、轉換 TXT 文件，以及使用 Mac 所選文字快捷鍵。每篇都說明需要留意的限制。",
        "guides_link": "查看使用指南",
        "closing_title": "把注意力留給文字。",
        "closing_break": "把注意力",
        "closing_body": "下載 OpenCCman，開始你的下一次中文轉換。"
    },
    "en": {
        "title": "OpenCCman — Chinese, in the right words.",
        "description": "OpenCCman 2.0 brings Mac global shortcuts, TXT import and export, and a flexible source-and-result workspace to iPhone, iPad and Mac. Convert Chinese on your device with OpenCC.",
        "h1": [
            "Chinese, in the right words."
        ],
        "intro": "OpenCCman 2.0 brings Mac global shortcuts, TXT import and export, and a flexible source-and-result workspace to iPhone, iPad and Mac. Convert Chinese on your device with OpenCC.",
        "platforms": "iPhone · iPad · Mac",
        "features_title": "Familiar words. Regional nuance.",
        "features": [
            [
                "Mac global shortcuts",
                "Convert selected text in another app and replace it in an editable field, or open the selection in OpenCCman. Requires Accessibility permission and a compatible source app."
            ],
            [
                "Read source and result together",
                "Compare both panes side by side or stacked on Mac and iPad. Four presets make common Chinese conversions easier to start."
            ],
            [
                "Bring a TXT file",
                "Import or drop one UTF-8 TXT file, then export the converted result. Files up to 10 MiB are supported; conversion runs locally."
            ]
        ],
        "fig": {
            "other_app": "Another app",
            "key": "Shortcut",
            "replace": "Convert and replace",
            "open": "Open in OpenCCman",
            "app_line": "Source · Result",
            "fig_caption": "Example · Taiwan · Standard + Idioms",
            "side": "Side by side",
            "stacked": "Stacked",
            "layout_label": "Layout",
            "src": "Source",
            "out": "Result",
            "local": "Conversion runs locally",
            "chips": [
                "One file",
                "UTF-8",
                "Up to 10 MiB"
            ]
        },
        "film_title": "See OpenCCman 2.0 in action.",
        "film_lead": "Choose a preset, compare source and result, and work with TXT documents on iPhone, iPad and Mac. OpenCCman 2.0 is available on the App Store.",
        "film_note": "Product video · 25 seconds · with music",
        "film_load": "Loads only after you press play · about 3 MB",
        "film_play": "Play the product video",
        "film_download": "Download the video",
        "guides_title": "Start with the task in front of you.",
        "guides_body": "Learn to choose a preset, convert a TXT document, and use Mac selection shortcuts. Each guide includes the limits that matter.",
        "guides_link": "Explore the guides",
        "closing_title": "Keep your focus on the words.",
        "closing_break": "",
        "closing_body": "Get OpenCCman for your next Chinese conversion."
    }
}

CHANGELOG = {
    "zh-Hans": {
        "title": "更新记录",
        "description": "OpenCCman iPhone、iPad 和 Mac 版本的更新内容、兼容范围与文件限制。",
        "intro": "这里记录用户能感知的变化及系统、文件格式限制。完整的工程变更保留在应用仓库。",
        "releases": [
            {
                "id": "version-21",
                "version": "2.1",
                "date": "2026 年 10 月 1 日发布",
                "note": "适用于 iOS/iPadOS 15 及以上、macOS 12 及以上。iPhone/iPad 文件上限仍为 10 MiB；1 GiB 直接文件转换仅限 Mac Pro，不支持批量转换。<a href=\"https://github.com/gewill/OpenCCman/releases/tag/v2.1\">查看 2.1 发布说明</a>。",
                "groups": [
                    [
                        "新增",
                        [
                            "Mac Pro 可将单个大于 10 MiB、最多 1 GiB 的 UTF-8 TXT 文件直接转换并导出到文件，不占用当前编辑区的原文和结果。任务显示进度并可取消；不超过 10 MiB 的文件继续使用可编辑的导入流程。",
                            "新增免费「转换文字」快捷指令动作，可选择四个公开预设，并将结果交给下一个动作。适用于 iOS/iPadOS 16 及以上、macOS 13 及以上；UTF-8 输入上限 10 MiB，不计入主页每日次数。",
                            "新工作区默认留空，可自行填入示例。清空原文前会确认，同时清除当前窗口的原文、结果、导出快照和导入文件名。",
                            "更新应用图标与启动标识，支持系统提供的深色、透明和着色图标外观；开启「减少动态效果」时使用短暂淡入，VoiceOver 启用时跳过过渡。"
                        ]
                    ],
                    [
                        "修复",
                        [
                            "Mac 全局「转换」快捷键在自动粘贴前，会核对焦点窗口、选中文字及可编辑目标是否仍与任务开始时一致。无法确认目标时，结果保留在 OpenCCman 中供手动复制。"
                        ]
                    ]
                ]
            },
            {
                "id": "version-20",
                "version": "2.0",
                "date": "2026 年 9 月 28 日发布",
                "groups": [
                    [
                        "新增",
                        [
                            "四个常用预设覆盖简体、OpenCC 繁体、台湾正体加词组及香港繁体；高级组合仍可使用。",
                            "Mac 和 iPad 的原文、结果可左右或上下排列。布局偏好按窗口保存；窗口变窄时暂时改为上下排列，不覆盖原偏好。iPhone 使用紧凑的上下工作区。",
                            "可导入或拖入单个不超过 10 MiB 的 UTF-8 TXT 文件（含 BOM），并将最近一次成功结果导出为不带 BOM 的 UTF-8。正文在本机处理，保留换行、空行、Emoji、组合字符和 U+0000。",
                            "Mac 全局快捷键与系统服务可处理其他应用中选中的文字。自动替换需要辅助功能权限及来源应用支持编辑；也可在 OpenCCman 中查看转换结果。",
                            "设置中加入用户中心，可查看购买状态、恢复购买及联系支持。macOS 13 及以上还可选择登录时启动。"
                        ]
                    ],
                    [
                        "变更",
                        [
                            "内置 OpenCC 核心从 1.2.0 升至 1.4.2。旧选项含义保留，但词典更新可能使个别转换结果改变。",
                            "主页仍每天提供 12 次免费转换。跨窗口开始任务时先预约次数；失败或取消会释放。Pro 转换不受此限制。",
                            "最低系统版本为 iOS 15 和 macOS 12；也支持 iPad。"
                        ]
                    ],
                    [
                        "修复",
                        [
                            "取消后，旧转换或文件导入不会把结果写回新稿。超限或编码无效的导入不会覆盖当前原文。",
                            "大段文字转换不再因分块边界改变词组或丢失此前的正文。",
                            "Mac 剪贴板流程保留原有数据表示，也不会覆盖用户后来复制的新内容。"
                        ]
                    ]
                ]
            }
        ],
        "history": {
            "id": "history",
            "title": "早期源码记录",
            "range": "1.0–1.2",
            "items": [
                "1.2：更新依赖；当时的大段文字分块转换后来由 2.0 的修复替代。",
                "1.1：加入 macOS 系统服务和可配置的全局选中文字快捷键。",
                "1.0：首次提供 iPhone、iPad 和 Mac 简繁及地区用语转换。"
            ],
            "link": "<a href=\"https://github.com/gewill/OpenCCman/blob/main/CHANGELOG.md\">查看完整应用 Changelog</a>"
        }
    },
    "zh-Hant": {
        "title": "更新紀錄",
        "description": "OpenCCman iPhone、iPad 與 Mac 版本的更新內容、相容範圍及檔案限制。",
        "intro": "這裡記錄使用者能察覺的變更，以及系統與檔案格式限制。完整工程變更保留在 App 儲存庫。",
        "releases": [
            {
                "id": "version-21",
                "version": "2.1",
                "date": "2026 年 10 月 1 日推出",
                "note": "適用於 iOS/iPadOS 15 以上、macOS 12 以上。iPhone/iPad 檔案上限仍為 10 MiB；1 GiB 直接檔案轉換僅限 Mac Pro，不支援批次轉換。<a href=\"https://github.com/gewill/OpenCCman/releases/tag/v2.1\">檢視 2.1 發布說明</a>。",
                "groups": [
                    [
                        "新增",
                        [
                            "Mac Pro 可將單一大於 10 MiB、最多 1 GiB 的 UTF-8 TXT 檔案直接轉換並匯出成檔案，不動目前編輯區的原文與結果。工作會顯示進度，也能取消；不超過 10 MiB 的檔案仍使用可編輯的匯入流程。",
                            "新增免費的「轉換文字」捷徑動作，可選擇四個公開預設，並將結果傳給下一個動作。適用於 iOS/iPadOS 16 以上、macOS 13 以上；UTF-8 輸入上限 10 MiB，不計入首頁每日次數。",
                            "新工作區預設為空，可自行填入範例。清除原文前會確認，同時移除目前視窗的原文、結果、匯出快照及匯入檔名。",
                            "更新 App 圖示與啟動標誌，支援系統提供的深色、透明及著色圖示外觀；開啟「減少動態效果」時改用短暫淡入，啟用 VoiceOver 時跳過轉場。"
                        ]
                    ],
                    [
                        "修正",
                        [
                            "Mac 全域「轉換」快速鍵在自動貼上前，會核對焦點視窗、所選文字及可編輯目標是否與工作開始時一致。若無法確認，結果會留在 OpenCCman 供手動複製。"
                        ]
                    ]
                ]
            },
            {
                "id": "version-20",
                "version": "2.0",
                "date": "2026 年 9 月 28 日推出",
                "groups": [
                    [
                        "新增",
                        [
                            "四個常用預設涵蓋簡體、OpenCC 繁體、臺灣正體加詞組及香港繁體；仍可使用進階組合。",
                            "Mac 與 iPad 可將原文和結果左右或上下排列。版面偏好按視窗儲存；視窗變窄時暫時上下排列，不覆蓋原偏好。iPhone 使用精簡的上下工作區。",
                            "可匯入或拖入單一不超過 10 MiB 的 UTF-8 TXT 檔案（含 BOM），並將最近一次成功結果匯出為不含 BOM 的 UTF-8。文字在本機處理，保留換行、空白行、Emoji、組合字元和 U+0000。",
                            "Mac 全域快速鍵與系統服務可處理其他 App 中選取的文字。自動取代需要輔助使用權限及來源 App 支援編輯；也可在 OpenCCman 中查看結果。",
                            "設定中加入使用者中心，可查看購買狀態、回復購買及聯絡支援。macOS 13 以上亦可選擇登入時啟動。"
                        ]
                    ],
                    [
                        "變更",
                        [
                            "內建 OpenCC 核心由 1.2.0 升至 1.4.2。舊選項意義維持不變，但詞典更新可能改變個別轉換結果。",
                            "首頁仍每日提供 12 次免費轉換。跨視窗開始工作時先預留次數；失敗或取消會釋放。Pro 轉換不受此限制。",
                            "最低系統版本為 iOS 15 和 macOS 12；亦支援 iPad。"
                        ]
                    ],
                    [
                        "修正",
                        [
                            "取消後，舊轉換或檔案匯入不會將結果寫回新稿。超過上限或編碼無效的匯入不會覆蓋目前原文。",
                            "大段文字轉換不再因分段邊界改變詞組或遺失先前正文。",
                            "Mac 剪貼簿流程保留原有資料表示，也不會覆蓋使用者稍後複製的新內容。"
                        ]
                    ]
                ]
            }
        ],
        "history": {
            "id": "history",
            "title": "早期原始碼紀錄",
            "range": "1.0–1.2",
            "items": [
                "1.2：更新相依套件；當時的大段文字分段轉換後來由 2.0 的修正取代。",
                "1.1：加入 macOS 系統服務及可設定的全域選取文字快速鍵。",
                "1.0：首次提供 iPhone、iPad 與 Mac 簡繁和地區用語轉換。"
            ],
            "link": "<a href=\"https://github.com/gewill/OpenCCman/blob/main/CHANGELOG.md\">檢視完整 App Changelog</a>"
        }
    },
    "en": {
        "title": "Changelog",
        "description": "OpenCCman release notes and compatibility details for iPhone, iPad and Mac.",
        "intro": "Release notes describe changes you can use, along with platform and file-format limits. The full engineering history remains in the app repository.",
        "releases": [
            {
                "id": "version-21",
                "version": "2.1",
                "date": "Published 1 October 2026",
                "note": "Requires iOS/iPadOS 15+ or macOS 12+. iPhone/iPad files remain limited to 10 MiB; direct file conversion up to 1 GiB is Mac Pro only, with no batch conversion. <a href=\"https://github.com/gewill/OpenCCman/releases/tag/v2.1\">Read the 2.1 release notes</a>.",
                "groups": [
                    [
                        "Added",
                        [
                            "On Mac, Pro can convert and export one UTF-8 TXT file larger than 10 MiB, up to 1 GiB, directly to a file. The current draft and result stay in place. The task shows progress and supports cancellation. Files up to 10 MiB keep the editable import workflow.",
                            "A free Shortcuts action converts text with one of four public presets and returns the result to the next action. Available on iOS/iPadOS 16+ and macOS 13+; input is limited to 10 MiB of UTF-8 and does not use the homepage daily allowance.",
                            "New workspaces start empty, with an optional example. Clearing the source asks for confirmation and removes the current window’s source, result, export snapshot and imported filename.",
                            "Updated app icon and launch mark, including system-supported dark, clear and tinted icon appearances. Reduce Motion uses a short fade, and VoiceOver skips it."
                        ]
                    ],
                    [
                        "Fixed",
                        [
                            "The Mac global Convert shortcut checks that the focused window, selection and editable target are still the ones that started the request. If the target cannot be confirmed, the result stays in OpenCCman for manual copying."
                        ]
                    ]
                ]
            },
            {
                "id": "version-20",
                "version": "2.0",
                "date": "Published 28 September 2026",
                "groups": [
                    [
                        "Added",
                        [
                            "Four presets cover Simplified Chinese, OpenCC Traditional, Taiwan Standard with idioms, and Hong Kong Traditional. Advanced combinations remain available.",
                            "Mac and iPad can place source and result side by side or stacked. Layout preference belongs to each window; narrow windows stack temporarily without changing that preference. iPhone keeps a compact stacked workspace.",
                            "Import or drop one UTF-8 TXT file up to 10 MiB, including a UTF-8 BOM; export the latest successful result as UTF-8 without a BOM. File work runs locally and preserves line endings, blank lines, Emoji, combining characters and embedded U+0000.",
                            "Mac global shortcuts and Services work with selected text in other apps. Automatic replacement needs Accessibility permission and an editable source app; conversion can also open the result in OpenCCman.",
                            "A Customer Center in Settings shows purchase status, restore and support. Mac users on macOS 13+ can optionally enable Launch at Login."
                        ]
                    ],
                    [
                        "Changed",
                        [
                            "The embedded OpenCC core moves from 1.2.0 to 1.4.2. Existing option meanings remain; updated dictionaries may change particular conversion results.",
                            "The homepage still offers 12 free conversions per day. Starting work reserves a use across windows; failures and cancellations release it. Pro conversions remain exempt.",
                            "Minimum systems are iOS 15 and macOS 12. The app is also available on iPad."
                        ]
                    ],
                    [
                        "Fixed",
                        [
                            "Cancellation prevents a late conversion or file import from replacing newer text. An oversized or invalid import leaves the current draft intact.",
                            "Large-text conversion now preserves phrase boundaries and earlier text instead of letting chunk boundaries alter words or drop content.",
                            "The Mac pasteboard workflow preserves saved representations and avoids overwriting a newer copy made by the user."
                        ]
                    ]
                ]
            }
        ],
        "history": {
            "id": "history",
            "title": "Earlier source history",
            "range": "1.0–1.2",
            "items": [
                "1.2: dependency updates; its earlier chunked large-text conversion was replaced by the 2.0 correction above.",
                "1.1: macOS Services and configurable global shortcuts for selected text.",
                "1.0: the original iPhone, iPad and Mac Chinese conversion app with regional options."
            ],
            "link": "<a href=\"https://github.com/gewill/OpenCCman/blob/main/CHANGELOG.md\">Full app changelog</a>"
        }
    }
}

SUPPORT = {
    "zh-Hans": {
        "title": "联系支持",
        "intro": "遇到问题，或想提出建议？欢迎直接联系开发者。",
        "email_label": "发送邮件",
        "restore_title": "购买与恢复",
        "restore_body": "如需恢复 Pro，请使用购买时的 Apple 账号，并在应用内选择恢复购买。退款申请由 Apple 处理。",
        "refund_label": "向 Apple 申请退款",
        "details_lead": "为了更快定位问题，请说明：",
        "details": [
            "设备型号",
            "系统版本",
            "应用版本",
            "重现步骤"
        ],
        "warning": "请勿发送密码、验证码或包含敏感信息的原文。",
        "description": "联系 OpenCCman 开发者，反馈问题或建议，恢复 Pro 购买，或向 Apple 申请退款。",
        "email": "531sunlight@gmail.com",
        "refund_url": "https://reportaproblem.apple.com/"
    },
    "zh-Hant": {
        "title": "聯絡支援",
        "intro": "遇到問題，或想提出建議？歡迎直接聯絡開發者。",
        "email_label": "傳送電子郵件",
        "restore_title": "購買與回復",
        "restore_body": "如需回復 Pro，請使用購買時的 Apple 帳號，並在應用程式內選擇回復購買。退款申請由 Apple 處理。",
        "refund_label": "向 Apple 申請退款",
        "details_lead": "為了更快找出問題，請說明：",
        "details": [
            "裝置型號",
            "系統版本",
            "應用程式版本",
            "重現步驟"
        ],
        "warning": "請勿傳送密碼、驗證碼或包含敏感資訊的原文。",
        "description": "聯絡 OpenCCman 開發者，回報問題或建議、回復 Pro 購買，或向 Apple 申請退款。",
        "email": "531sunlight@gmail.com",
        "refund_url": "https://reportaproblem.apple.com/"
    },
    "en": {
        "title": "Support",
        "intro": "Have a question, a problem or an idea? Contact the developer directly.",
        "email_label": "Email support",
        "restore_title": "Purchases & restoration",
        "restore_body": "To restore Pro, use the Apple account used for the purchase and choose Restore Purchases in the app. Refund requests are handled by Apple.",
        "refund_label": "Request a refund from Apple",
        "details_lead": "Please include:",
        "details": [
            "Device model",
            "Operating system",
            "App version",
            "Steps to reproduce the issue"
        ],
        "warning": "Do not send passwords, verification codes or sensitive source text.",
        "description": "Contact the OpenCCman developer, restore a Pro purchase, or request a refund from Apple.",
        "email": "531sunlight@gmail.com",
        "refund_url": "https://reportaproblem.apple.com/"
    }
}

# The glosses are margin headings; each paragraph is the approved policy text.
PRIVACY = {
    "zh-Hans": {
        "title": "隐私政策",
        "description": "OpenCCman 如何处理您输入的文字、购买信息和支持邮件。",
        "updated": "更新日期：2026 年 9 月 19 日",
        "sections": [
            [
                "本机转换",
                "OpenCCman 使用 OpenCC 在设备上转换文本。应用不会将您输入、导入或转换的正文发送到转换服务器。偏好设置和每日转换额度保存在本地。打开与导出文件通过系统文件选择器及您选择的存储位置处理。"
            ],
            [
                "购买与 RevenueCat",
                "购买功能使用 Apple App 内购买和 RevenueCat 验证购买、恢复权益及管理 Pro 权限。RevenueCat 处理购买记录和应用用户标识；当前应用使用 RevenueCat 的匿名标识，无需创建 OpenCCman 账号。发往 RevenueCat 的请求还包含购买服务所需的技术信息：设备型号、操作系统与应用版本、语言、App Store 国家或地区，以及 iPhone 和 iPad 上的供应商标识符（IDFV）。RevenueCat 可能根据请求的 IP 地址估计您所在的国家或地区；据 RevenueCat 说明，估计完成后不会保存该 IP 地址。购买信息也用于购买分析。详见 <a href=\"https://www.revenuecat.com/privacy\">RevenueCat 隐私政策</a>。"
            ],
            [
                "用户中心",
                "在 iPhone 和 iPad 上，设置中的「用户中心」由 RevenueCat 提供。每次打开时，RevenueCat 会记录一次使用事件，包含匿名标识、时间、语言及显示设置，用于使用统计。"
            ],
            [
                "销售通知",
                "RevenueCat 还会向开发者的 Slack 工作区发送购买事件通知，用于了解销售情况。通知可能包含应用匿名用户标识、商品及金额信息，仅由开发者本人查看。我们不将这些标识与姓名、邮箱或广告数据关联。通知按 Slack 工作区的数据保留设置保存。"
            ],
            [
                "权限、链接与邮件",
                "在 Mac 上，全局快捷键使用辅助功能权限和剪贴板复制或替换其他应用中选中的文本；您可在系统设置中管理权限。打开支持、隐私政策或应用推荐链接会访问外部服务。若您通过电子邮件联系支持，开发者会收到您的邮箱地址、邮件内容（草稿包含应用名称和版本）及您主动提供的信息。支持邮件仅由开发者本人查看，只用于答复您的问题，保存在开发者的邮箱中，没有固定的删除期限。"
            ],
            [
                "联系方式",
                "隐私问题请联系：531sunlight@gmail.com。"
            ]
        ],
        "back": "返回首页"
    },
    "zh-Hant": {
        "title": "隱私權政策",
        "description": "OpenCCman 如何處理您輸入的文字、購買資訊和支援郵件。",
        "updated": "更新日期：2026 年 9 月 19 日",
        "sections": [
            [
                "本機轉換",
                "OpenCCman 使用 OpenCC 在裝置上轉換文字。應用程式不會將您輸入、匯入或轉換的正文傳送至轉換伺服器。偏好設定和每日轉換額度儲存在本機。開啟與匯出檔案透過系統檔案選擇器及您選擇的儲存位置處理。"
            ],
            [
                "購買與 RevenueCat",
                "購買功能使用 Apple App 內購買和 RevenueCat 驗證購買、回復權益及管理 Pro 權限。RevenueCat 處理購買記錄和應用程式使用者識別碼；目前應用程式使用 RevenueCat 的匿名識別碼，無需建立 OpenCCman 帳號。傳送至 RevenueCat 的請求還包含購買服務所需的技術資訊：裝置型號、作業系統與應用程式版本、語言、App Store 國家或地區，以及 iPhone 和 iPad 上的廠商識別碼（IDFV）。RevenueCat 可能依據請求的 IP 位址估計您所在的國家或地區；據 RevenueCat 說明，估計完成後不會保存該 IP 位址。購買資訊也用於購買分析。詳見 <a href=\"https://www.revenuecat.com/privacy\">RevenueCat 隱私政策</a>。"
            ],
            [
                "使用者中心",
                "在 iPhone 和 iPad 上，設定中的「使用者中心」由 RevenueCat 提供。每次開啟時，RevenueCat 會記錄一次使用事件，包含匿名識別碼、時間、語言及顯示設定，用於使用統計。"
            ],
            [
                "銷售通知",
                "RevenueCat 也會向開發者的 Slack 工作區傳送購買事件通知，用於了解銷售情況。通知可能包含應用程式匿名使用者識別碼、商品及金額資訊，僅由開發者本人查看。我們不將這些識別碼與姓名、電子郵件地址或廣告資料關聯。通知依 Slack 工作區的資料保留設定儲存。"
            ],
            [
                "權限、連結與郵件",
                "在 Mac 上，全域快速鍵使用輔助使用權限和剪貼板複製或替換其他應用程式中選取的文字；您可在系統設定中管理權限。開啟支援、隱私政策或應用程式推薦連結會存取外部服務。若您透過電子郵件聯絡支援，開發者會收到您的電子郵件地址、郵件內容（草稿包含應用程式名稱和版本）及您主動提供的資訊。支援郵件僅由開發者本人查看，只用於回覆您的問題，保存在開發者的信箱中，沒有固定的刪除期限。"
            ],
            [
                "聯絡方式",
                "隱私問題請聯絡：531sunlight@gmail.com。"
            ]
        ],
        "back": "返回首頁"
    },
    "en": {
        "title": "Privacy policy",
        "description": "How OpenCCman handles the text you convert, purchase information and support email.",
        "updated": "Updated September 19, 2026",
        "sections": [
            [
                "On-device conversion",
                "OpenCCman converts text on your device using OpenCC. The app does not send the text you enter, import or convert to a conversion server. Preferences and daily conversion allowances are stored locally. Files you open or export are handled through the system file picker and the storage location you choose."
            ],
            [
                "Purchases and RevenueCat",
                "Purchases use Apple’s in-app purchase system and RevenueCat to validate purchases, restore access and manage Pro entitlements. RevenueCat processes purchase records and an app user identifier; the current app uses RevenueCat’s anonymous identifier rather than asking you to create an OpenCCman account. Requests to RevenueCat also include technical information needed by the purchase service: device model, operating system and app version, language, App Store country or region and, on iPhone and iPad, the identifier for vendor (IDFV). RevenueCat may estimate your country or region from a request’s IP address; according to RevenueCat, the IP address is not stored after that estimate. Purchase information also supports purchase analytics. See <a href=\"https://www.revenuecat.com/privacy\">RevenueCat’s privacy policy</a>."
            ],
            [
                "Customer Center",
                "On iPhone and iPad, Customer Center in Settings is provided by RevenueCat. Each time you open it, RevenueCat records a usage event with the anonymous identifier, time, language and display settings for usage statistics."
            ],
            [
                "Sales notifications",
                "RevenueCat also sends purchase-event notifications to the developer’s Slack workspace for sales monitoring. These notifications may include an anonymous app user identifier, product and purchase amount information, and are viewed only by the developer. We do not associate these identifiers with names, email addresses or advertising data. Notifications are retained according to the Slack workspace’s data retention settings."
            ],
            [
                "Permissions, links and email",
                "On Mac, global shortcuts use Accessibility permission and the clipboard to copy or replace selected text in other apps. You can manage this permission in System Settings. Opening support, privacy or recommended-app links takes you to external services. If you contact support by email, the developer receives your email address, your message (the draft includes the app name and version) and any information you choose to include. Support emails are read only by the developer, used only to respond to your request, and kept in the developer’s mailbox without a fixed deletion period."
            ],
            [
                "Contact",
                "Privacy questions: 531sunlight@gmail.com."
            ]
        ],
        "back": "Back to home"
    }
}

NOT_FOUND = {
    "title": "Page not found — OpenCCman",
    "heading": "Page not found",
    "lines": [
        [
            "zh-Hans",
            "找不到这一页。"
        ],
        [
            "zh-Hant",
            "找不到這一頁。"
        ]
    ],
    "links": [
        [
            "zh-Hans",
            "/zh-Hans/",
            "简体中文首页"
        ],
        [
            "zh-Hant",
            "/zh-Hant/",
            "繁體中文首頁"
        ],
        [
            "en",
            "/en/",
            "OpenCCman — Home"
        ]
    ]
}

ROOT = {
    "title": "OpenCCman",
    "prompt": "Choose your language"
}
