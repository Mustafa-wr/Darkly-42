# Improper Access Control: Header Manipulation Referrer

## Description
This vulnerability involved redirecting from the website's "BornToSec" button to the Albatros page, where hidden comments provided critical information for exploitation. The comments indicated specific requirements for the request, including a referral URL and a user-agent string.

## Steps to Exploit
1. **Accessing the Albatros Page:**
   - By clicking the "BornToSec" button located at the bottom of the website, we were redirected to the Albatros page.

2. **Inspecting the Page:**
   - Upon inspecting the Albatros page's source code, we discovered a comment that read:
     ```
     <!--
     You must come from : "https://www.nsa.gov/".
     -->
     ```
   - Another comment suggested the use of a specific browser:
     ```
     <!--
     Let's use this browser : "ft_bornToSec". It will help you a lot.
     -->
     ```

3. **Modifying the Request with Burp Suite:**
   - Using Burp Suite, we intercepted the request to the Albatros page and modified the following headers:
     - **Referer:** Changed to `https://www.nsa.gov/`
     - **User-Agent:** Changed to `ft_bornToSec`

4. **Forwarding the Modified Request:**
   - After making the changes, we forwarded the modified request. This successfully triggered the conditions specified in the comments, and we received the flag.

## Impact
This type of vulnerability can have several vulnerabilities, including:

- **Access Control Bypass:** Attackers could exploit this vulnerability to gain unauthorized access to restricted pages or data by manipulating request headers.

- **Information Disclosure:** Sensitive information could be exposed if proper checks are not in place to validate the origin of requests.

- **User Trust Erosion:** If users become aware of such vulnerabilities, it could damage their trust in the security of the application, resulting in reputational harm.

## Mitigation
1. **Validate Request Headers:** Implement server-side checks to validate referer and user-agent headers to ensure that requests originate from legitimate sources.

2. **Security Best Practices:** Follow security best practices for web applications, including the use of tokens or session management to validate user access.

3. **Regular Security Audits:** Conduct regular security audits and code reviews to identify and remediate vulnerabilities that could be exploited through header manipulation.

4. **framework-specific protections:** web frameworks usually have built-in protections against header injection. Ensure using these features correctly.
