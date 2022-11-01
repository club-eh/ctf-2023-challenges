function rotateMiddle() {
	key = document.querySelector("#key1").value;
	angle = (key % 36) * -10;
	document.querySelector("#middle").style.transform = `rotate(${angle}deg)`;
}
function rotateInner() {
	key = document.querySelector("#key2").value;
	angle = (key % 36) * -10;
	document.querySelector("#inner").style.transform = `rotate(${angle}deg)`;
}

