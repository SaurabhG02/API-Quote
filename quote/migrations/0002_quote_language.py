# Generated by Django 2.2.12 on 2020-08-31 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='language',
            field=models.CharField(choices=[('en', 'En'), ('sr', 'Sr')], default='en', max_length=20),
        ),
    ]
