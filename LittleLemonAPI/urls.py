from django.urls import path
from . import views

urlpatterns = [
    path('menu-item', views.MenuItemsView.as_view()),
    path('menu-item/<int:pk>', views.SingleMenuItemView.as_view()),
]