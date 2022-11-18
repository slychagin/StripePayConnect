from django.urls import path
from . import views


urlpatterns = [
    path('<int:item_id>/', views.buy_item, name='buy_item'),
    path('create-checkout-session/<pk>/', views.create_checkout_session, name='create-checkout-session'),
]
