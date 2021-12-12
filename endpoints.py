from random import randint
import os
import requests

countries = ['us', 'gb', 'ng', 'za', 'ie']

def create_endpoint():
    country_code = countries[randint(0,4)]
    return "http://newsapi.org/v2/top-headlines?country={0}&apiKey={1}".format(country_code, os.environ.get("NEWS_API_KEY"))


def call_endpoint():
    endpoint = create_endpoint()
    response = requests.get(endpoint)
    return response.json()['articles'][randint(0,19)]
