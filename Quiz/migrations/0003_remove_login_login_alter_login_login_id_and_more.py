# Generated by Django 4.1.4 on 2022-12-22 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='login',
        ),
        migrations.AlterField(
            model_name='login',
            name='Login_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='login',
            name='Password',
            field=models.CharField(max_length=100),
        ),
    ]