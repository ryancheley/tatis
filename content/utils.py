import datetime

import requests
import statsapi

from .models import InjuredList


def check_home_or_away(game_id: int, team_id: int):
    try:
        away_team_id = statsapi.boxscore_data(game_id).get("away").get("team").get("id")
        if away_team_id == team_id:
            return "away"
        else:
            return "home"
    except requests.exceptions.HTTPError:
        return None


def check_for_error(game_id: int, player_last_name: str):
    is_injured = InjuredList.objects.last()
    if is_injured.is_injured:
        did_an_error_happen = "Not Yet *"
    else:
        did_an_error_happen = "Not Yet"
    display_color = "#FFC425"
    url = f"https://statsapi.mlb.com/api/v1.1/game/{game_id}/feed/live"
    response = requests.get(url)
    game = response.json()
    team_location = check_home_or_away(game_id, 135)

    try:
        info = game.get("liveData").get("boxscore").get("teams").get(team_location).get("info")
        for i in info:
            if i.get("title") == "FIELDING":
                fielding = i.get("fieldList")
                for item in fielding:
                    if item.get("label") == "E":
                        errors = item.get("value").split("; ")
                        for error in errors:
                            if player_last_name in error:
                                did_an_error_happen = "Yes"
                                display_color = "#E35625"
    except AttributeError:
        pass
    return did_an_error_happen, display_color


def get_game_id(team_id: int, game_date: datetime) -> int:
    game_date = game_date.strftime("%Y-%m-%d")
    try:
        game_id = statsapi.schedule(date=game_date, team=team_id, sportId=1)[0].get("game_id")
    except IndexError:
        game_id = None
    return game_id


def get_total_errors(player_id):
    fielding_stats = statsapi.player_stat_data(player_id, group="[fielding]", type="[season]")
    try:
        total_errors = fielding_stats.get("stats")[0].get("stats").get("errors")
    except IndexError:
        total_errors = 0
    return total_errors
