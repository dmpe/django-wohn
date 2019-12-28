# Heroku/PaaS

Heroku requires several files to be in the root of the repository, see <https://devcenter.heroku.com/articles/deploying-python>

Some of the necessary files can be found in the `services/heroku/` folder of a dedicated branch.

## 1. Initial Setup steps

If **models have changed**, following needs to be run **first** on a **LOCAL PC**:

### 1.1 Prepare PostgreSQL database

```
sudo su postgres
psql
```

To create our DB, use `psql`:

```
CREATE DATABASE b40re;
CREATE USER jm WITH ENCRYPTED PASSWORD 'yourpass';
GRANT ALL PRIVILEGES ON DATABASE b40re TO jm;
```

### 1.2 Collect static files

This also acts as a sort of test where you can spot some errors early on.
It uploads static and media files directly to the Azure blob container too.

```
python3 manage.py collectstatic
```

#### 1.2.5 Create Django superuser

In Heroku, via their cli:

```
heroku run python3 manage.py createsuperuser --username admin --email ci@se.cz
```

### 1.3 Prepare migrations files

If previously some deployments to the local PC were executed, then one **has** to clean & prepare database again.

<https://stackoverflow.com/a/40790734>

- Find and delete all `migrations` folders

```
find -type d -name migrations -prune -exec rm -rf {} \;
```

- Run makemigrations again

<https://stackoverflow.com/a/50309967>

```
python3 manage.py makemigrations <model>
```

Deploy to local/on remote server

```
python3 manage.py migrate
```

### 1.4 Deploy to Heroku

Heroku automatically runs `collectstatic`.

```
git push master heroku
```

## 2. Common Heroku issues

- Kill heroku dyno

```
heroku ps && heroku ps:stop web.1
```

# 3. Other notes

When you add new css/js files to `static` folder, it is good idea to still run locally `python3 manage.py collectstatic` which will overwrite `staticfiles` folder & which again can be pushed to heroku (unless being ignored by `gitignore`).
