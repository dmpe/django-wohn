Heroku requires several files to be in the root of the repository, see <https://devcenter.heroku.com/articles/deploying-python>

Some of the necessary files can be found in the `services/heroku/` folder of a dedicated branch.

## 1. Common tasks for <u>local and Heroku</u>

If **models have been changed**, following needs to be run on a **LOCAL PC**:

### 1.1 Clean PostgreSQL database 

If previously some deployments to the local PC have been executed, then one **has** to clean & prepare database again. 

```
sudo su postgres 
psql
```

To create DB via `psql`, use 

```
CREATE DATABASE b40re;
CREATE USER jm WITH ENCRYPTED PASSWORD 'yourpass';
GRANT ALL PRIVILEGES ON DATABASE b40re TO jm;
```

### 1.2 Collect static files

This also acts as a sort of test where you can spot some errors early on. 
It also uploads static and media files directly to the Azure blob container.

```
python3 manage.py collectstatic
```

### 1.2.5 Create DJango superuser 

Via their cli

```
heroku run python3 manage.py createsuperuser --username admin --email ci@se.cz
```


### 1.3 Prepare migrations files

<https://stackoverflow.com/a/40790734>
 
- Find and delete all `migrations` folders

```
find -type d -name migrations -prune -exec rm -rf {} \;
```

- Run makemigrations again

<https://stackoverflow.com/a/50309967>

```
python3 manage.py makemigrations core && python3 manage.py makemigrations userMng
```

Deploy to local/on remote server

```
python3 manage.py migrate
```

### 1.4 Deploy to Heroku

Heroku automatically runs collectstatic.

```
git push master heroku
```

## 2. Common issues

- Kill heroku dyno

```
heroku ps && heroku ps:stop web.1
```

# 3. Other notes

When you add new css/js to `static` folder, it is good idea to still run locally `python3 manage.py collectstatic` which will overwrite `staticfiles` & which again can be pushed to heroku (unless being ignored by `gitignore`). 
