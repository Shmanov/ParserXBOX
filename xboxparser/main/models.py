from django.db import models
from datetime import datetime


class Game(models.Model):
    id = models.CharField(primary_key=True, serialize=False, verbose_name='ID', max_length=12)
    name = models.CharField('Name Product', max_length=100)
    rating_ms = models.IntegerField('Rating MS', default=0)
    now_on_sale = models.BooleanField('Now on Sale', default=False)
    rating_gavimo = models.IntegerField('Rating Gavimo', default=0)
    rating_eneba = models.IntegerField('Rating Eneba', default=0)
    total_rating = models.IntegerField('Total Rating', default=0)
    game_sale = models.BooleanField('Game Sale', default=False)
    date_end_sale = models.DateTimeField('Date End Sale', default=datetime.now())
    first_price = models.FloatField('First Price', default=0)
    first_region = models.CharField('First Region', max_length=100)
    second_price = models.FloatField('Second Price', default=0)
    second_region = models.CharField('Second Region', max_length=100)
    difference = models.FloatField('Difference', default=0)
    buy = models.BooleanField('BUY',default= False)


    def __str__(self):
        return self.name



