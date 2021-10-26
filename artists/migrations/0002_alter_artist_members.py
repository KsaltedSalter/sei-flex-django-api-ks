# Generated by Django 3.2.8 on 2021-10-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='artists', to='artists.Member'),
        ),
    ]
