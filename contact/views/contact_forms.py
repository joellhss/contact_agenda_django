from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from contact.forms import ContactForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
        
# Create your views here.
@login_required
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {
        'tab_title': 'Novo contato',
        'page_title': 'Novo contato',
        'form': form,
        'form_action': form_action,
        'btn_submit': 'Cadastrar'
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, 'Contato salvo com sucesso!')
            return redirect('contact:detail', contact_id=contact.pk)

        messages.error(request, 'Erro ao salvar contato!')
        return render(request, 'contact/create.html', context)

    context = {
        'tab_title': 'Novo contato',
        'page_title': 'Novo contato',
        'form': ContactForm(),
        'form_action': form_action,
        'btn_submit': 'Cadastrar'
    }
    return render(request, 'contact/create.html', context)

@login_required
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    form_action = reverse('contact:update', args=(contact_id,))
    
    if request.method == 'POST':
        if request.POST.get('delete_picture') == 'True':
            contact.picture = 'pictures/default/default.jpg'
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)

        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
        'tab_title': 'Atualizar contato',
        'page_title': 'Atualizar contato',
        'form': form,
        'form_action': form_action,
        'btn_submit': 'Atualizar'
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, 'Contato atualizado com sucesso!')
            return redirect('contact:detail', contact_id=contact.pk)

        messages.error(request, 'Erro ao atualizar contato!')
        return render(request, 'contact/create.html', context)

    context = {
        'tab_title': 'Atualizar contato',
        'page_title': 'Atualizar contato',
        'form': ContactForm(instance=contact),
        'form_action': form_action,
        'btn_submit': 'Atualizar'
    }
    return render(request, 'contact/create.html', context)

@login_required
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)

    if request.method == 'POST':
        # contact.delete()
        contact.show = False
        contact.save()
        messages.success(request, 'Contato excluído com sucesso!')
        return redirect('contact:home')

    messages.error(request, 'Erro ao excluir contato!')
    return redirect('contact:detail', contact_id=contact_id)