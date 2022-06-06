from django.db import models
from actor.models import Actor
# Create your models here.
class Movie(models.Model):
    name = models.CharField(verbose_name='Movie Name',max_length=30)
    production_year = models.IntegerField()
    creation_time = models.DateField()
    actor = models.ManyToManyField(Actor, verbose_name='Actor Name',related_name='actor')
    update_time = models.DateField(auto_now=True)


    def __str__(self):
        return f'actors :  {self.name}'









