# PoC || GTFO

<i>Easy MISC Challenge by Spaghetti</i>
		
### Challenge Question

There is a flag hidden within this PDF newsletter, can you find it?

<details> 
  <summary>Hints</summary>
  <ol>
   <li>Look into PDF objects and artifacts.</li>
  </ol>
</details>

<details> 
  <summary>Answer Summary</summary>
  &emsp;The flag is in the variable name for the email text field. There are lots of tools to get a data dump from the PDF, I used PDF toolkit.
  &emsp;&emsp;`pdftk poc-or-gtfo.pdf dump_data_fields output data_fields`
</details>

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{d4t4_f131d5_dump_g8fas6}</b>
</details>

