#!/usr/bin/env bash
set -o errexit

# PYTHONPATHを設定（プロジェクトルートを追加）
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# pipとビルドツールのアップグレード
pip install --upgrade pip setuptools wheel

# 依存関係のインストール（backendフォルダ内のrequirements.txt）
pip install --no-cache-dir -r backend/requirements.txt

# FLASKアプリケーションのパスを指定（flaskrを含める）
export FLASK_APP=wsgi:app

# データベースマイグレーション
flask db upgrade