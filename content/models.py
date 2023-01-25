from django.db import models


class InjuredList(models.Model):
    """
    InjuredList model
    """

    is_injured = models.BooleanField(default=False)

    def __str__(self):
        return str(self.is_injured)


class SuspendedList(models.Model):
    """
    Is he a cheater?
    """

    is_suspended = models.BooleanField(default=True)

    def __str__(self):
        return str(self.is_suspended)
