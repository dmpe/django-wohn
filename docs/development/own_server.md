Before I have switched to container based CI/CD, I have installed everything on server myself...

Some important components are located in `services/own_server`.
See heroku page as well.

To install pgadmin4, follow <https://www.pgadmin.org/docs/pgadmin4/4.x/server_deployment.html>

## 1. Deploy to own server

### Create superuser

```
python3 manage.py createsuperuser --username admin --email ci@se.cz
```

Then, execute on remote server following commands whenever models change.

```
python3 manage.py makemigrations core && python3 manage.py makemigrations userMng && python3 manage.py migrate && sudo systemctl restart gunicorn.service
```

After pushing a commit to the server, see a special post-receive hook <https://gist.github.com/lemiorhan/8912188> too.

### Setup Git Repo with post-receive hook

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

## 3. Run Celery and RabbitMQ Management UI

// TODO: Could be moved to Azure Functions

First install `RabbitMQ`, then `Celery`.

```
sudo rabbitmq-plugins enable rabbitmq_management
sudo rabbitmqctl add_user jm password
sudo rabbitmqctl set_user_tags jm administrator
```

Run `Celery` from b40re directory using

```
sudo systemctl restart rabbitmq<TAB>
celery -A vanoce worker -l info
```

Then, in an another `bash` window, execute commands below so that tasks such as
fetching forex/currency data are run immediately.

```
python3 manage.py shell
from userMng.third_party_services.celery_tasks import parse_forex_data
rst = parse_forex_data.apply()
```

Source: <https://stackoverflow.com/a/12900126/2171456>
