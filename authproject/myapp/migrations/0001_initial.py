# Generated by Django 4.2.6 on 2023-11-30 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usersignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fistname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
                ('number', models.BigIntegerField()),
            ],
        ),
    ]
