from django.db import models

from users.models import Users
from book.models import Books


class Purchases(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, default='')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.user.first_name} buy {self.book.title}"

    class Meta:
        db_table = 'purchase'
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'
        ordering = ['-date']
