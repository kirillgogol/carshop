from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('catalog/', views.CarsView.as_view(), name='cars'),
    path('catalog/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registration/', views.RegisterUser.as_view(), name='register'),
]
