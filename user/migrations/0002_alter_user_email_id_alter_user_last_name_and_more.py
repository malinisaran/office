# Generated by Django 4.0.3 on 2022-05-31 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Email_id',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='Last_Name',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='Mobile_Number',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='Password',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_Name',
            field=models.CharField(max_length=4),
        ),
    ]
