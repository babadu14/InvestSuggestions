from django.db import models

# Create your models here.
class CryptoPrice(models.Model):
    coin = models.CharField(max_length=20)
    timestamp = models.DateTimeField(null=True, blank=True)
    price = models.FloatField()
    class Meta:
        unique_together = ('coin', 'timestamp')
