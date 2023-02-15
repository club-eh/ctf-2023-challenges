# zeuszip

<i>Easy Cryptography Challenge by tetratarius</i>

### Challenge Question

We've extracted a file from one of t3l0s' hacker's dropbox servers, but the file is password protected. Can you bypass the password protection and read the contents?

<details> 
  <summary>Hints</summary>
  <ol>
   <li>Google something about password protected zips...</li>
  </ol>
</details>

<details> 
  <summary>Answer Summary</summary>

  1. Generate hash file for [John the Ripper](https://www.openwall.com/john/):  
     `zip2john zeus.zip > ziphash.txt`
  2. Crack the password using the `rockyou` wordlist:  
     `john --format=zip ziphash.txt --wordlist=/usr/share/wordlists/rockyou.txt`
  3. Extract `flag.txt` from the archive using the cracked password.
  4. Read `flag.txt` to get the flag.
</details>

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{m1n074urs_5p3C14L_h1D1n6Pl4c3}</b>
</details>
