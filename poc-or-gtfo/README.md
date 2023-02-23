# PoC || GTFO

<i>Easy MISC Challenge by Spaghetti</i>

### Challenge Question

There is a flag hidden within this PDF newsletter, can you find it?

<details>
  <summary>Hints</summary>

  1. Look into PDF objects and artifacts.
</details>

<details>
  <summary>Answer Summary</summary>

  &emsp;The flag is in the variable name for the email text field.  
  &emsp;There are lots of tools to get a data dump from the PDF; I used PDF toolkit.

  &emsp;Run the command: `pdftk poc-or-gtfo.pdf dump_data_fields output data_fields`
</details>

<details>
  <summary>Flag</summary>

  &emsp;**clubeh{d4t4_f131d5_dump_g8fas6}**
</details>

