# Generated by Django 2.0.2 on 2018-03-04 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=250)),
                ('level', models.IntegerField()),
                ('occupants', models.CharField(max_length=250)),
            ],
        ),
    ]
