import pytest
from constance import config


@pytest.fixture
def not_on_injured_list():
    """Set IS_INJURED config to False for testing."""
    original_value = config.IS_INJURED
    config.IS_INJURED = False
    yield config
    config.IS_INJURED = original_value


@pytest.fixture
def on_injured_list():
    """Set IS_INJURED config to True for testing."""
    original_value = config.IS_INJURED
    config.IS_INJURED = True
    yield config
    config.IS_INJURED = original_value


@pytest.fixture
def not_suspended():
    """Set IS_SUSPENDED config to False for testing."""
    original_value = config.IS_SUSPENDED
    config.IS_SUSPENDED = False
    yield config
    config.IS_SUSPENDED = original_value


@pytest.fixture
def suspended():
    """Set IS_SUSPENDED config to True for testing."""
    original_value = config.IS_SUSPENDED
    config.IS_SUSPENDED = True
    yield config
    config.IS_SUSPENDED = original_value
