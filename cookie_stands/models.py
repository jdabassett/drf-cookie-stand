from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import random


class CookieStand(models.Model):
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(blank=True)
    hourly_sales = models.JSONField(default=list, blank=True, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('cookie_stand_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        print("save triggered", self.minimum_customers_per_hour, self.maximum_customers_per_hour, self.average_cookies_per_sale)
        if not self.hourly_sales:
            min = self.minimum_customers_per_hour
            max = self.maximum_customers_per_hour

            cookies_each_hour = []
            for _ in range(14):
                new = int(random.randint(min,max))*self.average_cookies_per_sale
                cookies_each_hour.append(new)

            self.hourly_sales = cookies_each_hour

        super().save(*args, **kwargs)

