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
  <ol>
    <li>Run sudo zip2john zues.zip > ziphash.txt</li>
    <li>Run sudo john --format=zip ziphash.txt --wordlist=/usr/share/wordlists/rockyou.txt</li>
    <li>Extract the flag.txt file from zues.zip using cracked password.</li>
    <li>Read flag.txt to get the flag.</li>
  </ol>
</details>

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{m1n074urs_5p3C14L_h1D1n6Pl4c3}</b>
</details>
