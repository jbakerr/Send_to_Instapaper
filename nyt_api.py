import urllib.request
import requests
import urllib.parse
import credentials
import datetime
from log import write_values


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

for stories in data['results'][:5]:
    title = stories['title']
    title = title.encode('utf-8')
    url = stories['url']
    date = datetime.date.today()
    status = "ok"
    insta_params['url'] = stories['url']
    insta_data = urllib.parse.urlencode(insta_params)
    insta_data = insta_data.encode('utf-8')
    insta_req = urllib.request.Request(insta_url, insta_data)
    insta_resp = urllib.request.urlopen(insta_req)
    write_values(title, url, date, status)

    # resp_data = insta_resp.read()
    # print(resp_data)
