import pytest

from content.models import InjuredList


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
