import csv
from nyt_api import article_que
import urllib.request
import requests
import urllib.parse
import credentials
import datetime
from log import write_values


# Insapaper API Request
insta_url = 'https://www.instapaper.com/api/add'
insta_params = {
    'username': credentials.instapaper_username,
    'password': credentials.instapaper_password,
    'url': ""
}


# print(len(article_que))
my_file = open('/Users/baker/Code/Python/gmail_instapaper/log_file.csv', 'a')


for article in article_que:
    insta_params['url'] = article['url']
    insta_data = urllib.parse.urlencode(insta_params)
    insta_data = insta_data.encode('utf-8')
    insta_req = urllib.request.Request(insta_url, insta_data)
    insta_resp = urllib.request.urlopen(insta_req)
    resp_data = insta_resp.read()
    article['status'] = resp_data

with my_file:
    my_fields = ['title', 'url', 'date', 'status']
    writer = csv.DictWriter(my_file, fieldnames=my_fields)
    # writer.writeheader()
    for article in article_que:
        writer.writerow(article)

