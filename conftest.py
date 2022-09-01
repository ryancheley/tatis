import pytest

from content.models import InjuredList, SuspendedList


@pytest.fixture
def not_on_injured_list():
    InjuredList.objects.create(is_injured=False)
    is_injured = InjuredList.objects.get(pk=1)
    return is_injured


@pytest.fixture
def on_injured_list():
    InjuredList.objects.create(is_injured=True)
    is_injured = InjuredList.objects.get(pk=1)
    return is_injured


@pytest.fixture
def not_suspended():
    SuspendedList.objects.create(is_suspended=False)
    is_suspended = SuspendedList.objects.get(pk=1)
    return is_suspended


@pytest.fixture
def suspended():
    SuspendedList.objects.create(is_suspended=True)
    is_suspended = SuspendedList.objects.get(pk=1)
    return is_suspended
