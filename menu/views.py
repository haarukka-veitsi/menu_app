from django.shortcuts import render


def draw_menu_tree(request, menu_slug=None):
    context = {}
    return render(request, 'menu/index.html', context)
