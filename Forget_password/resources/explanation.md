# Password Reset Exploitation

## Description
This vulnerability involved exploiting the "Forgot Password" functionality to retrieve the flag by manipulating the email address sent in the request. Initially, the password reset form accepted an email input that could be modified to test the system's response.

## Steps to Exploit
1. **Access the Forgot Password Functionality:**
   - On the login page, we clicked the "Forgot Password" link to access the password recovery form.

2. **Inspect the Network Request:**
   - Using the browser's Developer Tools, we navigated to the Network tab to monitor the requests made when submitting the password reset form.
   - We identified a POST request that included an email field in the form data.

3. **Modify the Email Address:**
   - We changed the email field to a random, arbitrary email address to test the server's response.

4. **Submit the Form:**
   - After modifying the email address, we submitted the form.
   - Upon sending the modified request, we received a response containing the flag.

## Impact
This type of vulnerability can have serious implications if exploited by malicious actors:

- **Account Takeover:** An attacker could gain unauthorized access to user accounts by exploiting the password reset functionality, especially if the backend does not validate email addresses properly.
  
- **Information Disclosure:** Exploiting the password recovery process can lead to the exposure of sensitive information, including flags or confidential data stored on the server.

- **User Trust Erosion:** If users become aware of such vulnerabilities, it could damage their trust in the application, leading to a decline in user engagement and potential financial loss.

## Mitigation
1. **Backend Validation:** Ensure that the backend properly validates the email address before processing password reset requests. Implement checks to ensure that the request is legitimate and that the email belongs to an existing user.

2. **Enhanced Security Measures:** Use multi-factor authentication (MFA) and other security measures to protect accounts from unauthorized access, even if an attacker is able to manipulate the password reset process.
