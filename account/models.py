from django.db import models
from django.contrib.auth.models import User



class Account(User):
    wallet = models.PositiveIntegerField(default=1_000_000)

    def __str__(self):
        return f"{self.username} --- {self.wallet}"