from typing import List, SupportsBytes
from swagger_server.constants import DbStockSector
from swagger_server.db_models.db_ticker import DbTicker
import requests
import yfinance as yf

url = 'https://finnhub.io/api/v1/stock/symbol?exchange=US&token='
token = 'c171qkv48v6se55vjibg'


def getSector(str):
    if str == DbStockSector.BASIC_MATERIALS.value:
        return DbStockSector.BASIC_MATERIALS.name
    elif str == DbStockSector.INDUSTRIALS.value:
        return DbStockSector.INDUSTRIALS.name
    elif str == DbStockSector.FINANCIAL_SERVICES.value:
        return DbStockSector.FINANCIAL_SERVICES.name
    elif str == DbStockSector.ENERGY.value:
        return DbStockSector.ENERGY.name
    elif str == DbStockSector.CONSUMER_CYCLICAL.value:
        return DbStockSector.CONSUMER_CYCLICAL.name
    elif str == DbStockSector.TECHNOLOGY.value:
        return DbStockSector.TECHNOLOGY.name
    elif str == DbStockSector.COMMUNICATION_SERVICES.value:
        return DbStockSector.COMMUNICATION_SERVICES.name
    elif str == DbStockSector.REAL_ESTATE.value:
        return DbStockSector.REAL_ESTATE.name
    elif str == DbStockSector.HEALTHCARE.value:
        return DbStockSector.HEALTHCARE.name
    elif str == DbStockSector.CONSUMER_DEFENSIVE.value:
        return DbStockSector.CONSUMER_DEFENSIVE.name
    elif str == DbStockSector.UTILITIES.value:
        return DbStockSector.UTILITIES.name
    elif str ==  DbStockSector.ETF.value:
        return DbStockSector.ETF.name
    # exception ones
    elif str == "Financial":
        return DbStockSector.FINANCIAL_SERVICES.name
    elif str == "ETF":
        return DbStockSector.ETF.name
    else:
        print("Sector didn't gottaaaaaaaaaaaaaaaaaaaaa: " + str)

def get_all_tickers(cls):
    response = requests.get(url + token)
    ticker_info_array = response.json()

    filtered_ticker_info_array = filter(lambda info: info["mic"] == "BATS", ticker_info_array)
    sorted_ticker_info_array = sorted(filtered_ticker_info_array, key=lambda info: info["mic"])
    print(len(sorted_ticker_info_array))
    for i in range(len(sorted_ticker_info_array)):
        print("index" + str(i))
        info = sorted_ticker_info_array[i]
        ticker = info["symbol"]

        collided_ticker: List[DbTicker] = cls.db.session.query(DbTicker).filter(DbTicker.ticker == ticker).all()
        if collided_ticker:
            print("already in database!")
            continue

        try:
            yTickerInfo = yf.Ticker(ticker).info
        except:
            continue
        dbTicker = DbTicker()
        
        dbTicker.ticker = ticker
        dbTicker.currency = info["currency"]
        dbTicker.market_code = info["mic"]
        
        if "sector" in yTickerInfo:
            if yTickerInfo["sector"] == '':
                continue
        elif yTickerInfo["quoteType"] != "ETF":
            continue
        dbTicker.sector = getSector(yTickerInfo["sector"] if "sector" in yTickerInfo else yTickerInfo["quoteType"])

        print("ticker " + ticker)
        print("sector " + dbTicker.sector)
        
        dbTicker.name = yTickerInfo["shortName"] if "shortName" not in yTickerInfo else yTickerInfo["longName"]
        dbTicker.description = yTickerInfo["longBusinessSummary"] if "longBusinessSummary" in yTickerInfo else ""
        cls.db.session.add(dbTicker)
        cls.db.session.flush()
        status = cls.db.session.commit()
        print(status)

