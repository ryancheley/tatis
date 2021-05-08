import requests
import datetime
import statsapi


def check_for_error(game_id: int, player_last_name: str):
    did_an_error_happen = "No"
    display_color = "#FFC425"
    url = f"https://statsapi.mlb.com/api/v1.1/game/{game_id}/feed/live"
    response = requests.get(url)
    game = response.json()
    try:
        info = game.get("liveData").get("boxscore").get("teams").get("away").get("info")
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
    total_errors = fielding_stats.get("stats")[0].get("stats").get("errors")
    return total_errors
