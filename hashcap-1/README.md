# Hashcap-1

Medium Cryptography challenge by tetratarius

### Challenge Question

We have managed to extract another password hash that we think is associated with one of the t3l0s hacker's accounts. Can you crack this hash?

Hash: `2790e01b73f4db3dbf3613fbe084d2a2de9d1d4d7ce24d8c8d5f47262f2b7ba7`

Flag format: `clubeh{<cracked_password>}`

<details> 
  <summary>Hint</summary>
  Look up how to crack password hashes... maybe advanced password cracking...
</details>

<details> 
  <summary>Answer summary and flag</summary>
  <br>
  Steps: <br>
  1. put hash into a hash.txt file <br>
  2. run john --format=raw-sha256 hash.txt --wordlist=usr/share/wordlists/rockyou.txt --rules=appendyears<br>
  3. copy and paste the password as the flag :)<br><br>
  
  Flag: clubeh{caesar441999}
</details>
