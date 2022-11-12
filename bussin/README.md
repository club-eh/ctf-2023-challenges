# Bussin 

Medium cryptography challenge by Spaghetti
		
### Challenge Question

Can you decode this cipher? The only lead we have is `pegasus`

112250011041{21244235_0154_05_150350051354_3541143141254155}

<details>
  <summary>Answer summary and flag</summary>
  
  This uses a polybius cipher in a col/row notation. `pegasus` is the starting key as seen below.

    || 0 | 1 | 2 | 3 | 4 | 5 |
  ----------------------------
  0 || p | e | g | a | s | u |
  1 || b | c | d | f | h | i |
  2 || j | k | l | m | n | o |
  3 || q | r | t | v | w | x |
  4 || y | z | 0 | 1 | 2 | 3 |
  5 || 4 | 5 | 6 | 7 | 8 | 9 |
		
  clubeh{d0n7_b3_4_5qu4r3_7hzfh6h9}
</details>

## Instructions for testers

- Everything needed is in the challenge question

