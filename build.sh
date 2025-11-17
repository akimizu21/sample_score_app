#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip setuptools wheel
pip install --no-cache-dir -r backend/requirements.txt

export FLASK_APP=wsgi:app

flask db upgrade