import requests


places = ['Лондон', 'аэропорт Шереметьево', 'Череповец']

for article_id in places:
	url_template = 'http://wttr.in/{}?nTqm&lang=ru'
	url = url_template.format(article_id)
	response = requests.get(url)
	response.raise_for_status()
	print(response.text)
