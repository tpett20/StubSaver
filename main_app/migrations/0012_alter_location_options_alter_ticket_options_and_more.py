# Generated by Django 4.2 on 2023-04-21 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_sportevent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='sportevent',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.ticket'),
        ),
    ]