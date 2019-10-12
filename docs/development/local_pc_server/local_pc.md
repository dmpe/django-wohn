# Local PC

Even though using container based approach for developing and deploying
the website, it may be necessary sometimes to test things locally, on your own PC with docker being installed.

See <https://dmpe.github.io/django-wohn/development/container/container/> for some additional documentation.


## Setup

- Install latest docker (compose is not necessary) with PostgreSQL (tested on 11+)
- Install all required package for backend part of melive.xyz

    ```
    sudo pip3 install -r backend/requirenments.txt
    ```

- Navigate to **backend** folder and execute

    ```
    python3 manage.py runserver --nostatic --insecure
    ```
    If your browser is complaining about SSL issues, follow this [answer](https://stackoverflow.com/a/34033592) for fixing it.
