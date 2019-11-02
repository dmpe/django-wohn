import os
from os import path
import requests
from dotenv import find_dotenv, load_dotenv
import pytest


def test_LocalPC_download():
    load_dotenv(find_dotenv("secrets.env"))
    link_db = os.getenv("dropbox_link")

    fl = os.path.abspath(os.path.join(os.path.dirname(__file__), "client_secrets.json"))
    r = requests.get(link_db, allow_redirects=True)
    open(fl, "wb").write(r.content)

    mes = None
    if path.exists(fl):
        mes = "Secret File for GA exists"
    else:
        mes = "GA secret json file does not exist"

    print(mes)

    assert mes == "Secret File for GA exists"

if __name__ == "__main__":
    test_LocalPC_download()
