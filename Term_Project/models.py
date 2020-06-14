from django.db import models

# Create your models here.


class Extinguisher(models.Model):
    num = models.IntegerField()
    location = models.CharField(max_length=200)
    local_num = models.IntegerField()
    last_check = models.TextField(max_length=8)
    fire_state = models.IntegerField()
    objects = models.Manager()
