from pydantic import BaseModel
import json
from jinja2 import Environment, FileSystemLoader

class Match_Round(BaseModel):
    id_home: int
    id_away: int
    round: str

fileLoader = FileSystemLoader("template")
env = Environment(loader = fileLoader)
matches = [{
    "home_name": "Liverpool",
    "home_id": 40,
    "prob_home": "59 %",
    "prob_away": "19 %",
    "prob_draw": "12 %",
    "bet_home": "1.90",
    "bet_away": "3.90",
    "bet_draw": "3.60",
    "away_name": "Porto",
    "away_id": 212,
  },
  {
    "home_name": "Man City",
    "home_id": 50,
    "prob_home": "67 %",
    "prob_away": "14 %",
    "prob_draw": "19 %",
    "bet_home": "1.60",
    "bet_away": "4.33%",
    "bet_draw": "5.00%",
    "away_name": "PSG",
    "away_id": 85,
  },
  {
    "home_name": "Atl. Madrid",
    "home_id": 530,
    "prob_home": "67 %",
    "prob_away": "14 %",
    "prob_draw": "19 %",
    "bet_home": "1.61",
    "bet_away": "3.80",
    "bet_draw": "5.50",
    "away_name": "Milan",
    "away_id": 489,
  },]

rendered = env.get_template("index.html").render(matches = matches)
print(rendered)