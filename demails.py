import requests
import urllib
import json
from bs4 import BeautifulSoup

urls = ("http://dartmouth.edu/faculty-directory/department?dept=All&page=1", "http://dartmouth.edu/faculty-directory/department?dept=All")
url = requests.get(urls)

soup = BeautifulSoup(url.content)

name = soup.find_all("a", {"href":"/faculty-directory/"})

title = soup.find_all("li", {"class":"first last"})

email = soup.find_all("a","href":"mailto:")

for item in name:
	print name.text

for item in title:
	print title.text

for item in email:
	print email.text
	
