# Password Cracking (Brute Force Attack)

## Description
This Flag involved performing a brute force attack on the login page to identify a valid username and password combination. By testing a list of common passwords, we were able to successfully gain access and retrieve the flag.

## Steps to Exploit
1. **Identify Target:**
   - The login page was identified as the target for the brute force attack.

2. **Use the Script:**
   - We used a Bash script to automate the process of testing a list of common passwords against the login form. The script iterated through the passwords and checked the response for the presence of the flag.

3. **Run the Script:**
   - The script was executed with a password list (`10k.txt`). During the process, the correct password "shadow" was identified.

4. **Gain Access:**
   - After identifying the correct password, "shadow," the login was successful, and the flag was obtained.


## Impact
The success of a brute force attack highlights several critical vulnerabilities:

- **Weak Password Policies:** If users or administrators use common or weak passwords, they become easy targets for brute force attacks. This can lead to unauthorized access to sensitive systems and data.
  
- **Account Compromise:** Once an attacker gains access through brute force, they can potentially escalate privileges, access sensitive information, or perform malicious activities within the system.

- **Automation Risks:** Automated scripts can quickly cycle through password lists, making brute force attacks more efficient and dangerous if proper protections are not in place.



## Mitigation
To prevent brute force attacks, consider implementing the following security measures:

- **Strong Password Policies:** Enforce strong password policies requiring a combination of uppercase letters, lowercase letters, numbers, and special characters.
  
- **Account Lockout Mechanisms:** Implement account lockout mechanisms that temporarily disable an account after a certain number of failed login attempts.
  
- **CAPTCHA:** Introduce CAPTCHA or other challenge-response tests to make automated brute force attacks more difficult.

- **Two-Factor Authentication (2FA):** Implement two-factor authentication to add an additional layer of security, requiring not just a password but also a second form of verification.

## Script Used
Below is the Bash script used to perform the brute force attack:

```bash
#!/bin/bash

passwords=$(<10k.txt)

# Split the passwords into an array
IFS=$'\n' read -d '' -r -a password_array <<< "$passwords"

counter=1

for i in "${password_array[@]}"; do
    response=$(curl -X POST "http://localhost/index.php?page=signin&username=admin&password=${i}&Login=Login#")
    echo "$response" | grep 'flag' && echo "Flag found on password ${counter}: ${i}" && break
    ((counter++))
done
```

How the Script Works:

Password List: The script reads a list of 10,000 common passwords from a file named 10k.txt.
Iteration: It then iterates through each password, using curl to submit the password to the login form.
Flag Detection: If the response contains the word "flag," the script outputs the correct password and stops.
