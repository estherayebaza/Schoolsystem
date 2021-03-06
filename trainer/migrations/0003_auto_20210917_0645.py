# Generated by Django 3.2.5 on 2021-09-17 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0002_alter_trainer_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='bank_account',
            field=models.CharField(blank='true', max_length=30, null='true'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='contract',
            field=models.CharField(blank='true', max_length=30, null='true'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='courses_taught',
            field=models.CharField(blank='true', max_length=30, null='true'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='cv',
            field=models.FileField(blank='true', null='true', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='email',
            field=models.EmailField(blank='true', max_length=254, null='true'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='first_name',
            field=models.CharField(blank='true', max_length=10, null='true'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='image',
            field=models.ImageField(blank='true', null='true', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='last_name',
            field=models.CharField(blank='true', max_length=10, null='true'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='lessons_attended',
            field=models.PositiveSmallIntegerField(blank='true', null='true'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='profession',
            field=models.CharField(blank='true', max_length=200, null='true'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='trainer_Id',
            field=models.CharField(blank='true', max_length=20, null='true'),
        ),
    ]
