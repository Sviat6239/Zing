from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, null=True, verbose_name="Last Name")
    username = models.CharField(max_length=50, unique=True, verbose_name="Username")
    password = models.CharField(max_length=128, verbose_name="Password")
    bio = models.TextField(blank=True, null=True, verbose_name="Biography", max_length=10000)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Avatar")
    display_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Display Name")

    def __str__(self):
        return f"{self.get_display_name()} ({self.username})"

    def get_display_name(self):
        if self.display_name:
            return self.display_name
        return f"{self.first_name} {self.last_name}"
