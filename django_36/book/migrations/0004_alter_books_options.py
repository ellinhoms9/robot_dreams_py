# Generated by Django 4.2.3 on 2023-08-22 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_books_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
    ]
