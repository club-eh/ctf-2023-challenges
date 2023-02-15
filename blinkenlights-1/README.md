# Blinkenlights-1

Medium MISC (Hardware and Forensics) challenge by Artemis

### Challenge Question

Here is another one of the microcontrollers used by t3l0s to send secret messages.

This pattern is different. Could you help me decode it?

Flag format: `clubeh{<recovered_text>}`

Note: there are two versions of the exact same recording.  
One is in grayscale (`-gray`), the other in full RGB. 
**You only need one to solve the challenge.**

<details> 
  <summary>Answer summary and flag</summary>
  
  Steps:
  This challenge displays a hidden message in morse code.
  Both lights on is a "-" and one light on is a ".".
  
  I created a solve script for color version this challenge. It is located in this folder and called Blinkenlights-1-solve.py
  
  Flag: clubeh{n3wtr1ck5325196} or clubeh{N3WTR1CK5325196}
  
</details>