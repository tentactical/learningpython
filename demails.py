import requests
import urllib
import json
from bs4 import BeautifulSoup

#urls = ("http://dartmouth.edu/faculty-directory/department?dept=All&page=1", "http://dartmouth.edu/faculty-directory/department?dept=All")
url_base = "http://dartmouth.edu/faculty-directory/department?dept=All&page="


email_list = []

f = open('parsed_output.txt', 'w')

max_pages = 50 # set this accordingly
i=1

while i<max_pages:
	url = url_base + str(i)
	i = i + 1
	html = requests.get(url)
	soup = BeautifulSoup(html.content)

	for e in soup.select('a[href^=mailto]'):
		parsed_email = e.getText()
		email_list.append(parsed_email)
		f.write(parsed_email + ',\n')
	
print "extracted " + str(len(email_list)) + " emails"

f.close()
