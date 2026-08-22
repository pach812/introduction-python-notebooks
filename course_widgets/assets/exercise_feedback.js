function render({ model, el }) {
  const root = document.createElement("section");
  root.className = "ces-feedback-coach";
  root.setAttribute("aria-live", "polite");
  el.appendChild(root);

  function saveHintCount(count) {
    model.set("value", { ...(model.get("value") || {}), hints_shown: count });
    model.save_changes();
  }

  function draw() {
    const value = model.get("value") || {};
    const hints = model.get("hints") || [];
    const checks = model.get("checks") || [];
    const hintsShown = Math.min(value.hints_shown || 0, hints.length);
    const statusName = model.get("status") || "pending";
    const statusIcons = {
      pending: "○",
      review: "↗",
      complete: "✓",
      error: "!",
    };
    root.replaceChildren();
    root.dataset.status = statusName;

    const header = document.createElement("header");
    const eyebrow = document.createElement("span");
    eyebrow.className = "eyebrow";
    eyebrow.textContent = "Retroalimentación";
    const heading = document.createElement("h3");
    heading.textContent = model.get("title");
    header.append(eyebrow, heading);
    root.appendChild(header);

    const status = document.createElement("div");
    status.className = `status ${statusName}`;
    const statusIcon = document.createElement("span");
    statusIcon.className = "status-icon";
    statusIcon.setAttribute("aria-hidden", "true");
    statusIcon.textContent = statusIcons[statusName] || "○";
    const summary = document.createElement("p");
    summary.textContent = model.get("summary");
    status.append(statusIcon, summary);
    root.appendChild(status);

    const error = model.get("error");
    if (error) {
      const errorBox = document.createElement("p");
      errorBox.className = "error";
      errorBox.textContent = error;
      root.appendChild(errorBox);
    }

    if (checks.length) {
      const list = document.createElement("ul");
      list.className = "checks";
      checks.forEach((item) => {
        const row = document.createElement("li");
        row.className = item.passed ? "passed" : "needs-review";
        const marker = document.createElement("span");
        marker.className = "check-marker";
        marker.textContent = item.passed ? "✓" : "→";
        const text = document.createElement("span");
        const label = document.createElement("strong");
        label.textContent = item.label;
        const message = document.createElement("span");
        message.className = "check-message";
        message.textContent = item.message;
        text.append(label, message);
        row.append(marker, text);
        list.appendChild(row);
      });
      root.appendChild(list);
    }

    if (hints.length && statusName !== "complete") {
      const hintSection = document.createElement("aside");
      hintSection.className = "hint-section";
      const hintHeader = document.createElement("div");
      hintHeader.className = "hint-header";
      const hintTitle = document.createElement("strong");
      hintTitle.textContent = "Pistas";
      const hintCount = document.createElement("span");
      hintCount.textContent = `${hintsShown} de ${hints.length}`;
      hintHeader.append(hintTitle, hintCount);
      hintSection.appendChild(hintHeader);

      if (hintsShown) {
        const hintList = document.createElement("ol");
        hintList.className = "hints";
        hints.slice(0, hintsShown).forEach((hintText) => {
          const item = document.createElement("li");
          item.textContent = hintText;
          hintList.appendChild(item);
        });
        hintSection.appendChild(hintList);
      } else {
        const invitation = document.createElement("p");
        invitation.className = "hint-invitation";
        invitation.textContent = "Úsalas de una en una si necesitas otra idea para continuar.";
        hintSection.appendChild(invitation);
      }

      if (hintsShown < hints.length) {
        const hintButton = document.createElement("button");
        hintButton.type = "button";
        hintButton.textContent = hintsShown ? "Mostrar otra pista" : "Mostrar una pista";
        hintButton.addEventListener("click", () => saveHintCount(hintsShown + 1));
        hintSection.appendChild(hintButton);
      }
      root.appendChild(hintSection);
    }
  }

  draw();
  model.on("change", draw);
}

export default { render };
