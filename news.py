import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("News for today")
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=33f86e11adc14a498f219e480093712b"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']

    for article in arts:
        speak(article['title'])
        speak("moving to next")

    