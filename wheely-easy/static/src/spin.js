function rotateMiddle() {
	key1 = document.querySelector("#key1").value;
	angle = (key1 % 36) * -10;
	document.querySelector("#middle").style.transform = `rotate(${angle}deg)`;
	
	if (document.querySelector('#key2').value == "") {
		document.querySelector("#inner").style.transform = `rotate(${angle}deg)`;
	}
}
function rotateInner() {
	key1 = document.querySelector("#key1").value;
	key2 = document.querySelector("#key2").value;
	angle1 = ((key1) % 36) * -10;
	angle2 = angle1 + (((key2) % 36) * -10);
	document.querySelector("#inner").style.transform = `rotate(${angle2}deg)`;
}

