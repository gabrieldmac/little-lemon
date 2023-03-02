from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-item', views.menu_items),
    path('menu-item/<int:pk>', views.single_item),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('manager-view/', views.manager_view),
    path('throttle_check/', views.throttle_check),
    path('throttle_check_auth/', views.throttle_check_auth)
    
]