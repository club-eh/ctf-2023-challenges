# Blinkenlights-2

Hard MISC (Hardware and Forensics) challenge by Artemis

### Challenge Question

This is the last t3l0s microcontroller we found containing secret messages.

We have no idea what's going on with this one. Good luck.

Note: there are two versions of the exact same recording.  
One is in grayscale (`-gray`), the other in full RGB. 
**You only need one to solve the challenge.**

<details> 
  <summary>Answer summary and flag</summary>
  
  This challenge is in binary.<br>
  There is 2 strings split up that must be xor'd after you have retrieved them.<br>
  Both strings start with xor, to give you a hint to complete this step.<br>
  
  The green light that stays on for over 1 second signifies that start of string 1, and is not included in the string.<br>
  The red light that stays on for over 1 second signifies that start of string 2, and is not included in the string.<br>
  
  String 1:<br>
  Both Red and green is "1".<br>
  Neither red or green is "0".<br>
  Green by itself signifies still in string 1.<br>
  
  String 2:<br>
  Both Red and green is "1".<br>
  Neither red or green is "0".<br>
  Red by itself signifies still in string 2.<br>
  
  I created a solve script for color version this challenge. It is located in this folder and called Blinkenlights-2-solve.py
  
  Flag: clubeh{cc_x0r_l3d$_6432684}
  
</details>
