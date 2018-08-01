import json
import urllib.request

echo = urllib.request.urlopen('https://codeclubprojects.org/en-GB/python/iss/')
iss = json.loads(echo.read())
print('\n')
print('There are currently', iss['number'], 'people on the ISS.')
print('\n')
people = iss['people']
print('Individuals currently on ISS:')
for i in people:
    print('     ' + i['name'])

print('\n')

loc = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
iss_loc = json.loads(loc.read())
iss_location = iss_loc['iss_position']
iss_lo = iss_location['longitude']
iss_la = iss_location['latitude']
print('Longitude of ISS: ', iss_lo)
print('Latitude of ISS:  ', iss_la)
