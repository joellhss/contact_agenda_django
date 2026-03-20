from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Nome de usuário',
            'email': 'E-mail',
            'password1': 'Senha',
            'password2': 'Confirmar senha'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Digite o nome aqui',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Digite o sobrenome aqui',
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Digite o nome de usuário aqui',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Digite o e-mail aqui',
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Digite a senha aqui',
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Digite a senha aqui',
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            base_class = 'form-control focus-ring focus-ring-success border'
            
            if self.is_bound:
                value = self.data.get(field_name)

                if self.errors.get(field_name):
                    field.widget.attrs['class'] = f'{base_class} is-invalid border-danger'
                elif value:
                    field.widget.attrs['class'] = f'{base_class} is-valid border-success'
                else:
                    field.widget.attrs['class'] = base_class
            else:
                field.widget.attrs['class'] = base_class
    
    def clean_username(self):
        value = self.cleaned_data.get('username')
        if not value:
            raise forms.ValidationError('Campo obrigatório.')
        if len(value) < 3:
            raise forms.ValidationError('Mínimo de 3 caracteres.')
        return value
    def clean_password2(self):
        value = self.cleaned_data.get('password2')
        if not value:
            raise forms.ValidationError('Campo obrigatório.')
        return value
    def clean_password1(self):
        value = self.cleaned_data.get('password1')
        if not value:
            raise forms.ValidationError('Campo obrigatório.')
        return value
    def clean_email(self):
        value = self.cleaned_data.get('email')
        if not value:
            raise forms.ValidationError('Campo obrigatório.')
        if User.objects.filter(email=value).exists():
            raise forms.ValidationError('E-mail já cadastrado.')
        return value
    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        if not value:
            raise forms.ValidationError('Campo obrigatório.')
        if len(value) < 3:
            raise forms.ValidationError('Mínimo de 3 caracteres.')
        return value
    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        if not value:
            raise forms.ValidationError('Campo obrigatório.')
        if len(value) < 3:
            raise forms.ValidationError('Mínimo de 3 caracteres.')
        return value

class UpdateUserForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite a senha aqui',
            'autocomplete': 'new-password',
        }),
        required=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite a senha aqui',
        }),
        required=False,
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'username': 'Nome de usuário',
            'email': 'E-mail',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Digite o nome aqui',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Digite o sobrenome aqui',
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Digite o nome de usuário aqui',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Digite o e-mail aqui',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            base_class = 'form-control focus-ring focus-ring-success border'
            
            if self.is_bound:
                value = self.data.get(field_name)

                if self.errors.get(field_name):
                    field.widget.attrs['class'] = f'{base_class} is-invalid border-danger'
                elif value:
                    field.widget.attrs['class'] = f'{base_class} is-valid border-success'
                else:
                    field.widget.attrs['class'] = base_class
            else:
                field.widget.attrs['class'] = base_class
    
    def clean_username(self):
        value = self.cleaned_data.get('username')
        if not value:
            raise forms.ValidationError('Campo obrigatório.')
        if len(value) < 3:
            raise forms.ValidationError('Mínimo de 3 caracteres.')
        return value
    def clean_password2(self):
        value = self.cleaned_data.get('password2')
        if value:
            if value != self.cleaned_data.get('password'):
                raise forms.ValidationError('As senhas não coincidem.')
        return value
    def clean_password(self):
        value = self.cleaned_data.get('password')
        if value:
            password_validation.validate_password(value, self.instance)
        return value
    def clean_email(self):
        value = self.cleaned_data.get('email')
        if not value:
            raise forms.ValidationError('Campo obrigatório.')
        current_email = self.instance.email
        if User.objects.filter(email=value).exclude(email=current_email).exists():
            raise forms.ValidationError('E-mail já cadastrado.')
        return value
    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        if not value:
            raise forms.ValidationError('Campo obrigatório.')
        if len(value) < 3:
            raise forms.ValidationError('Mínimo de 3 caracteres.')
        return value
    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        if not value:
            raise forms.ValidationError('Campo obrigatório.')
        if len(value) < 3:
            raise forms.ValidationError('Mínimo de 3 caracteres.')
        return value
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data.get('password'):
            user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
    