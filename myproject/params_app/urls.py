from django.urls import path 
from params_app.views import home,login,dashboard
# from params_app.views import login
urlpatterns = [
        path('',home, name='home'),
        path('login',login, name='login'),
        path('dashboard',dashboard, name='dashboard'),


]
