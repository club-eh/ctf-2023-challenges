# Jason's New Website

<i>Medium Web Exploitation Challenge by Arshdeep</i>

### Challenge Question

Hi! I'm Jason, and I've recently made my very own website using Go!

Unfortunately, the t3l0s hackers have managed to get access to my data.  
I don't know how it happened - I even used JWTs for security!

Can you help me determine how they got in?
Link: [http://challenges.ctf-2023.clubeh.ca:61214/](http://challenges.ctf-2023.clubeh.ca:61214/)

<details> 
  <summary>Hints</summary>
  <ol>
   <li>So many people can edit Wikipedia, I wonder how they keep track of the changes.</li>
  </ol>
</details>

<details> 
  <summary>Answer Summary</summary>
  <ol>
   <li>Read server.go, in the login method (handler for POST /login route), there is a function named checkHeaders, it checks for various custom headers and appends different properties to the response body based on the input value of the header. There is a custom header named `X-Env` which allows users to lookup for environment variable values.</li>
   <li>Make a POST request to route /login, with `X-Env` value as `SECRET`, which returns the JSON Web Token signing secret for the cookie.</li>
    &emsp;sh curl -X POST -H 'X-Env: SECRET' <url>/login
    <li>With the secret for JWT, go to [jwt.io](https://jwt.io), set the payload as:</li>
    &emsp;json { "isAdmin": true }<br>
    &emsp;and the secret as the secret you got from step 2.
    <li>Copy the encoded token, go to your browser, and for the challenge website, add the cookie named `token`, and the value is the encoded token copied from step 3. Refresh the web page and you should see the flag there. It can similarly achieved using the following curl command.</li>
    &emsp;sh curl -H 'Cookie: token=<token>' <url>
   </ol>

    <b>NOTE:</b> There is also a 32 characters password `3f*So0gmedVPRsoDD!kxx7fCfjfNkn*FW`, which can be used to login directly, the program file contains the bcrypt hash of the password.It is almost impossible to get the password using password cracking from the hash, therefore the hash is hard coded in the program itself.
</details>

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{1_4h0ugh4_jw45_w3r3_mag1c_2b7887ce}</b>
</details>
