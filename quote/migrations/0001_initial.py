# Generated by Django 2.2.12 on 2020-08-31 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('auther', models.CharField(max_length=250)),
                ('source', models.CharField(max_length=99, null=True)),
                ('rating', models.CharField(blank=True, max_length=99, null=True)),
            ],
        ),
    ]
