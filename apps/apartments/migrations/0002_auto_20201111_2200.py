# Generated by Django 3.1.1 on 2020-11-12 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]