import requests
import json

def getPlacesData():
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=42.684210%2C-73.848560&radius=5000&keyword=school&key=" + "AIzaSyCmHZ5a-6pYzfUO5c-Vnzh6buD_pZLQjkM"

    response = requests.request("GET", url, headers={}, data={})

    results = json.loads(response.content)
    print(results)

    with open("school.json", "w") as file:
        json.dump(results, file)

def parseData():
    with open("music_stores.json", "r") as file:
        data = json.load(file)
        for i in data['results']:
            print(i['name'])
            print(i['geometry']['location'])


#getPlacesData()
parseData()