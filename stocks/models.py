from django.db import models

class UserStock(models.Model):
    ticker_symbol = models.CharField(max_length=5)
    date_selected = models.DateField(auto_now=True)

    def __str__(self):
        return self.ticker_symbol




