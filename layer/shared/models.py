from pydantic import BaseModel, Json
from aws_lambda_powertools.utilities.parser.models import APIGatewayProxyEventModel
from typing import List, Optional

class TradeNotification(BaseModel):
    ticker: str
    action: str
    quantity: int

class SpotTrade(BaseModel):
    ticker: str
    action: str
    quantity: int

class SpotTradeAPIEvent(APIGatewayProxyEventModel):
    body: Json[SpotTrade]