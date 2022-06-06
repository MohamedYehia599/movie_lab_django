# Generated by Django 4.0.5 on 2022-06-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Movie Name')),
                ('production_year', models.IntegerField()),
                ('creation_time', models.DateField()),
                ('update_time', models.DateField(auto_now=True)),
                ('actor', models.ManyToManyField(to='actor.actor', verbose_name='Actor Name')),
            ],
        ),
    ]