# Directory Traversal Vulnerability and Authentication Bypass

## Description
In this challenge, we uncovered a vulnerability through directory traversal and authentication bypass. By analyzing the web server's file structure and leveraging weak credentials, we accessed restricted areas, leading to sensitive data exposure.

## Steps to Exploit

1. **Directory Listing with Gobuster:**
   - We used the Gobuster tool to identify accessible directories on the target website:
     ```bash
     gobuster dir -u "http://localhost/" -w "./common.txt" -b 200
     ```
   - This scan returned several paths, with the following notable entries:
     ```
     /admin                (Status: 301) [--> http://10.18.225.159/admin/]
     /audio                (Status: 301) [--> http://10.18.225.159/audio/]
     /css                  (Status: 301) [--> http://10.18.225.159/css/]
     /errors               (Status: 301) [--> http://10.18.225.159/errors/]
     /fonts                (Status: 301) [--> http://10.18.225.159/fonts/]
     /images               (Status: 301) [--> http://10.18.225.159/images/]
     /includes             (Status: 301) [--> http://10.18.225.159/includes/]
     /js                   (Status: 301) [--> http://10.18.225.159/js/]
     /whatever             (Status: 301) [--> http://10.18.225.159/whatever/]
     ```

2. **Identifying Vulnerable Paths:**
   - Exploring `/admin` revealed a login page with fields for a username and password.
   - In the `/whatever` directory, we located a file named `httpasswd` that, when downloaded and opened, revealed the following content:
     ```plaintext
     root:437394baff5aa33daa618be47b75cb49
     ```
   - The hashed value resembled an MD5 hash, prompting further investigation.

3. **Cracking the MD5 Hash:**
   - Using an MD5 decryption tool ([MD5 Decrypt](https://md5decrypt.net/en/)), we decrypted `437394baff5aa33daa618be47b75cb49`, which yielded the password `qwerty123@`.

4. **Accessing the Admin Panel:**
   - Returning to the `/admin` login page, we attempted multiple usernames with the password `qwerty123@`.
   - The credentials `root:qwerty123@` successfully bypassed the authentication, granting us access to the admin area.

## Flag
Within the admin area, we found the following flag:
`d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff`

## Impact
Directory traversal and weak authentication controls can lead to:

- **Unauthorized Access:** Attackers can gain access to restricted areas, potentially exposing sensitive data and system settings.
- **Credential Exposure:** Poor password management allows attackers to decode hashes and escalate access privileges.
- **Data Exfiltration:** Attackers can obtain sensitive information, such as hashed passwords and confidential resources.

## Evidence
*If available, include screenshots or logs showcasing the directory listing results, MD5 decryption output, and successful login.*

## Mitigation
To prevent vulnerabilities of this nature:

- **Restrict Directory Access:** Configure web server permissions to limit directory visibility and prevent traversal.
- **Strong Password Policies:** Enforce complex passwords and regularly update credentials to prevent easy decoding of hashed values.
- **Authentication Controls:** Implement multi-factor authentication and rate limiting to protect against unauthorized access.
- **Regular Audits:** Conduct security audits and penetration testing to uncover and address potential weaknesses.

## Payloads and Tools Used
### Gobuster Command
```bash
gobuster dir -u "http://localhost/" -w "./common.txt" -b 200
```
MD5 Decryption Tool
MD5 hash: 437394baff5aa33daa618be47b75cb49

Decrypted password: qwerty123@