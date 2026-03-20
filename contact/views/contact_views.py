from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar esta página!')
        return redirect('contact:login')

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(owner=request.user)\
        .order_by('-id')
    
    paginator = Paginator(contacts, 9)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'tab_title': 'Home',
        'page_obj': page_obj
    }
    return render(request, 'contact/index.html', context)

@login_required
def contact(request, contact_id):
    # contact_for_id = Contact.objects.get(pk=contact_id)
    contact_for_id = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    confirmation = request.GET.get('confirm') == '1'

    context = {
        'tab_title': f'{contact_for_id.first_name} {contact_for_id.last_name}',
        'contact': contact_for_id,
        'confirmation_del': confirmation
    }
    return render(request, 'contact/contact.html', context)

@login_required
def search(request):
    search_value = request.GET.get('q', '').strip()
    if not search_value:
        return redirect('contact:home') 

    contacts = Contact.objects\
        .filter(show=True)\
        .filter(owner=request.user)\
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
        'tab_title': 'Home',
        'page_obj': page_obj,
        'search_value': search_value
    }
    return render(request, 'contact/index.html', context)