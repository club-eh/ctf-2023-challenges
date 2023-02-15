# Hashcap-1

<i>Medium Cryptography Challenge by tetratarius</i>

### Challenge Question

We have managed to extract another password hash that we think is associated with one of the t3l0s hacker's accounts. Can you crack this hash?

Hash: `2790e01b73f4db3dbf3613fbe084d2a2de9d1d4d7ce24d8c8d5f47262f2b7ba7`

Flag format: `clubeh{<cracked_password>}`

<details> 
  <summary>Hints</summary>
  <ol>
    <li>Look up how to crack password hashes... maybe advanced password cracking...</li>
  </ol>
</details>

<details> 
  <summary>Answer Summary</summary>
  <ol>
    <li>Put hash into a hash.txt file</li>
    <li>Run john --format=raw-sha256 hash.txt --wordlist=usr/share/wordlists/rockyou.txt --rules=appendyears</li>
    <li>Copy and paste the password as the flag :)</li>
  </ol>
</details>

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{caesar441999}</b>
</details>
