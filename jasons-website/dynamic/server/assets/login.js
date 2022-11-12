/**
 * Display an error message to the user.
 * @param {string} message The text to display inside the alert.
 */
function alertMessage(message) {
  document.getElementById("alert-container").innerHTML = `
  <div id="login-alert" class="alert alert-danger alert-dismissible mx-2">
    ${message}
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>`;
}

/**
 * Runs when the document is finished loading.
 */
function onDocumentLoad() {
  document.getElementById("login-form").addEventListener("submit", async (event) => {
    // disable default form action
    event.preventDefault();

    // send login POST request
    const resp = await fetch("/login", {
      "method": "POST",
      "cache": "no-cache",
      "redirect": "follow",
      "headers": {
        "Content-Type": "application/json"
      },
      "body": JSON.stringify({
        "username": document.getElementById("username").value,
        "password": document.getElementById("password").value
      })
    });

    // parse + handle JSON response
    const data = await resp.json();
    if ("error" in data) {
      // show login error as alert
      alertMessage(data["error"]);
    } else {
      // navigate to redirected page
      window.location.href = resp.url;
    }

  });
}

if (document.readyState === "complete") {
  onDocumentLoad();
} else {
  document.addEventListener("DOMContentLoaded", onDocumentLoad);
}
