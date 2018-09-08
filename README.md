# Django 2+ based real-estate website

This has been developed by me for learning Django 2+ / Python 3+. 

## How to deploy

```
git push master heroku (will just push it)
```

If additionally, **models have been changed**, following needs to be run on a **LOCAL PC**:

1. Delete the whole `migrations` folder

1.5 `python3 manage.py makemigrations won`

1.6 `heroku run python3 manage.py migrate`

2. commit & push again 

**Notes**

When you add new images, pictures, js it is good idea to still run locally `python3 manage.py collectstatic` which will overwrite connect & which again can be pushed to heroku. That, even though heroku does it by itself.

Idea source: 
- <https://www.respekt.cz/sousede/nekolik-nezavislych-lidi-bydli-v-jednom-pronajatem-byte> sort of.
- <https://stackoverflow.com/a/40790734>
- <https://stackoverflow.com/a/50309967>