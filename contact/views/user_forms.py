from django.shortcuts import render, redirect
from contact.forms import RegisterForm, LoginForm, UpdateUserForm
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def register(request):
    form_action = reverse('contact:register')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        context = {
            'form': form,
            'tab_title': 'Criar conta',
            'page_title': 'Criar conta',
            'form_action': form_action,
            'btn_submit': 'Cadastrar'
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('contact:login')
        
        messages.error(request, 'Erro ao cadastrar usuário!')
        return render(request, 'contact/register.html', context)

    context = {
        'form': RegisterForm(),
        'tab_title': 'Criar conta',
        'page_title': 'Criar conta',
        'form_action': form_action,
        'btn_submit': 'Cadastrar'
    }
    return render(request, 'contact/register.html', context)

@login_required
def update_user(request):
    form_action = reverse('contact:update_user')
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        context = {
            'form': form,
            'tab_title': 'Atualizar usuário',
            'page_title': 'Atualizar usuário',
            'form_action': form_action,
            'btn_submit': 'Atualizar'
        }

        if form.is_valid():
            user = form.save()
            auth.update_session_auth_hash(request, user)
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('contact:home')
        
        messages.error(request, 'Erro ao atualizar usuário!')
        return render(request, 'contact/register.html', context)

    context = {
        'form': UpdateUserForm(instance=request.user),
        'tab_title': 'Atualizar usuário',
        'page_title': 'Atualizar usuário',
        'form_action': form_action,
        'btn_submit': 'Atualizar'
    }
    return render(request, 'contact/register.html', context)

        

def login_view(request):
    form_action = reverse('contact:login')
    form = LoginForm(request)

    if request.user.is_authenticated:
        messages.warning(request, 'Você já está logado!')
        return redirect('contact:home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        context = {
            'form': form,
            'tab_title': 'Login',
            'page_title': 'Login',
            'form_action': form_action,
            'btn_submit': 'Entrar'
        }

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Bem-vindo(a)!')
            return redirect('contact:home')
        
        messages.error(request, 'Erro ao fazer login!')
        return render(request, 'contact/login.html', context)

    context = {
        'form': form,
        'tab_title': 'Login',
        'page_title': 'Login',
        'form_action': form_action,
        'btn_submit': 'Entrar'
    }
    return render(request, 'contact/login.html', context)

def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return redirect('contact:login')