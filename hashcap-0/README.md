# Hashcap-0

Easy Cryptography challenge by tetratarius

### Challenge Question

We have managed to extract a password hash that we think is associated with one of the t3l0s hacker's accounts. Can you crack this hash?

Hash: `1c00e6b82bf96321a63b070333e3c48f775d973b951b929e07e309b6d5c8f73c`

Flag format: `clubeh{<cracked_password>}`

<details> 
  <summary>Hint</summary>
  Look up how to crack password hashes...
</details>

<details> 
  <summary>Answer summary and flag</summary>
  Steps: <br>
  1. put hash into a hash.txt file <br>
  2. run john --format=raw-sha256 hash.txt --wordlist=usr/share/wordlists/rockyou.txt<br>
  3. copy and paste the password as the flag :)<br>
  Flag: clubeh{caesar44}
</details>
