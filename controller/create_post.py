import random
from time import sleep
import requests
import json

from .zombie import zombie

API_KEY = "f9470565aafc345a48a32f0bc8f7431cc364d63ad83fb05867794de828b70c6d"


def create_post(title, post):
    username = random.choice(zombie)
    url = "https://uzaii.com/posts.json?api_key=%s&&api_username=%s" % (API_KEY, username)
    payload = {
        "title": title,
        "raw": post
    }
    response = requests.post(url, payload)
    data = json.loads(response.text)
    code = response.status_code
    if code == 200:
        return True, "发帖成功" \
                     "<a href=\"https://uzaii.com/t/topic/%s\">%s</a>"%(data['topic_id'], title)
    else:
        return False, data['errors']
