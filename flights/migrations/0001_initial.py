# Generated by Django 4.2.2 on 2023-07-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=64)),
                ('destinaion', models.CharField(max_length=64)),
                ('duration', models.IntegerField()),
            ],
        ),
    ]