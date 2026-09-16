const lang = (navigator.language || "en").toLowerCase();
const target = /^(zh-(tw|hk|mo|hant))/.test(lang) ? "zh-Hant" : lang.startsWith("zh") ? "zh-Hans" : "en";
location.replace("/" + target + "/");
