import pytest

from content.models import InjuredList, SuspendedList


@pytest.fixture
def not_on_injured_list():
    InjuredList.objects.get_or_create(is_injured=False)
    is_injured = InjuredList.objects.all()[0]
    return is_injured


@pytest.fixture
def on_injured_list():
    InjuredList.objects.get_or_create(is_injured=True)
    is_injured = InjuredList.objects.all()[0]
    return is_injured


@pytest.fixture
def not_suspended():
    SuspendedList.objects.get_or_create(is_suspended=False)
    is_suspended = SuspendedList.objects.all()[0]
    return is_suspended


@pytest.fixture
def suspended():
    SuspendedList.objects.get_or_create(is_suspended=True)
    is_suspended = SuspendedList.objects.all()[0]
    return is_suspended
