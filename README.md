# Contact Agenda (Django)

Projeto de estudo utilizando o framework **Django** para criação de uma agenda de contatos.
O objetivo deste projeto é reforçar conceitos fundamentais do Django durante o aprendizado.

---

# 🎯 Objetivo do projeto

Praticar conceitos fundamentais do Django como:

* Estrutura de projetos
* Aplicações (apps)
* Templates
* Arquivos estáticos
* Organização de código
* Uso do ORM

---

# 📚 Tecnologias utilizadas

* Python
* Django
* WhiteNoise

---

# 🚀 Criando e iniciando o projeto

## 1. Criar o ambiente virtual

```bash
python -m venv .venv
```

## 2. Ativar o ambiente virtual

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

# 📦 Instalar dependências

Instalar o Django

```bash
pip install django
```

Instalar o WhiteNoise (opcional – para servir arquivos estáticos em produção)

```bash
pip install whitenoise
```

---

# 🛠 Criar o projeto Django

```bash
django-admin startproject project .
```

Criar um novo aplicativo

```bash
python manage.py startapp nomedoapp
```

---

# ⚙️ Comandos úteis do Django

Listar todos os comandos disponíveis

```bash
python manage.py --help
```

Iniciar o servidor de desenvolvimento

```bash
python manage.py runserver
```

---

# 🗄 Migrações do banco de dados

Criar arquivos de migração após alterações nos models

```bash
python manage.py makemigrations
```

Aplicar migrações no banco de dados

```bash
python manage.py migrate
```

---

# 👤 Administração do Django

Criar um superusuário

```bash
python manage.py createsuperuser
```

Alterar senha de um usuário

```bash
python manage.py changepassword USERNAME
```

---

# 📁 Arquivos estáticos

Coletar arquivos estáticos para produção

```bash
python manage.py collectstatic
```

---

# 🧠 Trabalhando com Models (ORM do Django)

Importar o model

```python
from contact.models import Contact
```

## Criar um contato (lazy)

```python
contact = Contact(**fields)
contact.save()
```

## Criar um contato diretamente

```python
contact = Contact.objects.create(**fields)
```

## Buscar um contato pelo ID

```python
contact = Contact.objects.get(pk=10)
```

## Atualizar um contato

```python
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
```

## Apagar um contato

```python
contact.delete()
```

## Buscar todos os contatos

```python
contacts = Contact.objects.all()
```

## Ordenar contatos por ID (decrescente)

```python
contacts = Contact.objects.all().order_by('-id')
```

## Filtrar contatos

```python
contacts = Contact.objects.filter(**filters).order_by('-id')
```

---

# ▶️ Executando o projeto

Após instalar as dependências e ativar o ambiente virtual:

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000
```
