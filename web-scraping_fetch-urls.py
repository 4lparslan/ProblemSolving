# Fetching all urls starting with 'https' from a webpage

import requests
from bs4 import BeautifulSoup

url_list = []

input_file_name = "input.txt"
output_file = open('output.txt','w')
input_file = open(input_file_name, "r", encoding="utf-8")

for satir in input_file:
    url_list.append(satir.strip())

for url in url_list:
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	for link in soup.find_all('a'):
		href = link.get('href')
		if href and href.startswith('https'):
			href = href.lstrip()
			output_file.write(href)
			output_file.write('\n')
output_file.close()
input_file.close()