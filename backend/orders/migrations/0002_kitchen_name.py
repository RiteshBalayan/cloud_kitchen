# Generated by Django 5.0.1 on 2024-02-06 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen',
            name='name',
            field=models.TextField(blank=True),
        ),
    ]