from django.contrib import admin

from .models import Item, Menu


@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'slug', 'menu')


@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = ('name',)
