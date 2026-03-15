Iniciar o projeto
python -m venv venv
.venv/Scripts/activate
pip install django
django-admin startproject project.
manage.py runserver

# Migrar base de dados

python manage.py makemigrations
python manage.py migrate    




git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT