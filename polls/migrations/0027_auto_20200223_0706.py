# Generated by Django 2.2.4 on 2020-02-23 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_auto_20200223_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberofvideos',
            name='name',
            field=models.CharField(blank=True, default=None, help_text='number', max_length=500, null=True),
        ),
    ]
