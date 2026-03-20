from contact.models import Contact
from django import forms
import re

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Selecione uma categoria'
        self.fields['category'].required
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
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone:
            return phone  # deixa passar se for opcional

        # Remove espaços e traços
        phone_clean = re.sub(r'\D', '', phone)

        if len(phone_clean) < 10 or len(phone_clean) > 11:
            raise forms.ValidationError('Telefone inválido.')

        return phone
    
    def clean(self):
        data = super().clean()
        if not data.get('email') and not data.get('phone'):
            raise forms.ValidationError(
                'Informe pelo menos telefone ou e-mail.'
            )
        if data.get('first_name') == data.get('last_name'):
            raise forms.ValidationError(
                'Nome e sobrenome não podem ser os mesmos.'
            )
        return data
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'picture', 'category',)
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'phone': 'Telefone',
            'email': 'E-mail',
            'description': 'Descrição',
            'picture': 'Imagem de perfil',
            'category': 'Categoria'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Digite o nome aqui',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Digite o sobrenome aqui',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Digite o número de telefone aqui',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Digite o e-mail aqui',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Digite o que desejar sobre este contato',
                'rows': '5'
            }),
            'picture': forms.FileInput(attrs={
                'accept': "image/*"
            }),
            'category': forms.Select(attrs={
            }),
        }