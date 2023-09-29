from django.db import models

class Stonk(models.Model):
    ticker_symbol = models.CharField(max_length=5)
    volume = models.BigIntegerField()

    def __str__(self):
        return self.ticker_symbol



