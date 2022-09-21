from django.db import models


class Item(models.Model):
    class Meta:
        permissions = [
            ("download_csv", "Can download csv of all items")
        ]
    # An id is added automatically
    date = models.DateField(auto_now=True)
    name = models.CharField(max_length=50)
    txt1 = models.CharField(max_length=10)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    num3 = models.IntegerField()
