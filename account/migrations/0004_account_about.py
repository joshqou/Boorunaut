# Generated by Django 2.0 on 2018-03-08 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180306_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='about',
            field=models.CharField(default=False, max_length=2500),
        ),
    ]
