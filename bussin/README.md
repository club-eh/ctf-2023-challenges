# Bussin 

<i>Medium Cryptography Challenge by Spaghetti</i>
		
### Challenge Question

Can you decode this cipher? Our forensics team is unable to figure out the encryption, but they did recover the phrase `pegasus` from the rest of the data recovered from t3l0s, that might be helpful.

`223361122152{32355346_1265_16_261461162465_4652254252365266}`

<details>
  <summary>Hints</summary>
  <ol>
  	<li>Very old two dimensional cryptography algorithm.</li>
  </ol>
</details>

<details>
  <summary>Answer Summary</summary>
  &emsp;This uses a polybius cipher in a col/row notation. `pegasus` is the starting key as seen below.<br>
<p>
  --|| 1 | 2 | 3 | 4 | 5 | 6 |<br>
  1 || p | e | g | a | s | u |<br>
  2 || b | c | d | f | h | i |<br>
  3 || j | k | l | m | n | o |<br>
  4 || q | r | t | v | w | x |<br>
  5 || y | z | 0 | 1 | 2 | 3 |<br>6 || 4 | 5 | 6 | 7 | 8 | 9 |<br>
	</p>
</details>

<details>
  <summary>Flag</summary>
  &emsp;<b>clubeh{d0n7_b3_4_5qu4r3_7hzfh6h9} or CLUBEH{D0N7_B3_4_5QU4R3_7HZFH6H9}</b>
</details>

