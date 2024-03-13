import requests
api = "https://inv.nadeko.net/api/v1/videos/"


def get_video_description(video_id):
    res = requests.get(f"{api}{video_id}?fields=title,description&pretty=1")
    data = res.json()
    return data['description']

import csv
import json


with open('yt_links.json') as f:
    data = json.load(f)

with open('yt_links.csv', 'a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'link', 'description'])
    writer.writeheader()
    for x in data:
        title = x['title']
        link = "https://youtube.com" + x['url']
        description = get_video_description(x['url'].split('/watch?v=')[-1])
        writer.writerow({'title': title, 'link': link, 'description': description})