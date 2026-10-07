// Kiegészítő GA4 eseménykövetés a Material alap page-view méréséhez.
// Minden link-kattintást (belső/külső), a szerkesztés-gombot, és az olvasási
// mélységet (scroll depth) is eseményként küldi a gtag-nek.
(function () {
  function send(name, params) {
    if (typeof gtag === "function") {
      gtag("event", name, params || {});
    }
  }

  function initClickTracking() {
    document.addEventListener("click", function (e) {
      var link = e.target.closest("a");
      if (!link || !link.href) return;

      var isExternal = link.hostname && link.hostname !== window.location.hostname;
      var isEdit = link.classList && link.classList.contains("md-content__button");

      send(isEdit ? "edit_click" : isExternal ? "outbound_click" : "internal_link_click", {
        link_url: link.href,
        link_text: (link.textContent || "").trim().slice(0, 100),
        page_path: window.location.pathname,
      });
    });
  }

  function initScrollTracking() {
    var thresholds = [25, 50, 75, 90, 100];
    var fired = {};

    function onScroll() {
      var doc = document.documentElement;
      var scrollTop = window.scrollY || doc.scrollTop;
      var height = doc.scrollHeight - doc.clientHeight;
      if (height <= 0) return;

      var percent = Math.round((scrollTop / height) * 100);

      thresholds.forEach(function (t) {
        if (percent >= t && !fired[t]) {
          fired[t] = true;
          send("scroll_depth", {
            percent: t,
            page_path: window.location.pathname,
          });
        }
      });
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  function initReadingTime() {
    var start = Date.now();
    var sent = false;

    function sendReadingTime() {
      if (sent) return;
      sent = true;
      var seconds = Math.round((Date.now() - start) / 1000);
      send("reading_time", {
        seconds: seconds,
        page_path: window.location.pathname,
      });
    }

    window.addEventListener("beforeunload", sendReadingTime);
    document.addEventListener("visibilitychange", function () {
      if (document.visibilityState === "hidden") sendReadingTime();
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initClickTracking();
    initScrollTracking();
    initReadingTime();
  });
})();
