import pytest


@pytest.mark.django_db
def test_string_representation_employee_not_on_injured_list(not_on_injured_list):
    assert str(not_on_injured_list) == "False"


@pytest.mark.django_db
def test_string_representation_employee_on_injured_list(on_injured_list):
    assert str(on_injured_list) == "True"


@pytest.mark.django_db
def test_string_representation_player_not_suspended(not_suspended):
    assert str(not_suspended) == "False"


@pytest.mark.django_db
def test_string_representation_player_suspended(suspended):
    assert str(suspended) == "True"
