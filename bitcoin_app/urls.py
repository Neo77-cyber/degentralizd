from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name = 'home' ),
    path('signin/', views.signin, name = 'signin' ),
    path('register/', views.register, name = 'register' ),
    path('logout', views.logout, name = 'logout'),
    path('portfolio/', views.portfolio, name = 'portfolio' ),
    path('buycrypto/', views.buy_crypto, name = 'buy_crypto' ),
    path('howitworks/', views.how_it_works, name = 'how_it_works' ),
    path('support/', views.how_it_works, name = 'support' )


       
]