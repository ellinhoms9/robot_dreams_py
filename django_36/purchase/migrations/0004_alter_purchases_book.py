# Generated by Django 4.2.3 on 2023-07-18 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_books_owner'),
        ('purchase', '0003_alter_purchases_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchases',
            name='book',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='book.books'),
        ),
    ]
