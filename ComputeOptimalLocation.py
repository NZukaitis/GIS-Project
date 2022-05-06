from math import *
import json

def distanceDegreesToMeters(lat1, long1, lat2, long2):
    #https://en.wikipedia.org/wiki/Great-circle_distance
    #formula used:
    #https://stackoverflow.com/questions/639695/how-to-convert-latitude-or-longitude-to-meters

    RADIUS = 6378.137 #WGS-84 Earth equatorial radius (km)

    deltaLat = (lat2 * pi / 180) - (lat1 * pi / 180)
    deltaLong = (long2 * pi / 180) - (long1 * pi * 180)

    a = pow(sin(deltaLat/2),2) + (cos(lat1 * pi/180) * cos(lat2 * pi/180) * pow(sin(deltaLong/2), 2))

    c = 2 * atan2(sqrt(a), sqrt(1-a))
    
    d = RADIUS * c

    return d * 1000

def weightDistance(distance):
    return (-1 * log(distance -10)) + 6.9

def calcWeight(lat, long):
    minBarWeight = 11 #max value for {@code weightDistance(distance)} is 10
    minMusWeight = -100 #there is no min value for {@code weightDistance(distance)}, so this should probably work for something that's guarenteed to be < first store
    minSchoolWeight = 11
    with open("bars.json", "r") as file:
        data = json.load(file)
        for i in data["results"]:
            currentLat = float(i["geometry"]["location"]["lat"])
            currentLng = float(i["geometry"]["location"]["lng"])

            temp = weightDistance(distanceDegreesToMeters(lat, long, currentLat, currentLng))

            if temp < minBarWeight:
                minBarWeight = temp
    
    with open("music_stores.json", "r") as file:
        data = json.load(file)
        for i in data["results"]:
            currentLat = float(i["geometry"]["location"]["lat"])
            currentLng = float(i["geometry"]["location"]["lng"])

            temp = weightDistance(distanceDegreesToMeters(lat, long, currentLat, currentLng))

            if temp > minMusWeight:
                minMusWeight = temp
    

    with open("school.json", "r") as file:
        data = json.load(file)
        for i in data["results"]:
            currentLat = float(i["geometry"]["location"]["lat"])
            currentLng = float(i["geometry"]["location"]["lng"])

            temp = weightDistance(distanceDegreesToMeters(lat, long, currentLat, currentLng))

            if temp < minSchoolWeight:
                minSchoolWeight = temp

    return minMusWeight - minBarWeight - minSchoolWeight #theoretical max should be 10


print(calcWeight(42.684210, -73.848560)) #coordinates entered are the center of the area used in {@code GetData.py}
