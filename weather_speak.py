from config import API_KEY
import requests
from gtts import gTTS
import os

CITY = "NARA"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ja"

response = requests.get(URL)
print(response.text)
data = response.json()
print(data)


weather = data['weather'][0]['description']
temp = data['main']['temp']

message = f"{CITY}の今日の天気は{weather}、気温は{int(temp)}度です"
print(message)


tts = gTTS(text=message, lang='ja')
tts.save("weather.mp3")
os.system("mpg123 weather.mp3")