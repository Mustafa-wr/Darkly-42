in the uplaod page, we tried to upload an image with all of formats, and it dos not accept any of them, we tried also the .js and .php, till we found that its accepting the .php.jpeg file format, but still there was no flag, we make a post method using curl in this command 
"curl -X POST -H 'Content-Type: multipart/form-data' --form 'Upload=Upload' --form 'uploaded=@m.php.jpeg;type=image/jpeg' http://localhost/?page=upload"

and we got the flag

The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8