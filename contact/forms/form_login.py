from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
        labels = {
            'username': 'Nome de usuário',
            'password': 'Senha'
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Digite o nome de usuário aqui',
            }),
            'password': forms.PasswordInput(attrs={
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