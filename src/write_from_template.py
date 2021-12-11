import pandas as pd
from pydantic import BaseModel
import json
from jinja2 import Environment, FileSystemLoader


def would_we_bet(match):
    bet = (match["home"] > 0.5) | (match["away"] > 0.5)
    return bet


def add_color(to_render):
    for match in to_render:
        match.update({"color": "#218038"}) if would_we_bet(match) else match.update(
            {"color": "#3aa0f3"}
        )
    return to_render


class Match_Round(BaseModel):
    id_home: int
    id_away: int
    round: str


path_1 = "tests/data/bets_39_2021_16.csv"
path_2 = "tests/data/predictions_39_2021_16.csv"
bets = pd.read_csv(path_1)
predicionts = pd.read_csv(path_2)
matches = bets.join(predicionts.set_index("id_match"), on="id_match")
to_render = [matches.iloc[i, :].to_dict() for i in range(len(matches))]
to_render_with_color = add_color(to_render)
fileLoader = FileSystemLoader("template")
env = Environment(loader=fileLoader)

rendered = env.get_template("index.html").render(matches=to_render_with_color)
print(rendered)
