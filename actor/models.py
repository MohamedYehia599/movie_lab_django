from django.db import models


class Actor(models.Model):
    g = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = models.CharField(verbose_name='Actor Name', max_length=30)
    gender = models.CharField(choices=g,max_length=6 ,default='M')
    picture = models.ImageField(upload_to='actor')

    def __str__(self):
        return self.name