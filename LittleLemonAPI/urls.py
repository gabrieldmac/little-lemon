from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-item', views.menu_items),
    path('menu-item/<int:pk>', views.single_item),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token)
]