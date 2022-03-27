from django.db import models


class InjuredList(models.Model):
    """
    InjuredList model
    """

    is_injured = models.BooleanField(default=False)

    def __str__(self):
        return str(self.is_injured)
