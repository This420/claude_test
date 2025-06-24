# claude_test

FastAPI + uv + Docker を使ったPython API開発環境

## 説明

このリポジトリはClaudeを使ったテスト目的で作成された、FastAPIとuvとDockerを使ったシンプルなPython API開発環境です。

## 使い方

### 前提条件
- Docker Desktop がインストールされていること

### 開発環境の起動

```bash
# リポジトリをクローン
git clone https://github.com/This420/claude_test.git
cd claude_test

# Docker Composeでアプリケーションを起動
docker-compose up --build
```

### API エンドポイント

アプリケーションが起動すると、以下のエンドポイントが利用可能になります：

- `GET /` - ルートエンドポイント
- `GET /health` - ヘルスチェック  
- `GET /items/{item_id}` - アイテム取得（パラメータ付き）
- `GET /users` - ユーザー一覧取得
- `POST /users` - ユーザー作成

### API ドキュメント

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 開発

コードを変更すると自動的にリロードされます。

### 停止

```bash
docker-compose down
```