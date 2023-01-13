# Bussin 

Medium cryptography challenge by Spaghetti
		
### Challenge Question

Can you decode this cipher? The only lead we have is `pegasus`

223361122152{32355346_1265_16_261461162465_4652254252365266}

<details>
  <summary>Answer summary and flag</summary>
  
  This uses a polybius cipher in a col/row notation. `pegasus` is the starting key as seen below.
  <p>
  --|| 1 | 2 | 3 | 4 | 5 | 6 |<br>
  1 || p | e | g | a | s | u |<br>
  2 || b | c | d | f | h | i |<br>
  3 || j | k | l | m | n | o |<br>
  4 || q | r | t | v | w | x |<br>
  5 || y | z | 0 | 1 | 2 | 3 |<br>
  6 || 4 | 5 | 6 | 7 | 8 | 9 |<br>
  </p>
  clubeh{d0n7_b3_4_5qu4r3_7hzfh6h9}
</details>

## Instructions for testers

- Everything needed is in the challenge question

