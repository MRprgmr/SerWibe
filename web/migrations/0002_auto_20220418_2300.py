# Generated by Django 3.2.12 on 2022-04-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='printer',
            field=models.CharField(default=0, max_length=250, verbose_name='Printer'),
            preserve_default=False,
        ),
    ]
