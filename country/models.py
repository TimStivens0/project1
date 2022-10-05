from django.db import models

class CountryModel(models.Model):
    Country_Name = models.CharField(max_length=50)
    Country_Capital = models.CharField(max_length=50)
    Country_Currency = models.CharField(max_length=30)

    def __str__(self):
        return self.Country_Name