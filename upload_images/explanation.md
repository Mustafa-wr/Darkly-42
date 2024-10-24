# Upload Page Exploitation

During our testing on the upload page, we attempted to upload images in various formats, but the server rejected all of them. We further experimented with file types, including `.js` and `.php`, but to no avail. Eventually, we discovered that the server accepted files with the `.php.jpeg` extension.

Despite successfully uploading the file, we initially did not receive any flag. To further investigate, we executed a POST request using `curl` with the following command:

```bash
curl -X POST -H 'Content-Type: multipart/form-data' --form 'Upload=Upload' --form 'uploaded=@m.php.jpeg;type=image/jpeg' http://localhost/?page=upload

After executing this command, we successfully retrieved the flag.

The flag is: 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8