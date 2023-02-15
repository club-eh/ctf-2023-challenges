# secretman

<i>Medium Reverse Engineering Challenge by tetratarius</i>

### Challenge Question

We've found what we suspect to be one of the hacker's programs for storing secrets, we believe that a secret key is hidden within the program.

<details> 
  <summary>Hints</summary>
  <ol>
    <li>Look up what a .pyc file is</li>
    <li>Look up how to reverse engineer a .pyc file</li>
  </ol>
</details>

<details> 
  <summary>Answer Summary</summary>
  <ol>
    <li>Download one of the .pyc reversing tools from the internet (uncompyle/decompyle), it will likely not work and tell the player that the python bytecode is python 3.10</li>
    <li>Google decompyle python 3.10, find this tool https://github.com/zrax/pycdc</li>
    <li>Need to compile it using CMAKE, and then make (this point may be a serious bottleneck that stops most beginners)</li>
    <li>Run pycdc on the secretman.pyc file to then understand the code better</li>
    <li>Realize that the two strings at the beginning of the file are a super simple way to hide the flag within the first two-dimensional string array using [index][index] combinations.</li>
    <li>Next you can:</li>
    <ol>
      <li>Manually get the flag from the 2-dim array</li>
      <li>Write a python script to do it for you</li>
      <li>Copy the function from the decompyled secretman.pyc and paste that with the strings into a python script to automate it for you</li>
    </ol>
  </ol>
</details>

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{tH3s3us_sUcK50rz}</b>
</details>
