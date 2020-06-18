from requests import get
from bs4 import BeautifulSoup
import json

weather_url = 'http://api.openweathermap.org/data/2.5/weather'
weather_params = {
    'q': 'Mogilev',
    'APPID': '141f807b628115f29a5b9d08f17e7171',
    'mode': 'xml',
    'units': 'metric'
}
weather_params2 = weather_params.copy()
weather_params2['mode'] = 'json'
rest = get(weather_url, weather_params)
rest2 = get(weather_url, weather_params2)
soup = BeautifulSoup(rest.content, 'xml')
print(soup.temperature['value'])
print(rest2.json()['main']['temp'])