from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from contact.forms import ContactForm
from django.urls import reverse
        

# Create your views here.
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {
        'site_title': 'Novo contato',
        'form': form,
        'form_action': form_action
        }

        if form.is_valid():
            print("Formulário válido")
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(request, 'contact/create.html', context)

    context = {
        'site_title': 'Novo contato',
        'form': ContactForm(),
        'form_action': form_action
    }
    return render(request, 'contact/create.html', context)

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
        'site_title': 'Novo contato',
        'form': form,
        'form_action': form_action
        }

        if form.is_valid():
            print("Formulário válido")
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

        return render(request, 'contact/create.html', context)

    context = {
        'site_title': 'Novo contato',
        'form': ContactForm(instance=contact),
        'form_action': form_action
    }
    return render(request, 'contact/create.html', context)


def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    print('entrei')

    if request.method == 'POST':
        # contact.delete()
        contact.show = False
        contact.save()
        return redirect('contact:home')

    return redirect('contact:detail', contact_id=contact_id)