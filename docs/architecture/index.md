# Development overtime

Shows how CI/CD + architecture looked like in the past.

![arch/evolution.jpg](arch/evolution.jpg)

# CI/CD Pipeline

Shows current deployment pipeline, from local changes to building a container on server.

![arch/azure.jpg](arch/azure.jpg)

# App's Class Diagramm

Created using <https://django-extensions.readthedocs.io/en/latest/graph_models.html> and

```shell
python3 manage.py graph_models -a -g -o arch/class_diagramm.png
```

![arch/class_diagramm.png](arch/class_diagramm.png)