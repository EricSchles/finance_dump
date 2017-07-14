from app import db

class FinancialData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_id = db.Column(db.String)
    stock_symbol = db.Column(db.String)
    financial_index = db.Column(db.String)
    last_trade_price = db.Column(db.Float)
    last_trade_with_currency = db.Column(db.Float)
    last_trade_datetime = db.Column(db.DateTime)
    dividend = db.Column(db.Float)
    stock_yield = db.Column(db.Float)
    
    
    def __init__(self,
                 stock_id,
                 stock_symbol,
                 financial_index,
                 last_trade_price,
                 last_trade_with_currency,
                 last_trade_datetime,
                 dividend,
                 stock_yield):
        self.stock_id = stock_id 
        self.stock_symbol = stock_symbol
        self.financial_index = financial_index
        self.last_trade_price = last_trade_price
        self.last_trade_with_currency = last_trade_with_currency
        self.last_trade_datetime = last_trade_datetime
        self.dividend = dividend
        self.stock_yield = stock_yield


    def __repr__(self):
        return '<id {}>'.format(self.id)

