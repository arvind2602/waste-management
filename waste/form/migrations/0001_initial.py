# Generated by Django 4.1.7 on 2023-04-21 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.IntegerField()),
                ('donation', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
