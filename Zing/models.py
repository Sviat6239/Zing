from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    username = models.CharField(max_length=50, unique=True, verbose_name="Username")
    password = models.CharField(max_length=128, verbose_name="Password")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
