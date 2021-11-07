# from django.contrib import admin
from django.urls import path

# import our views
from user import views

# define our app name
app_name = 'user'

# create our url paths
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
