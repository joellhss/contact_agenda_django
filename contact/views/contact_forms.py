from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q

# Create your views here.
def create(request):
    context = {
        'site_title': 'Novo contato',
    }
    return render(request, 'contact/create.html', context)