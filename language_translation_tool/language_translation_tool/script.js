function translateText() {
  const inputText = document.getElementById("inputText").value;
  const sourceLang = document.getElementById("sourceLang").value;
  const targetLang = document.getElementById("targetLang").value;
  const output = document.getElementById("translatedText");

  fetch("https://libretranslate.com/translate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      q: inputText,
      source: sourceLang,
      target: targetLang,
      format: "text"
    })
  })
    .then(res => res.json())
    .then(data => {
      output.innerText = data.translatedText;
    })
    .catch(err => {
      output.innerText = "Translation failed!";
      console.error(err);
    });
}

function copyText() {
  const text = document.getElementById("translatedText").innerText;
  navigator.clipboard.writeText(text).then(() => alert("Copied!"));
}

function speakText() {
  const text = document.getElementById("translatedText").innerText;
  const utterance = new SpeechSynthesisUtterance(text);
  speechSynthesis.speak(utterance);
}