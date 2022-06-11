from django.db import models
#
# # Create your models here.
class Director(models.Model):
    g = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    name = models.CharField(verbose_name='Director Name', max_length=30)
    age = models.IntegerField()
    gender = models.CharField(choices=g, max_length=6, default='M')

    def __str__(self):
        return self.name