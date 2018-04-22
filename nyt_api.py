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

article_que = []
article = {'title': None, 'url': None, 'date': None, 'status': None}


for stories in data['results'][:7]:
    article['title'] = stories['title'].encode('utf-8')
    # title = title.encode('utf-8')
    article['url'] = stories['url']
    article['date'] = datetime.date.today()
    article['status'] = "Pending"
    article_que.append(article)



    # insta_req = urllib.request.Request(insta_url, insta_data)
    # insta_resp = urllib.request.urlopen(insta_req)
    # write_values(title, url, date, status)

    # print(resp_data)
