def homiparse():
	import json, requests
	url='http://homicide.latimes.com/api/homicide/all/'
	resp = requests.get(url=url)
	data = json.loads(resp.text)
	with open("extraction.csv",'w') as f:
		for item in data['geojson']['features']:
			f.write(str(item['geometry']['coordinates'][0]) + ',' + str(item['geometry']['coordinates'][1]) + ',' + str(item['properties']['n'])+ ',' + str(item['properties']['r'])+ ',' + str(item['properties']['o'])+ ',' + str(item['properties']['ag'])+ ',' + str(item['properties']['g'])+ '\n')


