# Django 2+ based real-estate website

This has been developed by me for learning Django 2+ / Python 3+. 

## 1. How to deploy

### 1.1 Common tasks for <u>local and Heroku</u>

If **models have been changed**, following needs to be run on a **LOCAL PC**:

#### 1.1.1 Clean Postgres database 

If previously some deployments to the local PC have been executed, then one **has** to clean & prepare database again. 

```
sudo su postgres
dropdb b40
createdb b40
exit
```

#### 1.1.2 Collect static files

This also acts as a sort of test that can identify some errors early on.

```
python3 manage.py collectstatic
```

### 1.2 Prepare migrations files

- Find and delete all `migrations` folders

```
find -type d -name migrations -prune -exec rm -rf {} \;
```

- Run makemigrations again

```
python3 manage.py makemigrations core
python3 manage.py makemigrations userMng
```

### 1.3 Deploy to local PC

- Continue from previous steps

```
python3 manage.py migrate
```

### 1.4 Deploy to Heroku

Heroku automatically runs collectstatic.

```
git push master heroku
```

#### 1.4.1 Dont forget to create superuser

```
heroku run python3 manage.py createsuperuser --username admin --email ci@se.cz
```

### 1.5. Deploy to own server

Execute on remote server following commands whenever models change.

**Onelines**

```
python3 manage.py makemigrations core && python3 manage.py makemigrations userMng && python3 manage.py migrate && sudo systemctl restart gunicorn.service 
```

**Common issues:**

- Kill heroku dyno

```
heroku ps && heroku ps:stop web.1
```

- Start Django manually

```
python3 manage.py runserver
```

- Adding new SSL certificates via certbot (letsencrypt)

```
sudo certbot --nginx certonly
```

- Nginx 502 gateway issue after VM reboot

Just **restart** nginx, then `gunicorn.service` as well as stop that socket thing

- Create **ER** Diagramms

<https://django-extensions.readthedocs.io/en/latest/graph_models.html>

![amazing_server_configuration/my_project_visualized.png](amazing_server_configuration/my_project_visualized.png)

```
python3 manage.py graph_models -a -g -o amazing_server_configuration/my_project_visualized.png
```

### 1.6 Run Celery

Run celery from b40re directory using

```
celery -A vanoce worker -l info
```

(Then,) to execute task(s) immediately 

```
python3 manage.py shell
from userMng.tasks import parse_forex_data
rst = parse_forex_data.apply()
```
Source: <https://stackoverflow.com/a/12900126/2171456>

## 2. Notes

When you add new css/js to `static` folder, it is good idea to still run locally `python3 manage.py collectstatic` which will overwrite `staticfiles` & which again can be pushed to heroku (unless being ignored by `gitignore`. 

Idea source: 
- <https://www.respekt.cz/sousede/nekolik-nezavislych-lidi-bydli-v-jednom-pronajatem-byte> sort of.
- <https://stackoverflow.com/a/40790734>
- <https://stackoverflow.com/a/50309967>
- Git post-recieve hook: <https://gist.github.com/lemiorhan/8912188>
[]: 
