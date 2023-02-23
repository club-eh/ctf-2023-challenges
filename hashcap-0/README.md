# Hashcap-0

<i>Easy Cryptography Challenge by tetratarius</i>

[Challenge Archive](https://ctf-2023.clubeh.ca/challenges#hashcap-0-510623612)

### Challenge Question

We have managed to extract a password hash that we think is associated with one of the t3l0s hacker's accounts. Can you crack this hash?

Hash: `1c00e6b82bf96321a63b070333e3c48f775d973b951b929e07e309b6d5c8f73c`

Flag format: `clubeh{<cracked_password>}`

<details> 
  <summary>Hints</summary>
  <ol>
    <li>Look up how to crack password hashes...</li>
  </ol>
</details>

<details> 
  <summary>Answer Summary</summary>
  <ol>
    <li>Put hash into a hash.txt file</li>
    <li>Run john --format=raw-sha256 hash.txt --wordlist=usr/share/wordlists/rockyou.txt</li>
    <li>Copy and paste the password as the flag :)</li>
  </ol>
</details>

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{caesar44}</b>
</details>
