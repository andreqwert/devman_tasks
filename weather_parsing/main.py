import requests


places = ['Лондон', 'аэропорт Шереметьево', 'Череповец']

payload = {
	'lang': 'ru',
	'n': '',
	'T': '',
	'q': '',
	'm': ''
}


for place in places:
	url_template = 'http://wttr.in/{}'
	url = url_template.format(place)
	response = requests.get(url, params=payload)
	response.raise_for_status()
	print(response.text)	