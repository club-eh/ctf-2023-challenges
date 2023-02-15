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
  <br>
	This uses a polybius cipher in a col/row notation. `pegasus` is the starting key as seen below.<br><br>
	<table style="width:50%">
	  <tr>
		  <th>--</th>
		  <th>1</th>
		  <th>2</th>
		  <th>3</th>
		  <th>4</th>
		  <th>5</th>
		  <th>6</th>
	  </tr>
	  <tr>
		  <th>1</th>
		  <td>p</td>
		  <td>e</td>
		  <td>g</td>
		  <td>a</td>
		  <td>s</td>
		  <td>u</td>
	  </tr>
	  <tr>
		  <th>2</th>
		  <td>b</td>
		  <td>c</td>
		  <td>d</td>
		  <td>f</td>
		  <td>h</td>
		  <td>i</td>
	  </tr>
	  <tr>
		  <th>3</th>
		  <td>j</td>
		  <td>k</td>
		  <td>l</td>
		  <td>m</td>
		  <td>n</td>
		  <td>o</td>
	  </tr>
	  <tr>
		  <th>4</th>
		  <td>q</td>
		  <td>r</td>
		  <td>t</td>
		  <td>v</td>
		  <td>w</td>
		  <td>x</td>
	  </tr>
	  <tr>
		  <th>5</th>
		  <td>y</td>
		  <td>z</td>
		  <td>0</td>
		  <td>1</td>
		  <td>2</td>
		  <td>3</td>
	  </tr>
	  <tr>
		  <th>6</th>
		  <td>4</td>
		  <td>5</td>
		  <td>6</td>
		  <td>7</td>
		  <td>8</td>
		  <td>9</td>
	  </tr>
	</table>
</details>

<details>
  <summary>Flag</summary>
  &emsp;<b>clubeh{d0n7_b3_4_5qu4r3_7hzfh6h9} or CLUBEH{D0N7_B3_4_5QU4R3_7HZFH6H9}</b>
</details>

