import pytest
from constance import config


@pytest.mark.django_db
def test_constance_config_not_on_injured_list(not_on_injured_list):
    """Test that IS_INJURED config can be set to False."""
    assert config.IS_INJURED is False


@pytest.mark.django_db
def test_constance_config_on_injured_list(on_injured_list):
    """Test that IS_INJURED config can be set to True."""
    assert config.IS_INJURED is True


@pytest.mark.django_db
def test_constance_config_player_not_suspended(not_suspended):
    """Test that IS_SUSPENDED config can be set to False."""
    assert config.IS_SUSPENDED is False


@pytest.mark.django_db
def test_constance_config_player_suspended(suspended):
    """Test that IS_SUSPENDED config can be set to True."""
    assert config.IS_SUSPENDED is True


@pytest.mark.django_db
def test_constance_config_defaults():
    """Test that Constance config has correct default values."""
    assert config.PLAYER_TEAM_ID == 135
    assert config.PLAYER_LAST_NAME == "Tatis Jr"
    assert config.COLOR_NO_ERROR == "#FFC425"
    assert config.COLOR_ERROR == "#E35625"
    assert config.MESSAGE_ERROR == "Yes"
    assert config.MESSAGE_NO_ERROR == "Not Yet"
    assert config.MESSAGE_NO_ERROR_INJURED == "Not Yet *"
