# Directory Traversal Exploitation

## Description
This vulnerability involved exploiting a directory traversal flaw by manipulating file paths to access restricted files on the server. Our goal was to retrieve the contents of the `/etc/passwd` file, which typically contains user account information.

## Steps to Exploit
1. **Initial Path Submission:**
   - Using Burp Suite, we began by attempting to access the `/etc/passwd` file with the input `../etc/passwd`. This request did not return any results.

2. **Refining the Path:**
   - Next, we modified our input to `../../etc/passwd`, which prompted a response indicating a potential directory traversal issue.

3. **Continuing the Traversal:**
   - Encouraged by the response, we continued to append `../` to the path incrementally. This process involved several attempts until we reached the following input:
     ```
     ../../../../../../../etc/passwd
     ```

4. **Retrieving the Flag:**
   - Upon submitting the modified path, we successfully accessed the `/etc/passwd` file and retrieved the flag contained within it.

## Impact
This directory traversal vulnerability can lead to serious consequences, including:

- **Unauthorized Access:** Attackers can gain access to sensitive files and information stored on the server, potentially exposing user credentials and other critical data.

- **System Compromise:** If exploited, this vulnerability could allow attackers to read configuration files or other sensitive information that could facilitate further attacks on the system.

- **Loss of Confidentiality:** The exposure of sensitive data can lead to breaches of confidentiality, affecting user privacy and potentially leading to regulatory violations.

## Mitigation
1. **Input Validation:** Implement strict validation of user input to ensure that only permitted file paths are processed by the server.

2. **Restrict Access to Sensitive Files:** Configure the server to restrict access to sensitive files and directories, ensuring that they cannot be accessed through web requests.

3. **Use of Web Application Firewalls (WAF):** Deploy a WAF to monitor and filter incoming requests, helping to prevent directory traversal attempts and other common vulnerabilities.
