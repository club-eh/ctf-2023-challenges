# Hashcap-2

<i>Hard Cryptography Challenge by tetratarius</i>

[Challenge Archive](https://ctf-2023.clubeh.ca/challenges#hashcap-2-510632834)

### Challenge Question

We have managed to extract another password hash that we think is associated with one of the t3l0s hacker's accounts. Can you crack this hash?

Hash: `baf87edc0909566f043de0b04f6e95541da7082313ca91bafa83d48606effa9f`

Flag format: `clubeh{<cracked_password>}`

<details> 
  <summary>Hints</summary>
  <ol>
    <li>Look up how to crack password hashes... look at the man pages or documentation for the cracking tools and look at the different things you can do to improve the probabilty of cracking it.</li>
  </ol>
</details>

<details> 
  <summary>Answer Summary</summary>
  <ol>
    <li>Put hash into a hash.txt file</li>
    <li>Run `john --format=raw-sha256 hash.txt --wordlist=usr/share/wordlists/rockyou.txt --rules=prepend2numbersappend2numbers`</li>
    <li>Copy and paste the password as the flag :)</li>
  </ol>
</details>

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{69caesar4469}</b>
</details>
