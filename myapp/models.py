from django.db import models

# Create your models here.

class sos2(models.Model):
    La = models.TextField()

    def __str__(self):
        return self.La
