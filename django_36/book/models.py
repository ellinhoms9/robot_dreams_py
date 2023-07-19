from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.FloatField()

    class Meta:
        db_table = 'book'
        unique_together = ('title', 'author')
