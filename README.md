# Django 2+ based real-estate website

This has been developed by me for learning Django 2+ / Python 3+. 

## How to deploy

Usually: 
```
git push master heroku
```

If **models have been changed**, following needs to be run on a **LOCAL PC**:

1. Delete the whole `migrations` folder

1.5 `python3 manage.py makemigrations core, user_management`

1.6 `heroku run python3 manage.py migrate`

2. commit and push again

```
git push master heroku
```

**Notes**

When you add new css/js to `static` folder, it is good idea to still run locally `python3 manage.py collectstatic` which will overwrite `staticfiles` & which again can be pushed to heroku. 

Idea source: 
- <https://www.respekt.cz/sousede/nekolik-nezavislych-lidi-bydli-v-jednom-pronajatem-byte> sort of.
- <https://stackoverflow.com/a/40790734>
- <https://stackoverflow.com/a/50309967>