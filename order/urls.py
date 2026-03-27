from django.urls import path
from . import views

urlpatterns = [
    path('buy_now/<int:artwork_id>/', views.buy_now, name='buy_now'),
    path('checkout/', views.checkout, name='checkout'),
    path('place/', views.place_order, name='place_order'),
    path('success/', views.order_success, name='success'),
    path('payment/<int:order_id>/', views.payment_view),
    path('invoice/<int:order_id>/', views.invoice_view, name='invoice'),

]