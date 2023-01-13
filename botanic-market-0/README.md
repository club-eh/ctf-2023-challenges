# Botanic Market 

Easy web challenge by Spaghetti

### Challenge Question

This website is still under construction, can you find a vulnerability?

<details> 
  <summary>Answer summary and flag</summary>
  
  There is a double base64 encoded admin cookie that needs to be set to `ZEhKMVpR`, or true in double base64 (URL-safe variant).
  
  clubeh{c00k13_4u7h3n71c4710n_15_n07_54f3_eEr328VD}
</details>

## Instructions for testers

- Change working directory to `dynamic/`.
- Run the command `docker-compose build`.
- Run the command `docker-compose up`.
- Go to `http://localhost:1337` in your browser.

