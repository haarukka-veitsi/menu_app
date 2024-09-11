from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.draw_menu_tree, name='home'),
    path('<slug:menu_slug>/', views.draw_menu_tree, name='menu_tree'),
]
