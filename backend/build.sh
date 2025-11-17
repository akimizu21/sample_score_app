#!/usr/bin/env bash
set -o errexit

# pipとビルドツールのアップグレード
pip install --upgrade pip setuptools wheel

# 依存関係のインストール（backendフォルダ内のrequirements.txt）
pip install --no-cache-dir -r requirements.txt

# FLASKアプリケーションのパスを指定（flaskrを含める）
export FLASK_APP=wsgi:app

# backendディレクトリに移動してマイグレーション実行
flask db upgrade