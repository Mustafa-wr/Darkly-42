# Exploitation of Hidden Directory

## Description
During our enumeration process, we used the `gobuster` tool to discover hidden directories on the server. One of the findings was a hidden folder named `/.hidden`, which contained numerous links to other folders, each leading to more directories.

## Steps to Exploit
1. **Using Gobuster:**
   - We ran the `gobuster` tool to brute force the directories and found a hidden folder: `/.hidden`.

2. **Navigating the Hidden Folder:**
   - Upon navigating to `/.hidden`, we discovered more than 10 links to other folders, and inside each of them were even more folder links.

3. **Automating the Search:**
   - Instead of manually checking each folder, we decided to automate the process by using a script to traverse through all the folder links and output their contents recursively.

4. **Finding the Flag:**
   - After running the script, we found the flag hidden within one of the directories.

## Flag
The flag was successfully retrieved after recursively enumerating all the hidden folder contents.

## Impact
This type of vulnerability can expose sensitive files or directories that were unintentionally left on the server, such as:

- **Sensitive Data Exposure:** Attackers can gain access to configuration files, credentials, or other sensitive data left in hidden directories.
  
- **Unauthorized Access:** Files in hidden directories may provide insights or pathways to further exploit the system.

## Mitigation
1. **Directory Indexing:** Disable directory indexing on the server to prevent unauthorized access to hidden directories.

2. **File and Directory Permissions:** Ensure that proper permissions are set on sensitive files and directories to avoid unintended exposure.

3. **Regular Security Audits:** Periodically scan and audit the server for any unintentional directory or file exposure.
