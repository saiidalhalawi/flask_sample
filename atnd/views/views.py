# -*- coding:utf-8 -*-

from flask import config, request, redirect, url_for, render_template, flash, Flask
from atnd import app
from atnd.model.projects import Event
import json
import datetime
import pprint
import sys
import requests

@app.route('/')
def top():
    """[FUNCTIONS]TOP画面のアクション
    """
    result = getLatestEvent()
    return render_template('index.html', latestEvents = result)

def getLatestEvent():
    """[FUNCTIONS]最新の勉強会を取得
    """
    app = Flask(__name__)

    d = datetime.datetime.today()

    url = 'http://api.atnd.org/events/'
    payload = {'ym': d.year+d.month, 'count': 10, 'format': 'json', 'keyword': 'UI/UX'}
    content = requests.get(url, params=payload).text

    return json.loads(content.encode('utf-8'))
