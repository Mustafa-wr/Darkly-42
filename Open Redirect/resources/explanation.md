


# Unvalidated Redirects and Forwards (Open Redirect)

## Description
Client side redirection open redirect vulnrablility:

An open redirect vulnerability occurs when a website allows user-controlled inputs to influence the URL to which the user is redirected without proper validation. This vulnerability can be exploited by attackers to redirect users from a trusted website to a malicious one, thereby compromising user trust and potentially leading to phishing attacks or further exploitation.

## Steps to Exploit
1. **Identify Vulnerable Element:**
   - During navigation, we inspected the social media buttons and found an HTML element structured as follows:
     ```html
     <a href="index.php?page=redirect&amp;site=instagram" class="icon fa-instagram"></a>
     ```
   - The `href` attribute included a `site=instagram` parameter, indicating that the redirection target was controlled by the `site` parameter.

2. **Parameter Manipulation:**
   - By substituting the `site=instagram` parameter with arbitrary values like `site=hello`, we experimented with different inputs.
   - On one such manipulation, we successfully triggered the open redirect and obtained the flag.



## Impact
Exploiting an open redirect vulnerability can have several serious consequences:

- **Phishing Attacks:** Attackers can use the open redirect to craft URLs that appear legitimate, luring users into providing sensitive information on malicious sites.
  
- **Exploitation of Trust:** Users may  follow a link that redirects them to a harmful website, leveraging their trust in the original website.

- **Further Attacks:** Open redirects can also be chained with other vulnerabilities, such as Cross-Site Scripting (XSS), to escalate the attack's impact.


## Mitigation
To prevent open redirect vulnerabilities, consider the following strategies:

- **Avoid Using User-Controlled Redirects:** Where possible, avoid allowing user inputs to determine redirect destinations. Instead, use hardcoded URLs.
  
- **Whitelist Validation:** Implement strict validation for redirect parameters, ensuring they match only a predefined set of allowed URLs or paths.

- **Regular Expression Validation:** Validate the input using regular expressions to ensure it conforms to expected patterns 