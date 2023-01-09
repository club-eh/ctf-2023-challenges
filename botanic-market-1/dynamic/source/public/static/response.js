const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");
const BOT_NAME = "chatSNN";
const USER_NAME = "You";

/* Submits user message and gets bot response */
msgerForm.addEventListener("submit", event => {
	event.preventDefault();
	const msgText = msgerInput.value;
	if (!msgText) return;
	
	appendUserMessage(USER_NAME, msgText);
	msgerInput.value = "";
	botResponse(msgText);
	const chatWindow = document.getElementById('chat-window');

	setTimeout(() => {
    	chatWindow.scrollTop = chatWindow.scrollHeight;
	}, 500); 
});

/* Adds a user message to chat window */
function appendUserMessage(name, text) {
	const msgHTML = `
<div class="msg person-msg">
  <div class="msg-bubble" style="text-align: right;">
    <div class="msg-info">
      <div class="msg-info-name" style="display: inline-block">${name} ${formatDate(new Date())}</div>
    </div>
    <div class="user-talk-bubble">${text}</div>
  </div>
</div>
`;

	msgerChat.insertAdjacentHTML("beforeend", msgHTML);
	msgerChat.scrollTop += 500;
}

/* Adds a bot message to chat window */
function appendBotMessage(name, text) {
	const msgHTML = `
<div class="msg bot-msg">
  <div class="msg-bubble" style="text-align: left;">
    <div class="msg-info">
      <div class="msg-info-name" style="display: inline-block">${name} ${formatDate(new Date())}</div>
    </div>
    <div class="bot-talk-bubble">${text}</div>
  </div>
</div>
`;

	msgerChat.insertAdjacentHTML("beforeend", msgHTML);
	msgerChat.scrollTop += 500;
}

function botResponse(rawText) {
	$.get("/get", { msg: rawText }).done(function (data) {
		console.log(rawText);
		console.log(data);
		const msgText = data;
		appendBotMessage(BOT_NAME, msgText);
	});
}

function get(selector, root = document) {
	return root.querySelector(selector);
}

function formatDate(date) {
	const h = "0" + date.getHours();
	const m = "0" + date.getMinutes();
	return `${h.slice(-2)}:${m.slice(-2)}`;
}
