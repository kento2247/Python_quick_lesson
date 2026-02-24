const toggleButton = document.getElementById("theme-toggle");
const updated = document.getElementById("last-updated");

if (toggleButton) {
  toggleButton.addEventListener("click", () => {
    document.body.classList.toggle("dark");
  });
}

if (updated) {
  const now = new Date();
  updated.textContent = `Last updated: ${now.toLocaleString("ja-JP")}`;
}
