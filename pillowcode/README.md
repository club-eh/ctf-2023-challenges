# Pillowcode

<i>Medium Forensics Challenge by sudoBash418</i>

### Challenge Question

We've managed to capture some data from an adversary - but they seem to have encoded the data in an image?

<details> 
  <summary>Answer Summary</summary>
  &emsp;The naive solve is to directly reverse the operations from `encode()`:<br>
  &emsp;&emsp;flag[i] = (r & 0x70) | (g & 0x8a) | (b & 0x05)<br><br>
  &emsp;A simpler solution is possible:<br>
  &emsp;&emsp;flag[i] = r | g | b<br><br>
  &emsp;Solve script is available at `source/solve.py`
</details>

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{f1ddl1n9_w1th_p1x3l5_4nd_b1t5_118e08f9}</b>
</details>
