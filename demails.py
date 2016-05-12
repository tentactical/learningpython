#load proper libraries
import requests
import urllib
from bs4 import BeautifulSoup

#tell python to read the faculty directory page
urls = ("http://dartmouth.edu/faculty-directory/department?dept=All&page=1", "http://dartmouth.edu/faculty-directory/department?dept=All")
url = requests.get(urls)

#organize and read the content
soup = BeautifulSoup(url.content)
g_data = soup.find_all("div", {"class": "content"})

#print each entry
for item in g_data:
	print item.text
url = requests.get(urls)

