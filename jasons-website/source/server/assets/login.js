function alertMessage(message) {
  return `
    <div class="alert alert-danger">
      ${message} 
    </div>`;
}

$(document).ready(() => {
  const username = $("#username");
  const password = $("#password");
  const loginButton = $("#login");

  $("#login-form").on("submit", (event) => {
    event.preventDefault();

  });
});
