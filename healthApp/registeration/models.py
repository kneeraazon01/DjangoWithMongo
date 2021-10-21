from django.db import models

# Create your models here.


class RegisterModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
