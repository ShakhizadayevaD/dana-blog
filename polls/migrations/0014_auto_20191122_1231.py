# Generated by Django 2.2.4 on 2019-11-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20191122_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='videofile',
            field=models.FileField(null=True, upload_to='posts/', verbose_name=''),
        ),
    ]
