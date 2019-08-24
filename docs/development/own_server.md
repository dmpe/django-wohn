# Own Server

Before I have switched to container based, CI/CD workflow, I have installed everything needed on my server myself...

Some important components are located in `services/own_server`.
See heroku page as well.

To install pgadmin4, follow <https://www.pgadmin.org/docs/pgadmin4/4.x/server_deployment.html> guideline.

## 1. Deploy to own server

### Create Django superuser

```
python3 manage.py createsuperuser --username admin --email ci@se.cz
```

Then, execute on remote server following commands whenever Django model(s) change.

```
python3 manage.py makemigrations <model> && python3 manage.py migrate && sudo systemctl restart gunicorn.service
```

After git commit & push to the server, you can also use a special post-receive hook <https://gist.github.com/lemiorhan/8912188>.

### Setup Git Repo with post-receive hook

At certain point of time, the goal was to use AWS Cloud9 IDE to edit **and** push -- on the same server (username@domain:/home/username/domain_push.git) -- to the git repository, from which website was "deployment" (aka gunicorn restarted).

Today, this is totally obsolete with VS Code (remote development or Eclipse Che) for instance.

* See this guide <https://stackoverflow.com/a/40479963>
* E.g. for AWS Cloud9 IDE, first clone git repo somewhere
* Then create a new **bare** repo which is used for pushing to it and now you have to add/register aforementioned `post-recieve` hook.

## 2. Some common issues

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

(This could have been moved to Azure Functions for example.)

Source:

- <https://stackoverflow.com/a/12900126/2171456>

First install `RabbitMQ` (message broker), then `Celery` ("worker").

```
sudo rabbitmq-plugins enable rabbitmq_management
sudo rabbitmqctl add_user jm password
sudo rabbitmqctl set_user_tags jm administrator
```

Run `Celery` from `b40re` directory using:

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

