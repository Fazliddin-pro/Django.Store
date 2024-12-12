from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('checkout/', views.checkout, name='checkout'),
    path('logout/', views.logout, name='logout'),
]
