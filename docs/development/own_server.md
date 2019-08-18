Before I have switched to container based CI/CD, I have installed everything on server myself...

Some important components are located in `services/own_server`.
See heroku page as well. 


To install pgadmin4, follow <https://www.pgadmin.org/docs/pgadmin4/4.x/server_deployment.html>


## 1.1 Deploy to own server


### Create superuser

```
python3 manage.py createsuperuser --username admin --email ci@se.cz
```

Then, execute on remote server following commands whenever models change.

```
python3 manage.py makemigrations core && python3 manage.py makemigrations userMng && python3 manage.py migrate && sudo systemctl restart gunicorn.service 
```

After pushing a commit to the server, see a special post-receive hook <https://gist.github.com/lemiorhan/8912188> too.

## 1.1.1 Setup Git Repo with post-recieve hook

The goal was to use AWS Cloud9 IDE to push -- on the same server (username@domain:/home/username/domain_push.git) -- to the git repository which acts as deployment repo. 

Today, this is totally obsolete which VS Code (remote development or Eclipse Che) for instance.

* See this guide <https://stackoverflow.com/a/40479963>
* E.g. for AWS Cloud9 IDE, first clone this repo somewhere
* Create a new bare repo which is used for pushing and in it, add/register aforementioned `post-recieve` hook. 

## 2. Common issues

- Start Django manually

```
python3 manage.py runserver --nostatic
```

- Adding new SSL certificates via certbot (letsencrypt)

```
sudo certbot --nginx certonly
```

- Nginx 502 gateway issue after VM reboot

Just **restart** nginx, then `sudo systemctl restart gunicorn.service` as well as stop that socket thing



