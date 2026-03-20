from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category',
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(default='pictures/default/default.jpg',upload_to='pictures/%Y/%m/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=False, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Contact',
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def picture_filename(self):
        """Retorna apenas o nome do arquivo da imagem."""
        if self.picture:
            return os.path.basename(self.picture.name)
        return ''

    
