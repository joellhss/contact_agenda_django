from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q

# Create your views here.
def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')
    
    paginator = Paginator(contacts, 9)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'site_title': 'Home',
        'page_obj': page_obj
    }
    return render(request, 'contact/index.html', context)

def contact(request, contact_id):
    # contact_for_id = Contact.objects.get(pk=contact_id)
    contact_for_id = get_object_or_404(Contact, pk=contact_id, show=True)

    context = {
        'site_title': f'{contact_for_id.first_name} {contact_for_id.last_name}',
        'contact': contact_for_id
    }
    return render(request, 'contact/contact.html', context)

def search(request):
    search_value = request.GET.get('q', '').strip()
    if not search_value:
        return redirect('contact:home') 

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains = search_value) |
            Q(last_name__icontains = search_value) |
            Q(phone__icontains = search_value) |
            Q(email__icontains = search_value) |
            Q(id__icontains = search_value)
        )\
        .order_by('-id')
    
    paginator = Paginator(contacts, 9)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'site_title': 'Home',
        'page_obj': page_obj,
        'search_value': search_value
    }
    return render(request, 'contact/index.html', context)