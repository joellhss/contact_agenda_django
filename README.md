# Contact Agenda (Django)

Projeto de estudo utilizando o framework **Django** para criação de uma agenda de contatos.
O objetivo deste projeto é reforçar conceitos fundamentais do Django durante o aprendizado.

## 🎯 Objetivo do projeto

Praticar conceitos fundamentais do Django como:

* Estrutura de projetos
* Aplicações (apps)
* Templates
* Arquivos estáticos
* Organização de código

## 📚 Tecnologias utilizadas

* Python
* Django
* WhiteNoise


## 🚀 Criando e iniciando o projeto

### 1. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar o ambiente virtual

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```


## 📦 Instalar dependências

Instalar o Django:

```bash
pip install django
```


## 🛠 Criar o projeto Django

```bash
django-admin startproject project .
```

## ⚙️ Comandos úteis do Django

Ver todos os comandos disponíveis:

```bash
python manage.py --help
```

Iniciar o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Criar um novo aplicativo:

```bash
python manage.py startapp nomedoapp
```

## 📁 Arquivos estáticos

Coletar arquivos estáticos para produção:

```bash
python manage.py collectstatic
```
Instalar o WhiteNoise (para servir arquivos estáticos)(opcional):

```bash
pip install whitenoise
```

## ▶️ Executando o projeto

Após instalar as dependências e ativar o ambiente virtual:

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000
```
