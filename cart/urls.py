from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/<int:artwork_id>/', views.add, name='add'),
    path('increase/<int:item_id>/', views.increase),
    path('decrease/<int:item_id>/', views.decrease),
]