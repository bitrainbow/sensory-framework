import pyowm

api_key = '7b8fdaadb74b57cc2efa4e79869990dc'

def configure_weather_interface():
    owm = pyowm.OWM(api_key)
    return owm

def update_data(owm):
    observation = owm.weather_at_place('London,uk')
    w = observation.get_weather()
    return w



