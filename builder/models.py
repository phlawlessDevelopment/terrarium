from django.db import models

# Create your models here.

class Jar3DModel(models.Model):
    model_name = models.CharField(max_length=16)
    file = models.FileField()

    def __str__(self) -> str:
        return f'{self.model_name}'
