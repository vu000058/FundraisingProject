# Generated by Django 2.1.5 on 2019-03-07 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='event_due',
            field=models.DateField(null=True),
        ),
    ]
