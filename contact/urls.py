from django.contrib import admin
from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),

    # Contact CRUD
    path('contact/<int:contact_id>/detail/', views.contact, name='detail'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

    # User
    path('user/register/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.update_user, name='update_user'),
]
