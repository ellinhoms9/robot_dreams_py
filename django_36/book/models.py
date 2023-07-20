from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        db_table = 'book'
        unique_together = ('title', 'author')
