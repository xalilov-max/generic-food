# Generated by Django 4.2.16 on 2024-11-28 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100, verbose_name='Taom turi')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100, verbose_name='Taom nomi')),
                ('tarkibi', models.TextField(verbose_name='Tarkibi')),
                ('narxi', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Narxi')),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='foods.foodtype', verbose_name='Taom turi')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Izoh')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='foods.food', verbose_name='Taom')),
            ],
        ),
    ]
