# Generated by Django 5.0.1 on 2024-02-06 23:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('recipe', models.TextField()),
                ('is_verified', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('total_orders', models.IntegerField()),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='core.chef')),
                ('photos', models.ManyToManyField(blank=True, related_name='dishes', to='core.photo')),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitchens', to='core.chef')),
                ('photos', models.ManyToManyField(blank=True, related_name='kitchens', to='core.photo')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ready_at', models.DateTimeField()),
                ('quantity', models.PositiveIntegerField()),
                ('delivery_method', models.CharField(choices=[('Delivery', 'Delivery'), ('Collect', 'Collect')], default='Delivery', max_length=10)),
                ('delivery_radius', models.FloatField()),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='orders.dish')),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='orders.kitchen')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_customer_delivered', models.BooleanField(default=False)),
                ('is_chef_delivered', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='core.profile')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.inventory')),
            ],
        ),
    ]
