# Django 2 based real-estate website

This has been developed by me for learning Django 2+ / Python 3+. 

## How to deploy

```
git push master heroku (will just push it)
```

If additionally, models have been changed, following needs to be run on the **LOCAL PC**:
Source: <https://stackoverflow.com/a/40790734>

```
python3 manage.py makemigrations won

(Then it needs to upload that migration file!)
git push master heroku

heroku run python3 manage.py migrate

```