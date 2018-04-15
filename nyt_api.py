import urllib.request
import requests
import urllib.parse
import credentials


# NYT API REQUEST
nyt_api = "1907f8876c924723b11dc212ec92ad13"
nyt_url = "https://api.nytimes.com/svc/topstories/v2/home.json"


nyt_params = {'api-key': "1907f8876c924723b11dc212ec92ad13"}
nyt_url += "?api-key=" + str(nyt_api)
resp = requests.get(nyt_url)
data = resp.json()


# Insapaper API Request
insta_url = 'https://www.instapaper.com/api/add'
insta_params = {
    'username': credentials.instapaper_username,
    'password': credentials.instapaper_password,
    'url': ""
}

for stories in data['results'][4:5]:
    insta_params['url'] = stories['url']
    insta_data = urllib.parse.urlencode(insta_params)
    insta_data = insta_data.encode('utf-8')

    insta_req = urllib.request.Request(insta_url, insta_data)
    insta_resp = urllib.request.urlopen(insta_req)
