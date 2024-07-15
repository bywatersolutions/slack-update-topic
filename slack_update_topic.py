from slack_bolt import App
import datetime
import math
import os

def get_channel_id(self, channel_name):
    for result in self.client.conversations_list():
        for channel in result['channels']:
            if channel['name'] == channel_name:
                return channel['id']
    return None

weeks = math.floor( ( (datetime.datetime.now(datetime.UTC) - datetime.datetime(2024,1,1,0,0,0,0,datetime.UTC)).days / 7 ) )

topic = ""
if weeks % 2 == 0:
    topic = os.environ.get("SLACK_TOPIC_EVEN")
else:
    topic = os.environ.get("SLACK_TOPIC_ODD")

# Initializes your app with your bot token and socket mode handler
slack_bot_token = os.environ.get("SLACK_BOT_TOKEN")
slack_channel_name = os.environ.get("SLACK_CHANNEL_NAME") if os.environ.get("SLACK_CHANNEL_NAME") else "dev"
app = App(token=slack_bot_token)

channel_id = get_channel_id( app, slack_channel_name )
app.client.conversations_setTopic(channel=channel_id, topic=topic)
