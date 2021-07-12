from django.db import models

# Create your models here.
class RemovalReg(models.Model):
    chittyName = models.CharField(max_length=200)
    chittalName = models.CharField(max_length=200)
    chittalNo   = models.IntegerField()
    removalDate = models.CharField(max_length=200)
    time        = models.CharField(max_length=200)

