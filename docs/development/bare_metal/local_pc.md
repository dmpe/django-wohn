# Local PC

Even though using container based approach for developing and deploying
the website, it may be necessary sometimes to test things locally, on your own PC with docker being installed.

See <https://dmpe.github.io/django-wohn/development/container/container/> for some additional documentation.


## Setup

### Backend

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


### Frontend

To update `package.json` **and** package themselves, we need to install to:

```
yarn global add syncyarnlock // install syncyarnlock globally (!!!!)
yarn upgrade // update dependencies, updates yarn.lock
syncyarnlock -s -k // updates package.json with versions installed from yarn.lock
yarn install // updates yarn.lock with current version constraint from package.json
```
