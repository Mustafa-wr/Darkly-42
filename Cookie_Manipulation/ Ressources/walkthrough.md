Explanation
# Cookie Manipulation

## Description
This vulnerability involved manipulating the value of an admin cookie to gain unauthorized access and retrieve the flag. The website initially provided an MD5 hashed cookie value of "68934a3e9455fa72420237eb05902327," which, when decoded, translates to "false."

## Steps to Exploit
1. **Intercept the Request:**
   - Upon visiting the website's homepage, the response contained an admin cookie with the value "68934a3e9455fa72420237eb05902327."
   - This value was decoded using the MD5 hashing algorithm, revealing it to be "false.", example tool used (https://www.cmd5.org/)

2. **Generate the Correct Hash:**
   - To exploit the breach, we needed the cookie to represent "true" instead of "false."
   - The value "true" was encoded using MD5, resulting in the hash "b326b5062b2f0e69046810717534cb09."

3. **Modify the Cookie:**
   - Using BurpSuite's intercept feature, the original cookie value was replaced with the MD5 hash for "true" ("b326b5062b2f0e69046810717534cb09").

4. **Forward the Request:**
   - After modifying the cookie, the request was forwarded, successfully granting access and allowing us to retrieve the flag.



## Impact
This type of vulnerability can have severe consequences if exploited by Hackers:

- **Unauthorized Access:** An attacker can gain administrative privileges by simply altering a cookie value. This could lead to the attacker gaining control over sensitive data, user accounts, or even the entire web application.
  
- **Data Breach:** With administrative access, an attacker could access, modify, or delete critical data, potentially leading to data breaches that compromise user privacy and violate regulations.

- **System Compromise:** In some cases, gaining admin access through cookie manipulation could allow an attacker to install malicious software or backdoors, leading to a complete system compromise.

- **Loss of Trust:** If users or customers become aware that such a vulnerability exists, it could result in a significant loss of trust, damaging the reputation of the organization and leading to financial losses.


## Mitigation
1- To prevent such vulnerabilities, ensure that cookie values, especially those indicating administrative access, are securely handled and validated on the server side. Relying solely on client-side controls like cookies can lead to unauthorized access if not properly secured.

2- Genrally use more strong hashing algorithms than md5 as it's easy to find the hash value through the plenty available hash dictionaries for md5 hash
