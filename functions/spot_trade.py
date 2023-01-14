from http import HTTPStatus
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.parser import event_parser
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler.exceptions import InternalServerError
from requests.models import Response
from binance import Client
import os
from shared.discord import DiscordNotifier

from shared.models import SpotTradeAPIEvent
from shared.http_responses import build_response

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
TRADE_SNS_TOPIC = os.getenv("TRADE_SNS_TOPIC")
STAGE_ENVIRONMENT = os.getenv("STAGE_ENVIRONMENT")
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

client = Client(
    BINANCE_API_KEY,
    BINANCE_API_SECRET,
    testnet=True if STAGE_ENVIRONMENT != "production" else False,
)



notifier = DiscordNotifier(DISCORD_WEBHOOK)
logger = Logger()


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@event_parser(model=SpotTradeAPIEvent)
def lambda_handler(event: SpotTradeAPIEvent, _: LambdaContext) -> dict:
    
    try:
        params = event.body
        order = client.order_limit(
            symbol=params.symbol,
            side=params.action,
            quantity=params.quantity,
            price=params.price,
        )

        message = f'Min Wei {params.action} {params.quantity} unit of {params.symbol} at {params.price}'
        notifier.send(message)

        return build_response(HTTPStatus.OK, order)
    except Exception as err:
        return build_response(HTTPStatus.INTERNAL_SERVER_ERROR, {"message": str(err)})
