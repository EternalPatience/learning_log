from django.urls import path, include
from . import views
app_name = 'users'

urlpatterns = [
    #Switch on autorizarion
    path('', include('django.contrib.auth.urls')),
    path('logout/', views.logout, name='logged_out'),
    path('register/', views.register, name='register'),
]