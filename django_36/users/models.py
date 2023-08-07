from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy


class Users(AbstractUser):
    first_name = models.CharField(null=False, max_length=50)
    last_name = models.CharField(null=False, max_length=50)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.first_name} User "

    class Meta:
        db_table = 'user'
        verbose_name = 'Site User'
        verbose_name_plural = 'Site Users'

    def get_absolute_url(self):
        return reverse_lazy('users:users_detail', kwargs={'pk': self.pk})
