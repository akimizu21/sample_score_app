#!/usr/bin/env bash
# Renderのビルド時に実行されるスクリプト

set -o errexit

# 依存関係のインストール
pip install --upgrade pip
pip install -r requirements.txt

# データベースマイグレーション
flask db upgrade