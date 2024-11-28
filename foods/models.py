from django.db import models

# Create your models here.from django.db import models
from django.contrib.auth.models import User

class FoodType(models.Model):
    nomi = models.CharField(max_length=100, verbose_name="Taom turi")

    def __str__(self):
        return self.nomi

class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name='foods', verbose_name="Taom turi")
    nomi = models.CharField(max_length=100, verbose_name="Taom nomi")
    tarkibi = models.TextField(verbose_name="Tarkibi")
    narxi = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")

    def __str__(self):
        return self.nomi

class Comment(models.Model):
    text = models.TextField(verbose_name="Izoh")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='comments', verbose_name="Taom")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    def __str__(self):
        return f"{self.author.username}: {self.text[:20]}"
