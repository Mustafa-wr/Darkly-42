
# Exploitation of Upload Page

## Description
This vulnerability involved bypassing file upload restrictions on an upload page. We aimed to exploit the server's handling of file types to upload a malicious file and retrieve sensitive data.

## Steps to Exploit
1. **Testing File Uploads:**
   - We began by attempting to upload images in various formats, but the server rejected all of them.

2. **Experimenting with Different File Types:**
   - Next, we tested other file types, including `.js` and `.php`, but received similar rejections. 

3. **Finding an Accepted Extension:**
   - Ultimately, we discovered that the server accepted files with the `.php.jpeg` extension.

4. **Uploading the Malicious File:**
   - After successfully uploading a file named `m.php.jpeg`, we did not receive any immediate indication of a successful exploit.

5. **Executing a POST Request:**
   - To further investigate, we executed a POST request using `curl` with the following command:
   ```bash
   curl -X POST -H 'Content-Type: multipart/form-data' --form 'Upload=Upload' --form 'uploaded=@m.php.jpeg;type=image/jpeg' http://localhost/?page=upload
   ```
   - After executing this command, we successfully retrieved the flag.

## Flag
The flag is: `46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8`

## Impact
This type of vulnerability can have significant implications, such as:

- **Remote Code Execution:** If an attacker can upload and execute a malicious file, they may gain unauthorized access to the server or sensitive data.

- **Data Breach Risks:** Exploiting file upload vulnerabilities can lead to data breaches, compromising user information and sensitive system data.

- **Denial of Service:** Malicious uploads can be used to disrupt services, leading to downtime and loss of trust from users.

## Mitigation
1. **Strict File Type Validation:** Implement strict validation checks to only allow specific file types and extensions for upload.

2. **Content Scanning:** Use antivirus and malware scanning for uploaded files to identify and block malicious content before it reaches the server.

3. **Limit File Permissions:** Ensure that uploaded files are stored with minimal permissions and in directories that do not allow execution.

4. **Regular Security Audits:** Conduct regular security assessments to identify and remediate vulnerabilities related to file uploads and server configurations.
