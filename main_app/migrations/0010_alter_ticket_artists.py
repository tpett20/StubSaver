# Generated by Django 4.2 on 2023-04-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_ticket_artists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='artists',
            field=models.ManyToManyField(blank=True, to='main_app.artist'),
        ),
    ]
