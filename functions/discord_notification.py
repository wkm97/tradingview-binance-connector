import json
from typing import List
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.parser import envelopes, event_parser
import requests
import os

from shared.models import TradeNotification
from shared.discord import DiscordNotifier

logger = Logger()
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
notifier = DiscordNotifier(DISCORD_WEBHOOK)


# publish message by boto3.client('sns').publish(TopicArn=TRADE_SNS_TOPIC, Message=event.body.json())
@logger.inject_lambda_context
@event_parser(model=TradeNotification, envelope=envelopes.SnsEnvelope)
def lambda_handler(event: List[TradeNotification], _: LambdaContext) -> dict:
    data = event[0]
    message = f'Min Wei {data.action} {data.quantity} unit of {data.ticker}'
    notifier.send(message)



    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"status": "success"}),
    }
