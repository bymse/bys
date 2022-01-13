const copyButton = document.getElementById('copy-button');
if (copyButton) {
  copyButton.addEventListener('click', () => {
    const shortUrl = document.getElementById('short-url');
    if (shortUrl) {
      navigator.clipboard.writeText(shortUrl.href);
      copyButton.innerText = "Copied!"
    }
  });
}