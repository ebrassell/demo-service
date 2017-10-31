import json
import os
from slackclient import SlackClient
for k in os.environ.keys():
    print(k)
    print('=  '+os.environ[k])
slack_token = os.environ["SLACK_API_TOKEN"]
slack_channel = os.environ["SLACK_CHANNEL"]
slack_emoji = os.environ["SLACK_EMOJI"]
slack_username = os.environ["SLACK_USERNAME"]
sc = SlackClient(slack_token)

def goodbye(event, context):
    body = {
        "message": "Goodbye",
        "input": event
    }

    sc.api_call("chat.postMessage",
                channel=slack_channel,
                text='Goodbye',
                username=slack_username,
                icon_emoji=slack_emoji)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
