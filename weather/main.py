import requests

from celery import Celery
from celery.schedules import crontab


app = Celery(
    "weather_client",
    broker='redis://redis:6379/0',
    backend="redis://localhost:6379/0"
)

api_key = '21d28203d48477baaff6b52a03c7c297'


class WeatherClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = (
            "https://api.openweathermap.org/data/2.5/weather?q={},kg&appid={}"
        )

    def get_weather(self, city='Bishkek'):
        url = self.base_url.format(city, self.api_key)
        response = requests.get(url)
        if response.status_code == 200:
            data = requests.json()
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            print(
                f'''
                    Температура в Бишкеке равна {temperature:.1f} 
                    градусов Цельсия. Погода сейчас: {weather_description}
                '''
            )
        else:
            print(f'Error {response.status_code}: Ошибка при получении данных.')

    @app.task
    def request_daily_weather(self):
        self.get_weather()

    def run_daily(self):
        app.conf.beat_schedule = {
            'request_daily_weather': {
                'task': 'WeatherClient.request_daily_weather',
                # 'schedule': crontab(hour=4, minute=52)
                # 'schedule': crontab(minute='*')
                "schedule": crontab(minute="*/10"),
            }
        }
        app.conf.timezone = 'Asia/Bishkek'
        app.conf.result_backend = "redis://localhost"
        app.conf.broker_url = "redis://redis//"
        app.worker_main(["beat", '-l', 'INFO'])


if __name__ == '__main__':
    client = WeatherClient(api_key)
    client.run_daily()
