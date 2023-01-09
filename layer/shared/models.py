import json
from pydantic import BaseModel, Json
from aws_lambda_powertools.utilities.parser.models import APIGatewayProxyEventModel

class TradeNotification(BaseModel):
    symbol: str
    action: str
    quantity: int
    price: int

class SpotTradeParams(BaseModel):
    symbol: str
    action: str
    quantity: int
    price: int

class SpotTradeAPIEvent(APIGatewayProxyEventModel):
    body: Json[SpotTradeParams]  # type: ignore[assignment]