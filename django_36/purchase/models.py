from django.db import models

from users.models import Users
from book.models import Books


class Purchases(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, default='')
    date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'purchase'
        ordering = ['-date']
