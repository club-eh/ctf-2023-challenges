# Bussin 

Medium cryptography challenge by Spaghetti
		
### Challenge Question

Can you decode this cipher? The only lead we have is `pegasus`

112250011041{21244235_0154_05_150350051354_3541143141254155}

<details>
  <summary>Answer summary and flag</summary>
  
  This uses a polybius cipher in a col/row notation. `pegasus` is the starting key as seen below.
  <p>
  --|| 0 | 1 | 2 | 3 | 4 | 5 |<br>
  0 || p | e | g | a | s | u |<br>
  1 || b | c | d | f | h | i |<br>
  2 || j | k | l | m | n | o |<br>
  3 || q | r | t | v | w | x |<br>
  4 || y | z | 0 | 1 | 2 | 3 |<br>
  5 || 4 | 5 | 6 | 7 | 8 | 9 |<br>
  </p>
  clubeh{d0n7_b3_4_5qu4r3_7hzfh6h9}
</details>

## Instructions for testers

- Everything needed is in the challenge question

