# Generated by Django 4.2.3 on 2023-07-18 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_books_owner'),
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchases',
            name='book',
        ),
        migrations.AddField(
            model_name='purchases',
            name='book',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.books'),
        ),
    ]