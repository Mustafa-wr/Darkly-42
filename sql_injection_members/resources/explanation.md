# SQL Injection Exploitation on Search Members Page

## Description
This vulnerability involved performing a SQL injection on the search members page to extract sensitive information from the database. By utilizing generic union select payloads, we were able to manipulate the SQL query and retrieve data from the `users` table.

## Steps to Exploit
1. **Initial Payload Submission:**
   - We began by testing generic union select payloads from the SQL injection payload list found at [PayloadBox](https://github.com/payloadbox/sql-injection-payload-list).
   - We submitted the input `5 UNION ALL SELECT 1` but received an "incorrect number of columns" error.

2. **Refining the Payload:**
   - To resolve the column count issue, we modified our input to `5 UNION ALL SELECT 1, 2`, which successfully bypassed the error.

3. **Extracting Table Information:**
   - Utilizing the `information_schema`, we crafted a query to reveal table and column names using the payload: 
     ```
     5 UNION SELECT 1, CONCAT(table_name, 1000001, column_name) FROM information_schema.columns
     ```
   - This query returned a table called `users`, which contained the following columns: `username`, `password`, `user_id`, `first_name`, `last_name`, `town`, `country`, and `planet`.

4. **Retrieving User Data:**
   - We then executed a command to retrieve all values from the `users` table using the payload:
     ```
     5 UNION SELECT 1, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign) FROM users
     ```
   - This query provided the following output:
     - **ID:** 5 UNION SELECT 1, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign) FROM users 
     - **First Name:** 1
     - **Surname:** 5FlagGetThe424242

5. **Decrypting the Password:**
   - The password obtained from the output was "5FlagGetThe424242." We converted it to lowercase and applied the SHA-256 hashing algorithm, resulting in the final hash:
     ```
     5ff9d0165b4f92b14994e5c685cdce28
     ```

## Impact
This SQL injection vulnerability can lead to serious consequences, including:

- **Data Breach:** Unauthorized access to sensitive user information such as passwords and personal details.
  
- **System Compromise:** Exploitation of the vulnerability could allow attackers to manipulate or delete data, potentially affecting the integrity of the entire database.

- **Loss of Trust:** Users may lose confidence in the security of the application if they are aware that their personal data is at risk.

## Mitigation
1. **Parameterized Queries:** Implement prepared statements and parameterized queries to prevent SQL injection attacks by ensuring that user input is treated as data, not executable code.

2. **Input Validation:** Conduct thorough input validation to ensure that only expected values are processed by the application.

3. **Access Controls:** Enforce strict access controls on database queries to limit the information exposed to users, especially in public-facing applications.
