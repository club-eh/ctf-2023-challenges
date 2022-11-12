# Challenge Solution

1. Read server.go, in the login method (handler for POST /login route), there is a
   function named checkHeaders, it checks for various custom headers and appends
   different properties to the response body based on the input value of the header.
   There is a custom header named `X-Env` which allows users to lookup for environment
   variable values.

2. Make a POST request to route /login, with `X-Env` value as `SECRET`, which returns the
   JSON Web Token signing secret for the cookie.
```sh
curl -X POST -H 'X-Env: SECRET' <url>/login
```

3. With the secret for JWT, go to [jwt.io](https://jwt.io), set the payload as 
```json
{
  "isAdmin": true
}
```
and the secret as the secret you got from step 2.

4. Copy the encoded token, go to your browser, and for the challenge website, add the
   cookie named `token`, and the value is the encoded token copied from step 3. Refresh
   the web page and you should see the flag there.
   It can similarly achieved using the following curl command.
```sh
curl -H 'Cookie: token=<token>' <url>
```
