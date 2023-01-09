import os
from binance import Client
from binance.enums import SIDE_BUY

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
TRADE_SNS_TOPIC = os.getenv("TRADE_SNS_TOPIC")
# content of test_sample.py

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET, testnet=True)


def test_order():
    order = client.order_limit(
        symbol="ETHUSDT",
        side="BUY",
        quantity=0.1,
        price=1000
    )
    print(order)