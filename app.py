import random
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import schedule
import time

from notion import lists
from secret import SLACK_APP_TOKEN, SLACK_BOT_TOKEN

# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def handle_mention(body, say):
    choice = random.choice(lists())
    user = body["event"]["user"]

    event = body["event"]
    thread_ts = event.get("thread_ts", None) or event["ts"]

    say(f"🍚 점심 메뉴 추천: [{choice.category}] <{choice.url}|{choice.title}>", thread_ts=thread_ts)

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()