// Header menu (phones/tablets): disclosure button toggles #site-nav. Nav stays visible without JS.
(function () {
  var btn = document.querySelector(".nav-toggle");
  if (!btn) return;
  var header = btn.closest(".site-header");
  function set(open) {
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.setAttribute("aria-label", open ? "Close park menu" : "Open park menu");
    header.classList.toggle("menu-open", open);
  }
  btn.addEventListener("click", function () { set(btn.getAttribute("aria-expanded") !== "true"); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && btn.getAttribute("aria-expanded") === "true") { set(false); btn.focus(); }
  });
  document.addEventListener("click", function (e) { if (!header.contains(e.target)) set(false); });
  header.querySelectorAll("#site-nav a, .nav-cta").forEach(function (a) { a.addEventListener("click", function () { set(false); }); });
  window.matchMedia("(min-width: 1200px)").addEventListener("change", function () { set(false); });
})();
