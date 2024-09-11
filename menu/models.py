from django.db import models

from django.shortcuts import reverse


class Menu(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    menu = models.ForeignKey(Menu,
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'{self.name} (id: {self.id})'

    def get_absolute_url(self):
        return reverse('menu:menu_tree', kwargs={"menu_slug": self.slug})
