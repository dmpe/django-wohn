


# 3. Run Celery and RabbitMQ Management UI

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

Then, in an another `bash` window, execute commands below so that tasks such as fetching forex/currency data are run immediately.

```
python3 manage.py shell
from userMng.third_party_services.celery_tasks import parse_forex_data
rst = parse_forex_data.apply()
```

Source: <https://stackoverflow.com/a/12900126/2171456>

