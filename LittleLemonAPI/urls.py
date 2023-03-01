from django.urls import path
from . import views

urlpatterns = [
    path('menu-item', views.menu_items),
    path('menu-item/<int:pk>', views.single_item),
]