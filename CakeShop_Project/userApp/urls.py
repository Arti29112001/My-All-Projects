
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('login', views.login),
    path('signUp', views.signUp),
    path('ShowCakes/<id>', views.ShowCakes),
    path('ViewDetails/<id>', views.ViewDetails),
    path('signout', views.signout),
    path('addToCart', views.addToCart),
    path('showAllCartItems', views.showAllCartItems),
    path('MakePayment', views.MakePayment),
    path('demo', views.demo),
]

