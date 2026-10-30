/* Flex.Work interactive tools. Each tool initialises when its container is on the page. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var num = function (el) { var v = parseFloat((el && el.value) || "0"); return isFinite(v) ? v : 0; };
  var money = function (v, cur) { return (cur || "$") + Math.round(v).toLocaleString(); };
  var qs = new URLSearchParams(location.search);
  function copyText(t, btn) {
    var done = function () { if (btn) { var o = btn.textContent; btn.textContent = "Copied"; setTimeout(function () { btn.textContent = o; }, 1600); } };
    if (navigator.clipboard) navigator.clipboard.writeText(t).then(done, function () {}); else {
      var ta = document.createElement("textarea"); ta.value = t; document.body.appendChild(ta); ta.select();
      try { document.execCommand("copy"); done(); } catch (e) {} document.body.removeChild(ta);
    }
  }
  function download(name, text) {
    var a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([text], { type: "text/plain" }));
    a.download = name; document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }

  /* ---------- Role explorer ---------- */
  var ex = $("#explorer");
  if (ex && window.FW_ROLES) {
    var names = { r: "Remote", h: "Hybrid", p: "Part-time", f: "Freelance", d: "4-day / compressed", a: "Async-first" };
    var q = $("#ex-q"), cat = $("#ex-cat"), arr = $("#ex-arr"), min = $("#ex-min"), out = $("#ex-out"), cnt = $("#ex-count");
    var cats = Array.from(new Set(window.FW_ROLES.map(function (r) { return r.c; }))).sort();
    cats.forEach(function (c) { var o = document.createElement("option"); o.value = c; o.textContent = c; cat.appendChild(o); });
    if (qs.get("q")) q.value = qs.get("q");
    if (qs.get("t") && names[qs.get("t")]) arr.value = qs.get("t");
    function render() {
      var term = q.value.trim().toLowerCase(), c = cat.value, a = arr.value, m = parseInt(min.value, 10) || 1;
      var list = window.FW_ROLES.filter(function (r) {
        var hay = (r.t + " " + r.d + " " + r.s.join(" ") + " " + r.c).toLowerCase();
        return (!term || hay.indexOf(term) > -1) && (!c || r.c === c) && (!a || r.arr.indexOf(a) > -1) && r.flex >= m;
      }).sort(function (x, y) { return y.flex - x.flex || x.t.localeCompare(y.t); });
      cnt.textContent = list.length + " role" + (list.length === 1 ? "" : "s");
      if (!list.length) {
        out.innerHTML = '<div class="empty"><h3>No roles match those filters</h3><p>Loosen a filter, or tell us what you want and we&rsquo;ll match you when a role opens.</p><a class="btn" href="talent.html">Get matched</a></div>';
        return;
      }
      out.innerHTML = list.map(function (r) {
        var bar = ""; for (var i = 1; i <= 5; i++) bar += '<i class="' + (i <= r.flex ? "on" : "") + '"></i>';
        var tags = r.arr.split("").map(function (k) { return '<span class="tag">' + names[k] + "</span>"; }).join("");
        return '<article class="role"><h3>' + r.t + '</h3><div class="small muted">' + r.c + " &middot; " + r.lvl +
          '</div><div class="flexbar" role="img" aria-label="Flexibility ' + r.flex + ' of 5">' + bar + "</div><p>" + r.d +
          '</p><div class="mb0">' + tags + '</div><p class="small muted mt4 mb0">Core skills: ' + r.s.join(", ") + "</p></article>";
      }).join("");
    }
    [q, cat, arr, min].forEach(function (el) { el.addEventListener("input", render); });
    render();
  }

  /* ---------- Flex readiness quiz ---------- */
  var qz = $("#quiz");
  if (qz) {
    qz.addEventListener("submit", function (e) {
      e.preventDefault();
      var total = 0, n = 0, dims = {};
      $$("fieldset[data-dim]", qz).forEach(function (fs) {
        var v = fs.querySelector("input:checked"); if (!v) return;
        var d = fs.getAttribute("data-dim"); dims[d] = (dims[d] || 0) + parseInt(v.value, 10); total += parseInt(v.value, 10); n++;
      });
      var need = $$("fieldset[data-dim]", qz).length;
      if (n < need) { $("#quiz-msg").textContent = "Answer all " + need + " questions to see your result (" + (need - n) + " left)."; return; }
      $("#quiz-msg").textContent = "";
      var pct = Math.round(total / (need * 3) * 100);
      var band = pct >= 80 ? ["Fully remote ready", "You already have the habits most remote teams hire for. Target remote-first and async-first employers, and say so explicitly in applications."]
        : pct >= 60 ? ["Hybrid sweet spot", "You would thrive with two or three home days and a predictable anchor day. Strengthen the lowest dimension below before going fully remote."]
        : pct >= 40 ? ["Flex-curious", "Start with a trial arrangement — one home day or a compressed fortnight — and build routines before asking for more."]
        : ["Structure first", "You currently draw energy from in-person structure. Part-time, shift-choice or compressed weeks may suit you better than remote work."];
      $("#quiz-score").textContent = pct + "%";
      $("#quiz-band").textContent = band[0];
      $("#quiz-text").textContent = band[1];
      $(".meter i", $("#quiz-result")).style.width = pct + "%";
      var lbl = { focus: "Focus and self-direction", comms: "Written communication", setup: "Home setup", social: "Social energy", routine: "Routine and boundaries" };
      $("#quiz-dims").innerHTML = Object.keys(dims).map(function (k) {
        var max = $$('fieldset[data-dim="' + k + '"]', qz).length * 3;
        return "<dt>" + lbl[k] + "</dt><dd>" + Math.round(dims[k] / max * 100) + "%</dd>";
      }).join("");
      $("#quiz-result").hidden = false;
      $("#quiz-result").scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  /* ---------- Commute savings ---------- */
  var cm = $("#commute");
  if (cm) {
    var f = function (id) { return $("#" + id, cm); };
    if (qs.get("m")) f("cm-min").value = qs.get("m");
    function calcC() {
      var mins = num(f("cm-min")) * 2, days = num(f("cm-days")), weeks = num(f("cm-weeks")),
          km = num(f("cm-km")) * 2, cpk = num(f("cm-cpk")), other = num(f("cm-other")), wage = num(f("cm-wage")), mode = f("cm-mode").value;
      var ef = { car: 0.17, transit: 0.04, motorbike: 0.11, ev: 0.05, bike: 0 }[mode];
      var trips = days * weeks;
      var hours = mins * trips / 60, cost = (km * cpk + other) * trips, co2 = km * trips * ef, value = hours * wage;
      $("#cm-hours").textContent = Math.round(hours).toLocaleString() + " h";
      $("#cm-cost").textContent = money(cost);
      $("#cm-co2").textContent = Math.round(co2).toLocaleString() + " kg";
      $("#cm-value").textContent = money(value);
      $("#cm-days-back").textContent = (hours / 8).toFixed(1);
      $("#cm-total").textContent = money(cost + value);
    }
    $$("input,select", cm).forEach(function (el) { el.addEventListener("input", calcC); });
    calcC();
  }

  /* ---------- Freelance rate ---------- */
  var rt = $("#rate");
  if (rt) {
    var g = function (id) { return num($("#" + id, rt)); };
    function calcR() {
      var income = g("rt-income"), exp = g("rt-exp"), taxPct = g("rt-tax") / 100, weeksOff = g("rt-off"),
          hrs = g("rt-hours"), bill = g("rt-bill") / 100, profit = g("rt-profit") / 100;
      var gross = (income + exp) / Math.max(0.01, 1 - taxPct);
      gross = gross * (1 + profit);
      var billable = Math.max(1, (52 - weeksOff) * hrs * bill);
      var hourly = gross / billable;
      $("#rt-hourly").textContent = money(hourly);
      $("#rt-day").textContent = money(hourly * hrs / 5 * bill > 0 ? hourly * 8 : 0);
      $("#rt-gross").textContent = money(gross);
      $("#rt-billable").textContent = Math.round(billable).toLocaleString() + " h";
      $("#rt-month").textContent = money(gross / 12);
      $("#rt-proj").textContent = money(hourly * 40);
    }
    $$("input", rt).forEach(function (el) { el.addEventListener("input", calcR); });
    calcR();
  }

  /* ---------- Four-day week ---------- */
  var fd = $("#fourday");
  if (fd) {
    var h = function (id) { return $("#" + id, fd); };
    function calcF() {
      var hours = num(h("fd-hours")), salary = num(h("fd-salary")), model = h("fd-model").value, start = h("fd-start").value;
      var weekly = { "100": hours * 0.8, "compressed": hours, "nineeighty": hours, "pro": hours * 0.8 }[model];
      var days = { "100": 4, "compressed": 4, "nineeighty": 4.5, "pro": 4 }[model];
      var pay = { "100": salary, "compressed": salary, "nineeighty": salary, "pro": salary * 0.8 }[model];
      var perDay = weekly / days;
      var desc = {
        "100": "100-80-100: full pay, 80% of hours, 100% of agreed output. The model used in most published four-day-week pilots.",
        "compressed": "Compressed week: same total hours squeezed into four longer days. No pay change, but long days can tire people out.",
        "nineeighty": "9/80 schedule: 80 hours over nine working days, so every other Friday is off.",
        "pro": "Pro-rata four days: one fewer day, with salary and hours reduced proportionally."
      }[model];
      $("#fd-weekly").textContent = weekly.toFixed(1) + " h";
      $("#fd-perday").textContent = perDay.toFixed(1) + " h";
      $("#fd-pay").textContent = money(pay);
      $("#fd-hourly").textContent = money(pay / Math.max(1, weekly * 52)) + "/h";
      $("#fd-daysoff").textContent = Math.round((5 - days) * 52) + " extra days off a year";
      $("#fd-desc").textContent = desc;
      var dayNames = ["Mon", "Tue", "Wed", "Thu", "Fri"], off = parseInt(start, 10);
      $("#fd-week").innerHTML = dayNames.map(function (d, i) {
        var isOff = model === "nineeighty" ? (i === 4) : (i === off);
        var label = isOff ? (model === "nineeighty" ? "Off alt. weeks" : "Off") : perDay.toFixed(1) + " h";
        return '<div class="day" data-state="' + (isOff ? "off" : "office") + '" style="cursor:default;min-height:84px"><span>' + d + '</span><span class="st">' + label + "</span></div>";
      }).join("") + '<div class="day" data-state="off" style="cursor:default;min-height:84px"><span>Sat</span><span class="st">Off</span></div><div class="day" data-state="off" style="cursor:default;min-height:84px"><span>Sun</span><span class="st">Off</span></div>';
    }
    $$("input,select", fd).forEach(function (el) { el.addEventListener("input", calcF); });
    calcF();
  }

  /* ---------- Hybrid schedule planner ---------- */
  var pl = $("#planner");
  if (pl) {
    var days = ["Mon", "Tue", "Wed", "Thu", "Fri"], cycle = ["office", "home", "off"], lab = { office: "Office", home: "Home", off: "Off" };
    var tbody = $("tbody", pl);
    var people = [["You", "ohoho"], ["Teammate 2", "hohoh"], ["Teammate 3", "ohhoh"], ["Teammate 4", "hoohh"]];
    var w = qs.get("w");
    if (w && /^[ohf]{7}$/.test(w)) people[0][1] = w.slice(0, 5).replace(/f/g, "f");
    function rowHTML(name, pat) {
      return "<tr><th><input aria-label=\"Name\" value=\"" + name.replace(/"/g, "") + "\"></th>" + days.map(function (d, i) {
        var c = pat[i] === "h" ? "home" : pat[i] === "f" ? "off" : "office";
        return '<td><button type="button" data-state="' + c + '" aria-label="' + d + ' ' + lab[c] + '">' + lab[c] + "</button></td>";
      }).join("") + '<td><button type="button" class="rm" aria-label="Remove row" style="background:var(--line-2);color:var(--ink)">&times;</button></td></tr>';
    }
    function draw() { tbody.innerHTML = people.map(function (p) { return rowHTML(p[0], p[1]); }).join(""); bind(); summ(); }
    function bind() {
      $$("td button[data-state]", tbody).forEach(function (b) {
        b.onclick = function () { var s = cycle[(cycle.indexOf(b.dataset.state) + 1) % 3]; b.dataset.state = s; b.textContent = lab[s]; summ(); };
      });
      $$(".rm", tbody).forEach(function (b) { b.onclick = function () { b.closest("tr").remove(); summ(); }; });
    }
    function summ() {
      var rows = $$("tr", tbody), n = rows.length, best = -1, bestDay = "", lines = [];
      days.forEach(function (d, i) {
        var inOffice = rows.filter(function (r) { return r.querySelectorAll("td button[data-state]")[i].dataset.state === "office"; }).length;
        if (inOffice > best) { best = inOffice; bestDay = d; }
        lines.push("<dt>" + d + "</dt><dd>" + inOffice + " of " + n + " in office</dd>");
      });
      $("#pl-sum").innerHTML = lines.join("");
      $("#pl-anchor").textContent = n ? bestDay : "—";
      $("#pl-note").textContent = n ? (best === n ? "Everyone overlaps on " + bestDay + " — a natural anchor day for planning and one-to-ones." : "Best overlap is " + bestDay + " with " + best + " of " + n + " people. Agree on one anchor day where everyone is in.") : "Add people to compare schedules.";
    }
    $("#pl-add").addEventListener("click", function () {
      people = $$("tr", tbody).map(function (r) {
        return [$("input", r).value, $$("td button[data-state]", r).map(function (b) { return b.dataset.state[0] === "o" ? "o" : b.dataset.state[0] === "h" ? "h" : "f"; }).join("")];
      });
      people.push(["Teammate " + (people.length + 1), "ohoho"]); draw();
    });
    $("#pl-copy").addEventListener("click", function (e) {
      var t = $$("tr", tbody).map(function (r) {
        return $("input", r).value + ": " + $$("td button[data-state]", r).map(function (b, i) { return days[i] + " " + b.textContent; }).join(", ");
      }).join("\n") + "\nAnchor day: " + $("#pl-anchor").textContent;
      copyText(t, e.target);
    });
    draw();
  }

  /* ---------- Flexible work request letter ---------- */
  var lt = $("#letter");
  if (lt) {
    var v = function (id) { return ($("#" + id, lt).value || "").trim(); };
    function build() {
      var name = v("lt-name") || "[Your name]", mgr = v("lt-mgr") || "[Manager's name]", role = v("lt-role") || "[your role]",
          type = $("#lt-type", lt).value, detail = v("lt-detail") || "[describe the schedule]", start = v("lt-start") || "[start date]",
          trial = $("#lt-trial", lt).value, why = v("lt-why"), cover = v("lt-cover"), tone = $("#lt-tone", lt).value;
      var typeText = {
        hybrid: "a hybrid arrangement", remote: "a fully remote arrangement", compressed: "a compressed working week",
        fourday: "a four-day working week", parttime: "a reduction to part-time hours", flexi: "flexible start and finish times", jobshare: "a job-share arrangement"
      }[type];
      var open = tone === "formal" ? "Dear " + mgr + "," : "Hi " + mgr + ",";
      var body = open + "\n\n" +
        "I would like to request " + typeText + " in my role as " + role + ". Specifically, I am proposing: " + detail + ", starting " + start + ".\n\n" +
        "Why this works for the team\n" +
        (why ? why + "\n" : "") +
        "My priorities and deliverables would stay the same, and I will keep my calendar, status and response times visible so nothing slips.\n\n" +
        "How work will be covered\n" +
        (cover ? cover + "\n" : "I will stay reachable during agreed core hours, attend all key meetings, and hand over anything time-sensitive before any day away.\n") + "\n" +
        (trial !== "none" ? "A trial to test it\nI suggest a " + trial + " trial, with a check-in at the end to review output, responsiveness and any impact on colleagues. If it isn't working, we can adjust or return to my current pattern.\n\n" : "") +
        "I'd welcome the chance to discuss this. Could we find 20 minutes in the next week?\n\n" +
        (tone === "formal" ? "Kind regards,\n" : "Thanks,\n") + name;
      $("#lt-out").textContent = body;
      return body;
    }
    $$("input,select,textarea", lt).forEach(function (el) { el.addEventListener("input", build); });
    $("#lt-copy").addEventListener("click", function (e) { copyText(build(), e.target); });
    $("#lt-dl").addEventListener("click", function () { download("flexible-work-request.txt", build()); });
    $("#lt-print").addEventListener("click", function () { window.print(); });
    build();
  }

  /* ---------- Time-zone overlap ---------- */
  var tz = $("#tz");
  if (tz) {
    var zones = ["America/Los_Angeles", "America/Denver", "America/Chicago", "America/New_York", "America/Toronto", "America/Sao_Paulo", "Europe/London", "Europe/Paris", "Europe/Berlin", "Africa/Lagos", "Africa/Johannesburg", "Europe/Istanbul", "Asia/Dubai", "Asia/Karachi", "Asia/Kolkata", "Asia/Dhaka", "Asia/Bangkok", "Asia/Singapore", "Asia/Manila", "Asia/Shanghai", "Asia/Tokyo", "Australia/Sydney", "Pacific/Auckland"];
    try { var mine = Intl.DateTimeFormat().resolvedOptions().timeZone; if (mine && zones.indexOf(mine) < 0) zones.unshift(mine); } catch (e) {}
    var sels = $$("select.tz-sel", tz);
    sels.forEach(function (s, i) {
      zones.forEach(function (z) { var o = document.createElement("option"); o.value = z; o.textContent = z.replace(/_/g, " "); s.appendChild(o); });
      s.value = [mine || "America/New_York", "Europe/London", "Asia/Kolkata", ""][i] || "";
      if (i === 3) { var o0 = document.createElement("option"); o0.value = ""; o0.textContent = "None"; s.insertBefore(o0, s.firstChild); s.value = ""; }
    });
    function offsetMin(zone) {
      var d = new Date(), fmt = new Intl.DateTimeFormat("en-US", { timeZone: zone, hour12: false, year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit" });
      var p = {}; fmt.formatToParts(d).forEach(function (x) { p[x.type] = x.value; });
      var asUTC = Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour % 24, +p.minute);
      return Math.round((asUTC - d.getTime()) / 60000);
    }
    function drawTZ() {
      var ws = num($("#tz-start", tz)), we = num($("#tz-end", tz));
      var active = sels.map(function (s) { return s.value; }).filter(Boolean);
      var base = active[0];
      var baseOff = offsetMin(base);
      var work = active.map(function (z) {
        var diff = (offsetMin(z) - baseOff) / 60, arr = [];
        for (var hh = 0; hh < 24; hh++) { var local = ((hh + diff) % 24 + 24) % 24; arr.push({ local: local, on: local >= ws && local < we, edge: local >= ws - 1 && local < we + 1 }); }
        return { z: z, cells: arr };
      });
      var overlap = []; for (var hh = 0; hh < 24; hh++) overlap.push(work.every(function (w) { return w.cells[hh].on; }));
      var html = "";
      work.forEach(function (w) {
        html += '<div class="tz-row"><b title="' + w.z + '">' + w.z.split("/").pop().replace(/_/g, " ") + "</b>" + w.cells.map(function (c, i) {
          var cls = c.on ? "work" : c.edge ? "edge" : ""; if (overlap[i]) cls += " overlap";
          var lh = Math.floor(c.local), lm = Math.round((c.local - lh) * 60);
          return '<div class="tz-cell ' + cls + '" title="' + String(lh).padStart(2, "0") + ":" + String(lm).padStart(2, "0") + '">' + lh + "</div>";
        }).join("") + "</div>";
      });
      $("#tz-grid", tz).innerHTML = html;
      var hrs = overlap.filter(Boolean).length;
      var first = overlap.indexOf(true);
      $("#tz-hours").textContent = hrs + " h";
      $("#tz-msg").textContent = hrs === 0 ? "No shared working hours. Use async handoffs, or ask one location to shift by an hour or two (edge hours shown lighter)." :
        "Everyone overlaps for " + hrs + " hour" + (hrs > 1 ? "s" : "") + ", starting " + first + ":00 in " + base.split("/").pop().replace(/_/g, " ") + " time. Protect it for live meetings; move everything else to async.";
    }
    $$("select,input", tz).forEach(function (el) { el.addEventListener("input", drawTZ); });
    drawTZ();
  }

  /* ---------- Flex policy builder ---------- */
  var pb = $("#policy");
  if (pb) {
    var pv = function (id) { var el = $("#" + id, pb); return el ? (el.value || "").trim() : ""; };
    var checked = function (name) { return $$('input[name="' + name + '"]:checked', pb).map(function (x) { return x.value; }); };
    function buildP() {
      var org = pv("pb-org") || "[Company]", eff = pv("pb-date") || "[effective date]", model = $("#pb-model", pb).value,
          anchor = pv("pb-anchor"), core = pv("pb-core") || "10:00–15:00", types = checked("pb-types"), equip = $("#pb-equip", pb).value,
          stipend = pv("pb-stipend"), review = $("#pb-review", pb).value, loc = $("#pb-loc", pb).value;
      var modelText = {
        remote: "Remote-first: employees may work from any approved location by default. Offices are optional collaboration spaces.",
        hybrid: "Structured hybrid: employees work on-site on agreed anchor days and choose their location on other days.",
        flexible: "Team-led flexibility: each team agrees its own pattern, documented in a team working agreement.",
        office: "Office-based with flexibility: on-site by default, with the flexible options below available on request."
      }[model];
      var t = org + " — Flexible Work Policy\nEffective: " + eff + "\n\n" +
        "1. Purpose\nThis policy explains how employees at " + org + " can work flexibly while meeting the needs of customers, colleagues and the business.\n\n" +
        "2. Scope\nIt applies to all employees after their onboarding period, unless their role requires a fixed site or schedule (listed by department in Appendix A).\n\n" +
        "3. Our working model\n" + modelText + (anchor ? "\nAnchor days: " + anchor + "." : "") + "\n\n" +
        "4. Arrangements available\n" + (types.length ? types.map(function (x) { return "• " + x; }).join("\n") : "• [Select arrangements]") + "\n\n" +
        "5. Core hours and availability\nEmployees are expected to be reachable between " + core + " in their team's primary time zone, and to keep calendars and status up to date.\n\n" +
        "6. Requesting an arrangement\nEmployees submit a written request to their manager describing the arrangement, start date and how work will be covered. Managers respond in writing within 14 days. A declined request must include the business reason and any alternative offered.\n\n" +
        "7. Trial periods and review\nNew arrangements start with a " + review + " trial, followed by a review of output, responsiveness and team impact.\n\n" +
        "8. Location\n" + { country: "Employees must work from within the country of their employment contract. Working abroad requires prior written approval for tax, payroll and immigration reasons.", region: "Employees must work within the state or province of their contract unless approved in writing.", anywhere: "Employees may work from any location approved by People Operations, subject to tax, payroll and legal checks." }[loc] + "\n\n" +
        "9. Equipment and expenses\n" + { provided: "The company provides a laptop and essential equipment.", stipend: "The company provides a laptop and a home-office stipend" + (stipend ? " of " + stipend : "") + ".", byod: "Employees use their own equipment in line with the security policy; a monthly allowance may apply." }[equip] + " Employees are responsible for a safe, ergonomic and secure workspace.\n\n" +
        "10. Security and confidentiality\nUse company-approved devices and networks, lock screens, and never discuss confidential matters in public spaces.\n\n" +
        "11. Wellbeing and fairness\nFlexible workers have equal access to development, promotion and recognition. Managers judge performance on outcomes, not visibility. Employees are encouraged to keep clear start and finish times.\n\n" +
        "12. Changes\n" + org + " may revise this policy with reasonable notice. Individual arrangements may be changed by mutual agreement or with [notice period] notice for business reasons.\n\n" +
        "This template is general information, not legal advice. Check local employment law before adopting it.";
      $("#pb-out").textContent = t; return t;
    }
    $$("input,select,textarea", pb).forEach(function (el) { el.addEventListener("input", buildP); el.addEventListener("change", buildP); });
    $("#pb-copy").addEventListener("click", function (e) { copyText(buildP(), e.target); });
    $("#pb-dl").addEventListener("click", function () { download("flexible-work-policy.txt", buildP()); });
    buildP();
  }
})();
