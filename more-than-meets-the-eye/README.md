# More Than Meets the Eye

<i>Easy Forensics Challenge by tetratarius</i>

### Challenge Question

We have recovered some data from the hackers. We're sure that they've hidden a message within, can you recover it?

<details> 
  <summary>Hints</summary>
  <ol>
   <li>There may be other files inside this file...</li>
  </ol>
</details>

<details> 
  <summary>Answer Summary</summary>
  <ol>
    <li>Tip that it's in the forensics category means that you should probably look up how to perform digital forensics on a binary.</li>
    <li>Common technique for binary analysis is to run binwalk on it to find any hidden filetypes within it.</li>
    <ul>
      <li>Run binwalk -e to extract any files that are discovered.</li>
    </ul>
    <li>The flag will be an extracted image from the binary. </li>
  </ol>
&nbsp;&nbsp;<b>Note: </b>There are many other files within it that are meant to distract you from the flag.
</details>

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{m1N074Ur5_c0LL3c710N}</b>
</details>
