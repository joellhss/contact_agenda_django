from django.contrib import admin
from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),

    # Contact CRUD
    path('contact/<int:contact_id>/detail/', views.contact, name='contact_detail'),
    path('contact/create/', views.create, name='contact_create'),
    path('contact/<int:contact_id>/update/', views.contact, name='contact_update'),
    path('contact/<int:contact_id>/delete/', views.contact, name='contact_delete'),
]
