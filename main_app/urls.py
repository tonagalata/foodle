from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stores/', views.stores, name='stores'),
    path('accounts/signup/', views.signup, name='signup'),
    path('checkout/<int:total_volunteers>/<int:total_checkouts>/',
         views.checkout, name='checkout'),
    path('remove/', views.remove_vol, name='remove'),
    path('cart/', views.cart, name='cart'),
]
