# Generated by Django 4.1.4 on 2022-12-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Login_id', models.TextField(blank=True, max_length=50)),
                ('Password', models.TextField(blank=True, max_length=40)),
                ('login', models.BooleanField(error_messages='wrong')),
            ],
        ),
    ]