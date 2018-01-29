#current position of international space station
location = requests.get("http://api.open-notify.org/iss-now.json")

#print status code of wiwitiss
print(location.status_code)

#pass in location parameters. NYC lat, lon.
parameters = {"lat": 40.71, "lon": -74}

#create request with parameters included.
location = requests.get("http://api.open-notify.org/iss-now.json", params = parameters)

#print response, data returned by server through API
print(location.content)

#determine number of astraunots in space
astronauts = requests.get("http://api.open-notify.org/astros.json")
astrosNumber = astronauts.json()

print(astrosNumber["number"])
