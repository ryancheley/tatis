import datetime

import pytest
from freezegun import freeze_time

from content.utils import (
    check_for_error,
    check_home_or_away,
    get_game_id,
    get_total_errors,
)


@freeze_time("2021-04-24")
def test_get_game_id():
    today = datetime.datetime.now()
    game_id = get_game_id(135, today)
    assert game_id == 634361


@pytest.mark.django_db
def test_check_for_error_returns_yes_for_tatisjr(not_on_injured_list):
    game_id = get_game_id(135, datetime.date(2021, 4, 24))
    error = check_for_error(game_id, "Tatis")
    assert error[0] == "Yes"
    assert error[1] == "#E35625"


@pytest.mark.django_db
def test_check_for_error_returns_no_for_tatisjr_not_on_il(not_on_injured_list):
    game_id = get_game_id(135, datetime.date(2021, 5, 1))
    error = check_for_error(game_id, "Tatis")
    assert error[0] == "Not Yet"
    assert error[1] == "#FFC425"


@pytest.mark.django_db
def test_check_for_padres_game_not_on_il(not_on_injured_list):
    game_id = get_game_id(135, datetime.date(2021, 5, 6))
    error = check_for_error(game_id, "Tatis")
    assert error[0] == "Not Yet"
    assert error[1] == "#FFC425"


@pytest.mark.django_db
def test_check_for_error_returns_no_for_tatisjr_on_il(on_injured_list):
    game_id = get_game_id(135, datetime.date(2021, 5, 1))
    error = check_for_error(game_id, "Tatis")
    assert error[0] == "Not Yet *"
    assert error[1] == "#FFC425"


@pytest.mark.django_db
def test_check_for_padres_game_on_il(on_injured_list):
    game_id = get_game_id(135, datetime.date(2021, 5, 6))
    error = check_for_error(game_id, "Tatis")
    assert error[0] == "Not Yet *"
    assert error[1] == "#FFC425"


@freeze_time("2022-12-31")
def test_total_errors():
    total_errors = get_total_errors(665487)
    assert total_errors == 0


def test_check_home_or_away_home():
    game_location = check_home_or_away(633544, 135)
    assert game_location == "home"


def test_check_home_or_away_away():
    game_location = check_home_or_away(634361, 135)
    assert game_location == "away"


def test_check_home_or_away_none():
    game_location = check_home_or_away(None, 135)
    assert game_location is None
