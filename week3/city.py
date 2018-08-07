import sys
import pprint
import requests
from dateutil.parser import parse


class YahooWeatherForecast:

    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        if city in self._cached_data:
            return self._cached_data[city]
        url = f"https://query.yahooapis.com/v1/public/yql?q="\
              + f"select%20*%20from%20weather.forecast%20where%20w"\
              + f"oeid%20in%20(select%20woeid%20from%20geo.places("\
              + f"1)%20where%20text%3D%22{city}%22)%20and%20u%3D%2"\
              + f"7c%27&format=json&env=store%3A%2F%2Fdatatables.o"\
              + f"rg%2Falltableswithkeys"
        print("sending HTTP request")
        data = requests.get(url).json()
        forecast = []
        forecast_data = data["query"]["results"]["channel"]["item"]["forecast"]
        for day_data in forecast_data:
            forecast.append({
                "date": parse(day_data["date"]),
                "high_temp": int(day_data["high"])
            })
        self._cached_data[city] = forecast
        return forecast


class CityInfo:

    def __init__(self, city, forecast_provider=None):
        self.city = city
        self._forecast_provider = forecast_provider or YahooWeatherForecast()

    def weather_forecast(self):
        return self._forecast_provider.get(self.city)


def _main():
    weather_forecast = YahooWeatherForecast()
    for i in range(5):
        city = CityInfo(sys.argv[1])
        forecast = city.weather_forecast() # метод, который возвращает прогноз погоды
        pprint.pprint(forecast) # напечатаем прогноз красиво с помощью PrettyPrinter

if __name__ == "__main__":
    _main()
