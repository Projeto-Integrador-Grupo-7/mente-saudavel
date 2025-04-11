# Sistema Mente Saudável

## Instalar:
```
pip install django

pip install mysqlclient
```

## Criar banco:
```
CREATE DATABASE mente_saudavel CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## Migrations:
### Quando houver alteração em um arquivo models.py, utilize para criar a migration:
```
python manage.py makemigrations nome_do_app --name nome_da_migration
```
### Se a migration já foi criada, aplicar ela com:
```
python manage.py migrate
```

## Rodar aplicação:
```
python manage.py runserver
```
