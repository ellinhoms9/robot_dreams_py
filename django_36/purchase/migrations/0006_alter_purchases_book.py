# Generated by Django 4.2.3 on 2023-07-18 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_books_unique_together'),
        ('purchase', '0005_alter_purchases_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchases',
            name='book',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='book.books'),
        ),
    ]
