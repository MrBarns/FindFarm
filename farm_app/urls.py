from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.loginView, name='login'),
    path('home/', views.homeView, name='home'),
    path('logout/', views.logoutView, name='logout'),
    path('user_register/', views.registerView, name='register_user'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='farm_app/reset_request.html'),
    name="password_reset"),

    path('reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='farm_app/reset_mail_sent.html'),
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='farm_app/reset_password.html'),
    name="password_reset_confirm"),

    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='farm_app/reset_confirm.html'),
    name="password_reset_complete"),

    path('create-farm/', views.createFarm, name="create_farm"),
    path('update-farm/<str:pk>/', views.updateFarm, name="update_farm"),
    path('delete-farm/<str:pk>/', views.deleteFarm, name="delete_farm"),
    path('farm/<str:pk>/', views.farm, name="farm"),
    
]