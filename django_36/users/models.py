from django.db import models


class Users(models.Model):
    first_name = models.CharField(null=False, max_length=50)
    last_name = models.CharField(null=False, max_length=50)
    age = models.IntegerField(null=False)

    class Meta:
        db_table = 'user'


