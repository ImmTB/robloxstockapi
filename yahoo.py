import platform
import datetime
print('Python Version = ' + platform.python_version())
import yfinance as yf
print('yfinance version = ' + yf.__version__)

def yfinancetut(tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    investment = ('Company: ' + tickerinfo['shortName'])
    print(investment)
    costHigh = ('High: ', tickerinfo['regularMarketDayHigh'])
    print(costHigh)
    costLow = ('Low: ', tickerinfo['regularMarketDayLow'])
    print(costLow)
    ask = ('Ask: ', tickerinfo['ask'])
    print(ask)

yfinancetut('RBLX')