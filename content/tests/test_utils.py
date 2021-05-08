import datetime
from content.utils import get_game_id, check_for_error, get_total_errors
from freezegun import freeze_time


@freeze_time("2021-04-24")
def test_get_game_id():
    today = datetime.datetime.now()
    print(today)
    game_id = get_game_id(135, today)
    assert game_id == 634361


def test_check_for_error_returns_yes_for_tatisjr():
    game_id = get_game_id(135, datetime.date(2021, 4, 24))
    error = check_for_error(game_id, "Tatis")
    assert error[0] == "Yes"
    assert error[1] == "#E35625"


def test_check_for_error_returns_no_for_tatisjr():
    game_id = get_game_id(135, datetime.date(2021, 5, 1))
    error = check_for_error(game_id, "Tatis")
    assert error[0] == "No"
    assert error[1] == "#FFC425"


def test_check_for_padres_game():
    game_id = get_game_id(135, datetime.date(2021, 5, 6))
    error = check_for_error(game_id, "Tatis")
    assert error[0] == "No"
    assert error[1] == "#FFC425"


def test_total_errors():
    # TODO: dynamically check the total number of errors
    total_errors = get_total_errors(665487)
    api_total_errors = 10
    assert total_errors == api_total_errors
