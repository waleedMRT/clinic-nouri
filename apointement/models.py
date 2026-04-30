from django.db import models


class Apointement(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.first_name} | {self.date}"

# Create your models here.
