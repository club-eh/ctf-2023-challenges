# Captured Data

<i>Easy Forensics Challenge by tetratarius</i>

### Challenge Question

We have managed to capture some web traffic related to one of the attackers, can you decode it?

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im0xbjA3NHVyIiwibmFtZSI6IlJFREFDVEVEIiwicGFzcyI6ImNsdWJlaHtVbkM0UDd1cjQ4TDN9IiwicmVmZXJyZXIiOiJSRURBQ1RFRCJ9.TLKdT07xfu3jk1kMeWUoqPE2whuBd0kMCKLjsQTQBgM`

<details> 
  <summary>Hints</summary>
  <ol>
    <li>Look up common encodings used in web applications...</li>
  </ol>
</details>

<details> 
  <summary>Answer Summary</summary>
  <ol>
    <li>Challenge is an encoded JWT token, sort of tip-off to this is that it starts with `eyJ...`, most JWT's start with something like this.</li>
    <li>Solve by pasting the encoded text into CyberChef's input field and run the "magic" operation in the recipe column. Cyberchef will immediately tell that it's a JWT and decode it for you.</li>
    <li>See the flag inside the JWT, "clubeh{UnC4P7ur48L3}".</li>
   </ol>
</details>

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{UnC4P7ur48L3}</b>
</details>
