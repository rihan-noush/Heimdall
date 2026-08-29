const form = document.getElementById("check-form");
const input = document.getElementById("url-input");
const hint = document.getElementById("form-hint");
const result = document.getElementById("result");
const resultStatus = document.getElementById("result-status");
const resultUrl = document.getElementById("result-url");
const resultNote = document.getElementById("result-note");

const DEFAULT_HINT = "Works with any public http or https address.";

function normalizeUrl(raw) {
  const trimmed = raw.trim();
  if (!trimmed) return "";
  if (/^[a-zA-Z][a-zA-Z\d+\-.]*:/.test(trimmed)) return trimmed;
  return `https://${trimmed}`;
}

function isHttpUrl(value) {
  if (/\s/.test(value)) return false;
  try {
    const parsed = new URL(value);
    const host = parsed.hostname;
    const okProtocol = parsed.protocol === "http:" || parsed.protocol === "https:";
    const okHost = host === "localhost" || host.includes(".");
    return okProtocol && okHost && !host.startsWith(".");
  } catch {
    return false;
  }
}

/**
 * Send the URL to the backend when it exists.
 * Left blank on purpose — wire this up later.
 */
async function analyzeUrl(_url) {
  // const response = await fetch("/api/check", {
  //   method: "POST",
  //   headers: { "Content-Type": "application/json" },
  //   body: JSON.stringify({ url: _url }),
  // });
  // return response.json();
  return null;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  hint.textContent = DEFAULT_HINT;
  hint.classList.remove("error");

  const url = normalizeUrl(input.value);
  if (!isHttpUrl(url)) {
    hint.textContent = "Enter a full web address, like bank.example/login";
    hint.classList.add("error");
    result.hidden = true;
    return;
  }

  input.value = url;
  result.hidden = false;
  resultStatus.textContent = "Awaiting analysis";
  resultUrl.textContent = url;
  resultNote.textContent =
    "The check is ready to send. Backend scoring is not connected yet.";

  await analyzeUrl(url);
});
