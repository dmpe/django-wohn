# Django 2 based real-estate website

This has been developed by me for learning Django 2+ / Python 3+. 

## How to deploy

```
git push master heroku (will just push it)
```

If additionally, models have been changed, following needs to be run:

```
heroku run bash
python3 manage.py makemigrations won
python3 manage.py migrate
exit
```