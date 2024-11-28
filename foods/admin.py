from django.contrib import admin
from .models import FoodType, Food, Comment

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomi']

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'narxi', 'food_type']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'food', 'created']
