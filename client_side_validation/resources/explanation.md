# Exploitation of Survey Rating Limit

## Description
This vulnerability involved bypassing input validation on a survey page by manipulating the rating value submitted through the form. The goal was to exceed the allowed rating limit, which was set to a maximum of 10.

## Steps to Exploit
1. **Accessing the Survey Page:**
   - We navigated to the survey page and initiated the process of submitting a rating.

2. **Intercepting the Request:**
   - Using Burp Suite, we intercepted the request containing the rating value.

3. **Modifying the Rating Value:**
   - Upon inspecting the request, we noticed the rating parameter, which had a maximum allowed value of 10. We modified this value to a number greater than 10 (e.g., 15) and prepared the request for submission.

4. **Sending the Modified Request:**
   - After changing the rating value, we sent the modified request. The server processed the input without validating the new rating limit, and we successfully received the flag.

## Impact
This type of vulnerability can have significant implications, such as:

- **Data Integrity Issues:** By bypassing input validation, attackers can manipulate data, potentially skewing survey results or other metrics derived from user input.

- **Reputation Damage:** Organizations rely on accurate survey data to inform decisions. If manipulated, it can lead to poor decision-making based on false information, damaging the organization's credibility.

- **Exploitation of Weaknesses:** This vulnerability demonstrates weak parsing and validation mechanisms, making the application susceptible to further attacks.

## Mitigation
1. **Input Validation:** Implement robust input validation on the server side to ensure that all submitted values conform to expected ranges and types.

2. **Error Handling:** Employ proper error handling to manage invalid input gracefully, returning informative error messages to users without exposing underlying system details.

3. **Regular Security Audits:** Conduct regular security assessments and code reviews to identify and remediate vulnerabilities related to input handling and data processing.
