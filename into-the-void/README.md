# into-the-void

<i>Medium Forensics Challenge by TetraTarius</i>

[Challenge Archive](https://ctf-2023.clubeh.ca/challenges#into-the-void-385468698)

### Challenge Question

We've discovered an image left behind by one of the hackers of `t3l0s`, we suppose there may be some kind of data or message hidden within this image. Can you retrieve it?

<details> 
  <summary>Hints</summary>
  <ol>
    <li>Challenge can be considered 'steganography'</li>
    <li>Look up common stego tools, what are common techniques for hiding data within images? maybe there's portions of the data not being used?</li>
  </ol>
</details>

<details> 
  <summary>Answer Summary</summary>
  <ol>
    <li>Look up common image steganography techniques, i.e., check hacktricks.xyz</li>
    <ul>
      <li>Note that the image is a PNG, some stego techniques are unique to PNG and some may not even work on other formats or others may not work on this format.</li>
      <li>The bits in the image may be a hint about "Least Significant Bit" steganography.</li>
    </ul>
    <li>Most Stego-LSB tools will work.</li>
    <ul>
      <li>The one I used was: https://pypi.org/project/stego-lsb/</li>
    </ul>
    <li>Run the stego-lsb tool on the image and it will spit out another image with the flag as a string of text.</li>
  </ol>
</details>
<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{plA70_0n_7hE_W1RE}<b>
</details>
