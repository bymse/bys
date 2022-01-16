const copyButton = document.getElementById("copy-button");
if (copyButton) {
  copyButton.addEventListener("click", () => {
    const shortUrl = document.getElementById("short-url");
    if (shortUrl) {
      navigator.clipboard.writeText(shortUrl.href);
      copyButton.innerText = "Copied!";
    }
  });
}

const about = document.getElementById("about");
about.addEventListener("click", () => {
  const readme = document.getElementById("readme");
  const hasHide = readme.classList.contains("hide");
  readme.classList.toggle("hide");
  if (hasHide) {
    about.innerHTML = "&#9660; About"
  } else {
    about.innerHTML = "&#9658; About";
  }
});
