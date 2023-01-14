import json
from pydantic import BaseModel, Json
from aws_lambda_powertools.utilities.parser.models import APIGatewayProxyEventModel

class TradeNotification(BaseModel):
    symbol: str
    action: str
    quantity: int
    price: float

class SpotTradeParams(BaseModel):
    passphrase: str
    symbol: str
    action: str
    quantity: int
    price: float

class SpotTradeAPIEvent(APIGatewayProxyEventModel):
    body: Json[SpotTradeParams]  # type: ignore[assignment]