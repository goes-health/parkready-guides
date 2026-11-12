// Replaces the build-time NWS snapshot with the live NWS forecast when online.
// Uses the public api.weather.gov endpoints (no key). Falls back silently to the snapshot.
(function () {
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  document.querySelectorAll(".forecast[data-forecast-url]").forEach(function (box) {
    var url = box.getAttribute("data-forecast-url");
    var lat = box.getAttribute("data-lat"), lon = box.getAttribute("data-lon");
    if (!url || !window.fetch) return;
    var status = box.querySelector(".forecast-status");
    fetch(url, { headers: { Accept: "application/geo+json" } })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) {
        var periods = (d.properties && d.properties.periods) || [];
        if (!periods.length) return;
        var rows = periods.slice(0, 8).map(function (p) {
          return "<tr><td>" + esc(p.name) + "</td><td>" + esc(p.temperature) + "°" + esc(p.temperatureUnit) + "</td><td>" + esc(p.shortForecast) + "</td><td>" + esc(p.windSpeed) + "</td></tr>";
        }).join("");
        box.querySelector("tbody").innerHTML = rows;
        var t = d.properties.generatedAt || d.properties.updateTime;
        status.textContent = "Live from the National Weather Service" + (t ? " (issued " + new Date(t).toLocaleString() + ")" : "") + ".";
        status.classList.add("live");
      })
      .catch(function () {});
    fetch("https://api.weather.gov/alerts/active?point=" + lat + "," + lon, { headers: { Accept: "application/geo+json" } })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) {
        var html = (d.features || []).map(function (f) {
          return '<div class="wx-alert"><strong>' + esc(f.properties.event) + "</strong> — " + esc(f.properties.headline) + "</div>";
        }).join("");
        box.querySelector(".wx-alerts").innerHTML = html;
      })
      .catch(function () {});
  });
})();
