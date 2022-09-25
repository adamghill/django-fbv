from django.db import models


class FakeModel(models.Model):
    name: models.CharField = models.CharField(max_length=255)
    is_valid: models.BooleanField = models.BooleanField(default=False)
