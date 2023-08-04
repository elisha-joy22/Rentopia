from django.urls import path
from accounts import views

urlpatterns = [
    path('user/register/', views.RegisterUserView.as_view(), name='user-register'),
    path('user/login/', views.LoginUserView.as_view(), name='user-login'),
    path('user/logout/', views.LogoutUserView.as_view(), name='user-logout'),
    path('user/profile/', views.ProfileView.as_view(), name='user-profile'),
    path('user/home', views.HomeView.as_view(), name='user-home')
]
