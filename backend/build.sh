#!/usr/bin/env bash
set -o errexit

# 依存関係のインストール
pip install --upgrade pip setuptools wheel
pip install --no-cache-dir -r requirements.txt

# FLASKアプリケーションのパスを指定
export FLASK_APP=wsgi:app

# データベースマイグレーション
flask db upgrade