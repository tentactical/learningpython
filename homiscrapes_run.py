def homiparse_with_comments():
	import json, requests
	url='http://homicide.latimes.com/api/homicide/all/'
	resp = requests.get(url=url)
	data = json.loads(resp.text)
	with open("extraction.csv",'w') as f:
		for item in data['geojson']['features']:
			### this is orignal write statement
			### uncomment to reproduce the error
			#f.write(str(item['geometry']['coordinates'][0]) + ',' + str(item['geometry']['coordinates'][1]) + ',' + str(item['properties']['n'])+ ',' + str(item['properties']['r'])+ ',' + str(item['properties']['o'])+ ',' + str(item['properties']['ag'])+ ',' + str(item['properties']['g'])+ '\n')

			### the following is what I have working
			### the try/except is hard to follow at first and is kind
			### of beside the point. but the program was crashing on an
			### error due to text encoding mismatch, and this is the most
			### efficient way to handle it and keep moving
			try:
				## uncomment this line to print to screen rather
				## than write to file
				#print(str(item['geometry']['coordinates'][0]) + ',' + str(item['geometry']['coordinates'][1]) + ',' + str(item['properties']['n'])+ ',' + str(item['properties']['r'])+ ',' + str(item['properties']['o'])+ ',' + str(item['properties']['ag'])+ ',' + str(item['properties']['g'])+ '\n')
				f.write(str(item['geometry']['coordinates'][0]) + ',' + str(item['geometry']['coordinates'][1]) + ',' + str(item['properties']['n'])+ ',' + str(item['properties']['r'])+ ',' + str(item['properties']['o'])+ ',' + str(item['properties']['ag'])+ ',' + str(item['properties']['g'])+ '\n')

			except UnicodeEncodeError:
				print "No good encoding error"

def homiparse():
	print "Method homiparse() executing"
	import json, requests
	url='http://homicide.latimes.com/api/homicide/all/'
	resp = requests.get(url=url)
	data = json.loads(resp.text)
	with open("extraction.csv",'w') as f:
		for item in data['geojson']['features']:
			try:
				f.write(str(item['geometry']['coordinates'][0]) + ',' + str(item['geometry']['coordinates'][1]) + ',' + str(item['properties']['n'])+ ',' + str(item['properties']['r'])+ ',' + str(item['properties']['o'])+ ',' + str(item['properties']['ag'])+ ',' + str(item['properties']['g'])+ '\n')

			except UnicodeEncodeError:
				print "No good encoding error"
	print "Method homiparse() finished"


if __name__=="__main__":
	print "The init script is calling homiparse()."
	homiparse()
	print "Call to homiparse() complete"
