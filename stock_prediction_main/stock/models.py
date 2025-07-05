

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional: link to user
    ticker = models.CharField(max_length=10)
    predicted_price = models.FloatField()
    mse = models.FloatField()
    rmse = models.FloatField()
    r2 = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticker} - {self.predicted_price} on {self.created_at.strftime('%Y-%m-%d')}"
