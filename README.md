# Django 2+ based real-estate website

This has been developed by me for learning Django 2+ / Python 3+. 

## 1. How to deploy

### 1.1 Common tasks for <u>local and Heroku</u>

If **models have been changed**, following needs to be run on a **LOCAL PC**:

#### 1.1.1 Clean Postgres database 

If previously some deployments to the local PC have been executed, then one **has** to clean & prepare database again. 

```
sudo su postgres
dropdb mydb
createdb mydb
su jm
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

#### 1.4.1 Dont forget** to create superuser

```
heroku run python3 manage.py createsuperuser --username admin --email ci@se.cz
```


**Common issues:**

- Kill heroku dyno

```
heroku ps && heroku ps:stop web.1
```


## 2. Notes

When you add new css/js to `static` folder, it is good idea to still run locally `python3 manage.py collectstatic` which will overwrite `staticfiles` & which again can be pushed to heroku (unless being ignored by `gitignore`. 

Idea source: 
- <https://www.respekt.cz/sousede/nekolik-nezavislych-lidi-bydli-v-jednom-pronajatem-byte> sort of.
- <https://stackoverflow.com/a/40790734>
- <https://stackoverflow.com/a/50309967>