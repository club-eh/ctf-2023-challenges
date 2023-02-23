# Blinkenlights-2

<i>Hard MISC (Hardware and Forensics) Challenge by Artemis</i>

[Challenge Archive](https://ctf-2023.clubeh.ca/challenges#Blinkenlights%202-287043646)

### Challenge Question
This is the last t3l0s microcontroller we found containing secret messages.

We have no idea what's going on with this one. Good luck.

Note: there are two versions of the exact same recording.  
One is in grayscale (`-gray`), the other in full RGB. 
**You only need one to solve the challenge.**

<details> 
  <summary>Answer Summary</summary>
  &emsp;This challenge is in binary.<br>
  &emsp;There is 2 strings split up that must be xor'd after you have retrieved them.<br>
  &emsp;Both strings start with xor, to give you a hint to complete this step.<br><br>
  &emsp;The green light that stays on for over 1 second signifies that start of string 1, and is not included in the string.<br>
  &emsp;The red light that stays on for over 1 second signifies that start of string 2, and is not included in the string.<br><br>
  &emsp;String 1:<br>
  &emsp;&emsp;Both Red and green is "1".<br>
  &emsp;&emsp;Neither red or green is "0".<br>
  &emsp;&emsp;Green by itself signifies still in string 1.<br><br>
  &emsp;String 2:<br>
  &emsp;&emsp;Both Red and green is "1".<br>
  &emsp;&emsp;Neither red or green is "0".<br>
  &emsp;&emsp;Red by itself signifies still in string 2.<br><br>
  &emsp;I created a solve script for color version this challenge. It is located in this folder and called Blinkenlights-2-solve.py
</details>

[Alternate writeup by sudoBash418](https://sb418.net/ctfs/writeups/2023-01-15_hackers-odyssey-ctf/blinkenlights-2/)

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{cc_x0r_l3d$_6432684}</b>
</details>
