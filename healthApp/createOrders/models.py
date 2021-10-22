from django.db import models

# Create your models here.
class CreateOrderModel(models.Model):
    patient = models.CharField(max_length=255)
    medicine = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.patient} is  using {self.medicine}"
