# PoC || GTFO

Easy Misc challenge by Spaghetti
		
### Challenge Question

There is a flag hidden within this PDF newsletter, can you find it?

<details>
  <summary>Answer summary and flag</summary>
  
  The flag is in the variable name for the email text field. There are lots of tools to get a data dump from the PDF, I used PDF toolkit.
  
  `pdftk poc-or-gtfo.pdf dump_data_fields output data_fields`
  
  
</details>

## Instructions for testers

- The PDF file can be found in the `static` directory.

