import json
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.parser import event_parser
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger
from binance import Client
import os

from shared.models import SpotTradeAPIEvent

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
TRADE_SNS_TOPIC = os.getenv("TRADE_SNS_TOPIC")

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

logger = Logger()

# @logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@event_parser(model=SpotTradeAPIEvent)
def lambda_handler(event: SpotTradeAPIEvent, _: LambdaContext) -> dict:
    
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": "hello",
    }