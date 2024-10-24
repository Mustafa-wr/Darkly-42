# Exploitation of Feedback Page

## Description
This vulnerability involved a Cross-Site Scripting (XSS) attack on the feedback page. By injecting a simple script, we aimed to execute arbitrary JavaScript in the context of the web application.

## Steps to Exploit
1. **Accessing the Feedback Page:**
   - We navigated to the feedback page, where user input was accepted without proper validation.

2. **Injecting the XSS Payload:**
   - We submitted a simple XSS payload: `<script>alert(1)</script>`.

3. **Executing the Payload:**
   - Upon submission, the script executed in the browser, indicating that the input was not properly sanitized.

## Flag
The flag was successfully retrieved after executing the XSS payload.

## Impact
This type of vulnerability can have significant implications, such as:

- **User Data Exposure:** Attackers could steal cookies or session tokens, compromising user accounts.
  
- **Malicious Redirection:** Users could be redirected to malicious sites, leading to phishing attacks.

- **Reputation Damage:** Such vulnerabilities can damage the reputation of the organization, eroding user trust.

## Mitigation
1. **Input Validation:** Implement robust input validation to sanitize and encode user inputs.

2. **Content Security Policy:** Utilize a Content Security Policy (CSP) to limit the sources from which scripts can be executed.

3. **Regular Security Audits:** Conduct regular security assessments to identify and remediate vulnerabilities related to XSS and input handling.
