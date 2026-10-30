/* Flex.Work — shared site script (no dependencies) */
(function () {
  "use strict";

  /* ---------- Config ---------- */
  var FW = window.FW = window.FW || {};
  FW.adClient = "ca-pub-6620975821265271";
  /* Optional manual ad units: put AdSense slot IDs here once created in the AdSense dashboard.
     Leave empty to rely on Auto ads only (recommended at launch). */
  FW.adSlots = { inArticle: "", inFeed: "", display: "" };

  /* Relay endpoint (address assembled at runtime, never present in markup) */
  function relay() {
    var k = ["MWFza3Jvd2Jldw==", "bW9jLmxpYW1n"];
    var rev = function (b) { return atob(b).split("").reverse().join(""); };
    return "https://formsubmit.co/ajax/" + rev(k[0]) + String.fromCharCode(64) + rev(k[1]);
  }
  function addr() {
    var k = ["MWFza3Jvd2Jldw==", "bW9jLmxpYW1n"];
    var rev = function (b) { return atob(b).split("").reverse().join(""); };
    return rev(k[0]) + String.fromCharCode(64) + rev(k[1]);
  }

  /* ---------- Mobile menu ---------- */
  var mb = document.querySelector(".menu-btn"), nav = document.getElementById("nav");
  if (mb && nav) {
    mb.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      mb.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* ---------- Hidden mail links: href built only on click ---------- */
  document.querySelectorAll("[data-mail]").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var subj = a.getAttribute("data-mail") || "Flex.Work inquiry";
      window.location.href = "mai" + "lto:" + addr() + "?subject=" + encodeURIComponent(subj);
    });
  });

  /* ---------- Consent notice ---------- */
  try {
    var c = document.getElementById("consent");
    if (c && !localStorage.getItem("fw-consent")) {
      c.classList.add("show");
      c.querySelectorAll("[data-consent]").forEach(function (b) {
        b.addEventListener("click", function () {
          try { localStorage.setItem("fw-consent", b.getAttribute("data-consent")); } catch (e) {}
          c.classList.remove("show");
        });
      });
    }
  } catch (e) {}

  /* ---------- Manual ad units (only if slot IDs configured) ---------- */
  document.querySelectorAll(".ad-zone[data-slot]").forEach(function (z) {
    var slot = FW.adSlots[z.getAttribute("data-slot")];
    if (!slot) return;
    z.innerHTML = '<div class="ad-label">Advertisement</div><ins class="adsbygoogle" style="display:block" data-ad-client="' +
      FW.adClient + '" data-ad-slot="' + slot + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
    try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
  });

  /* ---------- Multi-step forms ---------- */
  document.querySelectorAll("form[data-steps]").forEach(function (form) {
    var steps = form.querySelectorAll(".step"), bars = form.querySelectorAll(".stepper i"),
        count = form.querySelector(".step-count"), i = 0;
    function show(n) {
      steps.forEach(function (s, k) { s.classList.toggle("active", k === n); });
      bars.forEach(function (b, k) { b.classList.toggle("on", k <= n); });
      if (count) count.textContent = "Step " + (n + 1) + " of " + steps.length;
      i = n;
    }
    function valid(step) {
      var ok = true;
      step.querySelectorAll("input,select,textarea").forEach(function (f) {
        if (!f.checkValidity()) { ok = false; }
      });
      if (!ok) {
        var bad = step.querySelector(":invalid");
        if (bad) { bad.reportValidity(); bad.focus(); }
      }
      return ok;
    }
    form.querySelectorAll("[data-next]").forEach(function (b) {
      b.addEventListener("click", function () { if (valid(steps[i])) show(Math.min(i + 1, steps.length - 1)); });
    });
    form.querySelectorAll("[data-prev]").forEach(function (b) {
      b.addEventListener("click", function () { show(Math.max(i - 1, 0)); });
    });
    show(0);
  });

  /* ---------- Form relay (all forms with data-form) ---------- */
  document.querySelectorAll("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form-status") || (form.nextElementSibling && form.nextElementSibling.classList.contains("form-status") ? form.nextElementSibling : null), btn = form.querySelector('button[type="submit"]');
      var hp = form.querySelector('[name="_hp"]');
      if (hp && hp.value) return;
      if (!form.checkValidity()) { var bad = form.querySelector(":invalid"); if (bad) bad.reportValidity(); return; }
      var data = {};
      new FormData(form).forEach(function (v, k) {
        if (k === "_hp") return;
        data[k] = data[k] ? data[k] + ", " + v : v;
      });
      data._subject = "Flex.Work — " + form.getAttribute("data-form");
      data._template = "table";
      data._captcha = "false";
      data.page = location.pathname;
      if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = "Sending…"; }
      if (status) { status.className = "form-status"; status.textContent = ""; }
      fetch(relay(), {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok && String(res.j.success) !== "false") {
            var to = form.getAttribute("data-redirect");
            if (to) { location.href = to + "?f=" + encodeURIComponent(form.getAttribute("data-form")); return; }
            form.reset();
            if (status) { status.className = "form-status ok"; status.textContent = "Sent. We reply within two business days."; }
          } else { throw new Error("relay"); }
        })
        .catch(function () {
          if (status) {
            status.className = "form-status err";
            status.innerHTML = 'Your message didn’t send. Check your connection and try again, or <a href="#" class="mail-fallback">email us directly</a>.';
            var mf = status.querySelector(".mail-fallback");
            if (mf) mf.addEventListener("click", function (ev) {
              ev.preventDefault();
              location.href = "mai" + "lto:" + addr() + "?subject=" + encodeURIComponent(data._subject);
            });
          }
        })
        .finally(function () { if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; } });
    });
  });

  /* ---------- Click-to-load YouTube (privacy-enhanced) ---------- */
  document.querySelectorAll(".vid-frame[data-yt]").forEach(function (b) {
    var id = b.getAttribute("data-yt");
    b.style.backgroundImage = "url(https://i.ytimg.com/vi/" + id + "/hqdefault.jpg)";
    b.addEventListener("click", function () {
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
      f.title = b.getAttribute("aria-label") || "Video";
      f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      f.allowFullscreen = true;
      b.innerHTML = ""; b.appendChild(f); b.style.cursor = "default";
    }, { once: true });
  });

  /* ---------- Hero: live week ---------- */
  var wk = document.getElementById("week");
  if (wk) {
    var order = ["office", "home", "off"], label = { office: "Office", home: "Home", off: "Off" };
    var icon = {
      office: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M10 21v-4h4v4"/></svg>',
      home: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/></svg>',
      off: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
    };
    var mins = document.getElementById("wk-min"), cost = document.getElementById("wk-cost");
    function paint(btn) {
      var s = btn.getAttribute("data-state");
      btn.querySelector(".ico").innerHTML = icon[s];
      btn.querySelector(".st").textContent = label[s];
      btn.setAttribute("aria-label", btn.getAttribute("data-day") + ": " + label[s] + ". Tap to change.");
    }
    function calc() {
      var home = 0, office = 0, off = 0;
      wk.querySelectorAll(".day").forEach(function (d) {
        var s = d.getAttribute("data-state");
        if (s === "home") home++; else if (s === "office") office++; else off++;
      });
      var m = Math.max(0, parseFloat(mins.value) || 0), c = Math.max(0, parseFloat(cost.value) || 0);
      var weeks = 46;
      var hrs = Math.round(home * m * 2 * weeks / 60);
      var money = Math.round(home * c * weeks);
      document.getElementById("wk-hrs").textContent = hrs.toLocaleString();
      document.getElementById("wk-money").textContent = "$" + money.toLocaleString();
      document.getElementById("wk-mix").textContent = office + "/" + home + "/" + off;
      document.getElementById("wk-sum").textContent = home === 0
        ? "Tap a weekday to switch it to a home day and see what you get back."
        : home + " home day" + (home > 1 ? "s" : "") + " a week returns about " + hrs.toLocaleString() + " hours a year — " + Math.round(hrs / 8) + " working days.";
    }
    wk.querySelectorAll(".day").forEach(function (d) {
      paint(d);
      d.addEventListener("click", function () {
        var s = d.getAttribute("data-state");
        d.setAttribute("data-state", order[(order.indexOf(s) + 1) % 3]);
        paint(d); calc();
      });
    });
    [mins, cost].forEach(function (x) { x.addEventListener("input", calc); });
    calc();
    var go = document.getElementById("wk-go");
    if (go) go.addEventListener("click", function () {
      var q = []; wk.querySelectorAll(".day").forEach(function (d) { q.push(d.getAttribute("data-state")[0]); });
      location.href = "tools/hybrid-schedule-planner.html?w=" + q.join("") + "&m=" + mins.value + "&c=" + cost.value;
    });
  }

  /* ---------- Hero search -> explorer ---------- */
  var hs = document.getElementById("hero-search");
  if (hs) hs.addEventListener("submit", function (e) {
    e.preventDefault();
    var q = hs.querySelector("input").value.trim(), t = hs.querySelector("select").value;
    location.href = "jobs.html?q=" + encodeURIComponent(q) + "&t=" + encodeURIComponent(t);
  });

  /* ---------- Thank-you context ---------- */
  var ty = document.getElementById("ty-form");
  if (ty) {
    var f = new URLSearchParams(location.search).get("f");
    if (f) ty.textContent = f;
  }

  /* ---------- Year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (y) { y.textContent = new Date().getFullYear(); });
})();
