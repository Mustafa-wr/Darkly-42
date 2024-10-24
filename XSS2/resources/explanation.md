
# Exploitation of Home Screen Image

## Description
During our testing, we noticed a clickable image on the home screen that led to the URL `http://localhost/?page=media&src=nsa`. We attempted to exploit this by injecting a script into the `src` parameter.

## Steps to Exploit
1. **Identifying the Clickable Image:**
   - We clicked the image on the home screen, which altered the URL to `http://localhost/?page=media&src=nsa`.

2. **Attempting XSS Injection:**
   - We tried to pass a script through the `src` parameter, but while it was successfully sent, we did not receive the flag.

3. **Using XSS Payloads:**
   - Utilizing payloads from the repository "https://github.com/payloadbox/xss-payload-list" in Burp Suite, we found an interesting line:
     ```
     src="data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+"
     ```
   - This indicated that the application might be handling base64-encoded data differently.

4. **Encoding Our Payload:**
   - We converted our simple script to base64 using the command:
     ```bash
     echo "<script>alert(1)</script>" | base64
     ```
   - This resulted in the output: `PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pgo=`.

5. **Injecting the Encoded Payload:**
   - We placed the base64 output into the payload and successfully retrieved the flag.
	"http://localhost/?page=media&src="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pgo=""


## Flag
The flag was successfully obtained after executing the base64-encoded script.

## Impact
This type of vulnerability can have significant implications, such as:

- **Arbitrary Script Execution:** Attackers can execute arbitrary scripts in users' browsers, compromising security.

- **Data Theft:** Sensitive user data can be stolen through unauthorized script execution.

- **Reputation Damage:** Security vulnerabilities can erode user trust and damage the organization’s reputation.

## Mitigation
1. **Input Validation:** Ensure that all user inputs are properly validated and sanitized to prevent script injection.

2. **Content Security Policy:** Implement a Content Security Policy (CSP) to restrict script execution from untrusted sources.

3. **Regular Security Audits:** Conduct ongoing security assessments to identify and remediate vulnerabilities, especially in input handling.



