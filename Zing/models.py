from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    username = models.CharField(max_length=50, unique=True, verbose_name="Username")
    password = models.CharField(max_length=128, verbose_name="Password")
    bio = models.TextField(blank=True, null=True, verbose_name="Biography")  # Biography field
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Avatar")  # Avatar field
    display_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Display Name")  # Display Name field

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    def save(self, *args, **kwargs):
        if not self.display_name:
            self.display_name = f"{self.first_name} {self.last_name}"  # Automatically set display name if not provided
        super(User, self).save(*args, **kwargs)
