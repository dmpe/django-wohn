#!/bin/bash
git config --global credential.helper store
git remote prune origin

git fetch origin --prune
