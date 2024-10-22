we noticed that there is an image is clickable in the home screen, after clicking it the url became "http://localhost/?page=media&src=nsa"
we tried to use xss by pass a script in src and its successfull sent, so its not protected but we didnt got the flag.

using the payloads "https://github.com/payloadbox/xss-payload-list" we tried it in burpsuit and found something in this line passing it as src="data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+" so there is something different in base64, we convert the simple script to base 64 "echo "<script>alert(1)</script>" | base64"


we put the output "PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pgo=" in that payload and we got the flag.