import requests
import json

url = "http://www.bbc.co.uk/radio1/playlist.json"

def get_titles(fn, loop):
    titles = []
    data = json.loads(requests.get(url).text)
    for list_key in data['playlist']:
        record = data['playlist'][list_key][0]
        titles.append(record['title'])
    loop.call_soon( fn, loop, titles )


