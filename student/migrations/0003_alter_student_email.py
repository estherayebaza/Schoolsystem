# Generated by Django 3.2.4 on 2021-07-30 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210730_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(default='estherayebaza@gmail.com', max_length=254),
        ),
    ]
