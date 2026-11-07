(function () {
  "use strict";

  // ---- mobile nav ----
  var burger = document.getElementById("burgerBtn");
  var menu = document.getElementById("mobileMenu");
  if (burger && menu) {
    burger.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      burger.setAttribute("aria-expanded", String(open));
    });
    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        menu.classList.remove("is-open");
        burger.setAttribute("aria-expanded", "false");
      });
    });
  }

  // ---- model category filter ----
  var filterRow = document.querySelector(".filter-row");
  var cards = document.querySelectorAll(".model-card");
  if (filterRow) {
    filterRow.addEventListener("click", function (e) {
      var btn = e.target.closest(".pill");
      if (!btn) return;

      filterRow.querySelectorAll(".pill").forEach(function (p) {
        p.classList.remove("is-active");
        p.setAttribute("aria-selected", "false");
      });
      btn.classList.add("is-active");
      btn.setAttribute("aria-selected", "true");

      var filter = btn.dataset.filter;
      cards.forEach(function (card) {
        var match = filter === "all" || card.dataset.category.split(" ").indexOf(filter) !== -1;
        card.classList.toggle("is-hidden", !match);
      });
    });
  }

  // ---- code tab switcher ----
  var codeTabs = document.querySelector(".code-tabs");
  if (codeTabs) {
    var panels = document.querySelectorAll(".code-block");
    codeTabs.addEventListener("click", function (e) {
      var tab = e.target.closest(".code-tab");
      if (!tab) return;

      codeTabs.querySelectorAll(".code-tab").forEach(function (t) {
        t.classList.remove("is-active");
      });
      tab.classList.add("is-active");

      panels.forEach(function (panel) {
        panel.classList.toggle("is-hidden", panel.dataset.panel !== tab.dataset.tab);
      });
    });
  }

  // ---- community avatar rail (decorative, abstract flat-color dots) ----
  var track = document.querySelector(".community__track");
  if (track) {
    var tones = ["#ea2804", "#202020", "#f4a8a0", "#575757", "#ff6a3d", "#bbbbbb", "#8d8d8d", "#c01f00"];
    var frag = document.createDocumentFragment();
    for (var loop = 0; loop < 2; loop++) {
      for (var i = 0; i < tones.length * 2; i++) {
        var dot = document.createElement("span");
        dot.className = "avatar-dot";
        dot.style.background = tones[i % tones.length];
        frag.appendChild(dot);
      }
    }
    track.appendChild(frag);
  }
})();
