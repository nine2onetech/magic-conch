# 마법의 소라고둥

## Overview

마법의 소라고둥은 노션 API 를 활용한 슬랙봇입니다.

## Getting Started


```shell
source .venv/bin/activate
```

```shell
pip install -r requirements.txt
```

Create a file called `secret.py` for establishing a connection between Slack and Notion. It is important to note that this file should not be uploaded to a public repository.

```python
SLACK_BOT_TOKEN = "xoxb-YOUR_SLACK_BOT_TOKEN}"
SLACK_APP_TOKEN = "xapp-YOUR_SLACK_APP_TOKEN"
NOTION_API_TOKEN = "secret_YOUR-NOTION-API-TOKEN"
DATABASE_ID = "NOTION_DATABASE_ID"
```

Alternatively, the values set in the environment variables can also be used.

```python
import os

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
NOTION_API_TOKEN = os.environ.get("NOTION_API_TOKEN")
DATABASE_ID = os.environ.get("NOTION_DATABASE_ID")
```

Let's Start!

```shell
python3 app.py
```