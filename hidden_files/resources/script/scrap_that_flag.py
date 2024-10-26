import requests 
from bs4 import BeautifulSoup
import sys
BASE_URL = "http://10.18.225.159/.hidden/"



def	main():
	scrap_one_layer(BASE_URL)


def	scrap_one_layer(url):
	response = requests.get(url)
	write_output_to_log_file(response.text)
	if "flag" in response.text:
		print("😎 found the flag")
		print(f"{response.text}")
		sys.exit(0)
	links, len_links = get_links_in_a_page(response.text)
	if len_links == 0:
		return 0
	for link in links:
		scrap_one_layer(url + link)


def	get_links_in_a_page(text):
	soup = BeautifulSoup(text, 'html.parser')
	
	un_parsed_links = soup.find_all("a")

	links = []
	for link in un_parsed_links:
		if  "../" in link or ".hidden" in link:
			continue
		links.append(link.get("href"))
	# sys.exit(1)
	return links, len(links)

def	write_output_to_log_file(output):
	with open("massive_data_scraped.log", "a") as f:
		f.write(output)
		# print(output)

if __name__ == "__main__":
	main()