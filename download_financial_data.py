from app.models import FinancialData
from googlefinance import getQuotes
import json
from app import db
from datetime import datetime

stock_data = getQuotes('AAPL')[0]

fin_data = FinancialData(
    stock_id=stock_data["ID"],
    stock_symbol=stock_data["StockSymbol"],
    financial_index=stock_data["Index"],
    last_trade_price=stock_data["LastTradePrice"],
    last_trade_with_currency=stock_data["LastTradeWithCurrency"],
    last_trade_datetime=datetime.strptime(stock_data["LastTradeDateTime"], "%Y-%m-%dT%H:%M:%SZ"),
    dividend=stock_data["Dividend"],
    stock_yield=stock_data["Yield"])
db.session.add(fin_data)
db.session.commit()
