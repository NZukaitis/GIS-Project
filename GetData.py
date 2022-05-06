import requests
import json

def getPlacesData(keyword, apiKey):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=42.684210%2C-73.848560&radius=5000&keyword=" + keyword + "&key=" + apiKey
    response = requests.request("GET", url, headers={}, data={})

    results = json.loads(response.content)

    with open("school.json", "w") as file:
        json.dump(results, file)