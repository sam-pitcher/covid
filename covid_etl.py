import requests

url = "https://covid-19-data.p.rapidapi.com/help/countries"

querystring = {"format":"json"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "cc8f7ed957msh0e0a15d2d9e5e02p1eac75jsn47de024ae36c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)