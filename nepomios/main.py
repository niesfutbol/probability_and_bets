import requests
from jinja2 import Environment, FileSystemLoader

from flask import Flask
from flask import render_template

def would_we_bet(match):
    bet = (match["home"] > 0.5) | (match["away"] > 0.5)
    return bet


def add_color(to_render):
    for match in to_render:
        match.update({"color": "#218038"}) if would_we_bet(match) else match.update(
            {"color": "#3aa0f3"}
        )
    return to_render



app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    conn = requests.get("https://rj2d6a.deta.dev")
    res = conn.json()
    to_render = res["response"]
    to_render_with_color = add_color(to_render)
    return render_template('index.html', matches=to_render_with_color)


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/<league>')
def league(league):
    return render_template(f"{league}.html")
