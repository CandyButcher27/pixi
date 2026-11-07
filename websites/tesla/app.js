(() => {
  const header = document.getElementById("siteHeader");
  const heroSection = document.querySelector(".hero");

  if (header && heroSection && "IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        header.classList.toggle("site-header--solid", !entries[0].isIntersecting);
      },
      { rootMargin: "-72px 0px 0px 0px", threshold: 0 }
    );
    io.observe(heroSection);
  }

  const panels = [
    { trigger: document.getElementById("vehiclesTrigger"), panel: document.getElementById("vehiclesPanel") },
    { trigger: document.getElementById("globeBtn"), panel: document.getElementById("langPanel") },
    { trigger: document.getElementById("accountBtn"), panel: document.getElementById("accountPanel") },
  ].filter((p) => p.trigger && p.panel);

  function closeAllPanels(except) {
    panels.forEach(({ trigger, panel }) => {
      if (panel === except) return;
      panel.hidden = true;
      trigger.setAttribute("aria-expanded", "false");
    });
  }

  panels.forEach(({ trigger, panel }) => {
    trigger.addEventListener("click", (e) => {
      e.stopPropagation();
      const isOpen = !panel.hidden;
      closeAllPanels();
      panel.hidden = isOpen;
      trigger.setAttribute("aria-expanded", String(!isOpen));
    });
  });

  document.addEventListener("click", (e) => {
    const insideHeader = e.target.closest(".site-header");
    if (!insideHeader || e.target.closest(".mega-panel a")) closeAllPanels();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeAllPanels();
  });

  const regionButtons = document.querySelectorAll(".mini-option");
  regionButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      regionButtons.forEach((b) => b.classList.remove("is-active"));
      btn.classList.add("is-active");
    });
  });

  const acctContinue = document.getElementById("acctContinue");
  const acctEmail = document.getElementById("acctEmail");
  const acctNote = document.getElementById("acctNote");
  if (acctContinue && acctEmail && acctNote) {
    acctContinue.addEventListener("click", () => {
      acctNote.textContent = acctEmail.value
        ? "Check your inbox for a sign-in link."
        : "Enter an email to continue.";
    });
  }

  const menuToggle = document.getElementById("menuToggle");
  const mobileMenu = document.getElementById("mobileMenu");
  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener("click", () => {
      const isOpen = mobileMenu.classList.toggle("is-open");
      mobileMenu.hidden = !isOpen;
      menuToggle.setAttribute("aria-expanded", String(isOpen));
    });
    mobileMenu.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        mobileMenu.classList.remove("is-open");
        mobileMenu.hidden = true;
        menuToggle.setAttribute("aria-expanded", "false");
      })
    );
  }

  const track = document.getElementById("heroTrack");
  const dotsWrap = document.getElementById("heroDots");
  const prevBtn = document.getElementById("heroPrev");
  const nextBtn = document.getElementById("heroNext");
  const hero = document.querySelector(".hero");

  if (track && dotsWrap && prevBtn && nextBtn && hero) {
    const slides = Array.from(track.querySelectorAll("[data-slide]"));
    const count = slides.length;
    let index = 0;
    let timer = null;

    slides.forEach((slide, i) => {
      const dot = document.createElement("button");
      dot.type = "button";
      dot.setAttribute("role", "tab");
      dot.setAttribute("aria-label", `Show slide ${i + 1} of ${count}`);
      dot.addEventListener("click", () => goTo(i, true));
      dotsWrap.appendChild(dot);
    });
    const dots = Array.from(dotsWrap.children);

    function render() {
      track.style.transform = `translateX(-${index * (100 / count)}%)`;
      dots.forEach((d, i) => d.setAttribute("aria-selected", String(i === index)));
    }

    function goTo(i, manual) {
      index = (i + count) % count;
      render();
      if (manual) restartTimer();
    }

    function next(manual) {
      goTo(index + 1, manual);
    }

    function prev(manual) {
      goTo(index - 1, manual);
    }

    function startTimer() {
      timer = setInterval(() => next(false), 6000);
    }

    function restartTimer() {
      clearInterval(timer);
      startTimer();
    }

    prevBtn.addEventListener("click", () => prev(true));
    nextBtn.addEventListener("click", () => next(true));
    hero.addEventListener("mouseenter", () => clearInterval(timer));
    hero.addEventListener("mouseleave", startTimer);
    hero.addEventListener("focusin", () => clearInterval(timer));
    hero.addEventListener("focusout", startTimer);

    render();
    startTimer();
  }

  const askForm = document.getElementById("askForm");
  const askInput = document.getElementById("askInput");
  if (askForm && askInput) {
    const originalPlaceholder = askInput.placeholder;
    askForm.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!askInput.value.trim()) return;
      askInput.value = "";
      askInput.placeholder = "Thanks - we'll follow up shortly.";
      setTimeout(() => (askInput.placeholder = originalPlaceholder), 3200);
    });
  }

  const scheduleBtn = document.getElementById("scheduleBtn");
  if (scheduleBtn) {
    const label = scheduleBtn.querySelector("span");
    const original = label.textContent;
    scheduleBtn.addEventListener("click", () => {
      label.textContent = "We'll reach out shortly";
      setTimeout(() => (label.textContent = original), 3200);
    });
  }

  const askScrollTop = document.getElementById("askScrollTop");
  if (askScrollTop) {
    askScrollTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }
})();
