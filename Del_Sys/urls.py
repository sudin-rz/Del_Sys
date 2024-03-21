from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home),

    path('sign_in/', auth_views.LoginView.as_view(template_name="sign_in.html")),
    path('sign_out/', auth_views.LogoutView.as_view(next_page="/")),
    path('sign_up/', views.sign_up),

    
    path('customer/',views.customer_page),
    path('courier/',views.courier_page),
    ]
