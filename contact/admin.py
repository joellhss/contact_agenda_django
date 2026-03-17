from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = '-id',


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'created_date', 'show')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('created_date',)
    list_per_page = 10
    list_max_show_all = 200
    list_editable = ('phone', 'show')
    list_display_links = ('id', 'first_name', 'last_name')

