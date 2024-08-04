import pandas as pd
import yfinance as yf
from datetime import datetime
import numpy as np

from pydantic import BaseModel
from crewai.tools import tool
from src.utils.financial_calculations import (
    calculate_beta,
    calculate_max_drawdown,
    calculate_sharpe_ratio,
    calculate_sortino_ratio,
    calculate_rsi,
    calculate_macd,
    analyze_trend,
    analyze_macd,
    analyze_rsi
)

class BasicStockInfoSchema(BaseModel):
    ticker: str
@tool
def get_basic_stock_info(ticker: str) -> pd.DataFrame:
    """Retrieves basic information about a single stock from Yahoo Finance."""
    stock = yf.Ticker(ticker)
    info = stock.info  # Deprecation note: This might change in future yfinance versions.
    
    basic_info = pd.DataFrame({
        'Name': [info.get('longName', 'N/A')],
        'Sector': [info.get('sector', 'N/A')],
        'Industry': [info.get('industry', 'N/A')],
        'Market Cap': [info.get('marketCap', 'N/A')],
        'Current Price': [info.get('currentPrice', 'N/A')],
        '52 Week High': [info.get('fiftyTwoWeekHigh', 'N/A')],
        '52 Week Low': [info.get('fiftyTwoWeekLow', 'N/A')],
        'Average Volume': [info.get('averageVolume', 'N/A')]
    })
    return basic_info


@tool
def get_fundamental_analysis(ticker: str, period: str = '1y') -> pd.DataFrame:
    """
    Performs fundamental analysis on a given stock for a specific period.
    """
    stock = yf.Ticker(ticker)
    history = stock.history(period=period)
    info = stock.info
    
    fundamental_analysis = pd.DataFrame({
        'PE Ratio': [info.get('trailingPE', 'N/A')],
        'Forward PE': [info.get('forwardPE', 'N/A')],
        'PEG Ratio': [info.get('pegRatio', 'N/A')],
        'Price to Book': [info.get('priceToBook', 'N/A')],
        'Dividend Yield': [info.get('dividendYield', 'N/A')],
        'EPS (TTM)': [info.get('trailingEps', 'N/A')],
        'Revenue Growth': [info.get('revenueGrowth', 'N/A')],
        'Profit Margin': [info.get('profitMargins', 'N/A')],
        'Free Cash Flow': [info.get('freeCashflow', 'N/A')],
        'Debt to Equity': [info.get('debtToEquity', 'N/A')],
        'Return on Equity': [info.get('returnOnEquity', 'N/A')],
        'Operating Margin': [info.get('operatingMargins', 'N/A')],
        'Quick Ratio': [info.get('quickRatio', 'N/A')],
        'Current Ratio': [info.get('currentRatio', 'N/A')],
        'Earnings Growth': [info.get('earningsGrowth', 'N/A')],
        'Stock Price Avg (Period)': [history['Close'].mean()],
        'Stock Price Max (Period)': [history['Close'].max()],
        'Stock Price Min (Period)': [history['Close'].min()]
    })
    return fundamental_analysis


@tool
def get_stock_risk_assessment(ticker: str, period: str = "1y") -> pd.DataFrame:
    """Performs a risk assessment on a given stock."""
    stock = yf.Ticker(ticker)
    history = stock.history(period=period)
    
    # Calculate daily returns
    returns = history['Close'].pct_change().dropna()
    
    # Calculate risk metrics
    volatility = returns.std() * np.sqrt(252)  # Annualized volatility
    beta = calculate_beta(returns, '^GSPC', period)  # Beta vs S&P 500
    var_95 = np.percentile(returns, 5)               # 95% VaR
    max_drawdown = calculate_max_drawdown(history['Close'])
    sharpe = calculate_sharpe_ratio(returns)
    sortino = calculate_sortino_ratio(returns)
    
    risk_assessment = pd.DataFrame({
        'Annualized Volatility': [volatility],
        'Beta': [beta],
        'Value at Risk (95%)': [var_95],
        'Maximum Drawdown': [max_drawdown],
        'Sharpe Ratio': [sharpe],
        'Sortino Ratio': [sortino]
    })
    return risk_assessment


@tool
def get_technical_analysis(ticker: str, period: str = "1y") -> pd.DataFrame:
    """Perform technical analysis on a given stock."""
    stock = yf.Ticker(ticker)
    history = stock.history(period=period)
    
    # Calculate indicators
    history['SMA_50'] = history['Close'].rolling(window=50).mean()
    history['SMA_200'] = history['Close'].rolling(window=200).mean()
    history['RSI'] = calculate_rsi(history['Close'])
    history['MACD'], history['Signal'] = calculate_macd(history['Close'])
    
    latest = history.iloc[-1]
    
    analysis = pd.DataFrame({
        'Indicator': [
            'Current Price',
            '50-day SMA',
            '200-day SMA',
            'RSI (14-day)',
            'MACD',
            'MACD Signal',
            'Trend',
            'MACD Signal',
            'RSI Signal'
        ],
        'Value': [
            f'${latest["Close"]:.2f}',
            f'${latest["SMA_50"]:.2f}',
            f'${latest["SMA_200"]:.2f}',
            f'{latest["RSI"]:.2f}',
            f'{latest["MACD"]:.2f}',
            f'{latest["Signal"]:.2f}',
            analyze_trend(latest),
            analyze_macd(latest),
            analyze_rsi(latest)
        ]
    })
    return analysis


@tool
def get_stock_news(ticker: str, limit: int = 10) -> pd.DataFrame:
    """Fetch recent news articles related to a specific stock."""
    stock = yf.Ticker(ticker)
    news = stock.news[:limit]
    
    news_data = []
    for article in news:
        news_entry = {
            "Title": article['title'],
            "Publisher": article['publisher'],
            "Published": datetime.fromtimestamp(article['providerPublishTime']).strftime('%Y-%m-%d %H:%M:%S'),
            "Link": article['link']
        }
        news_data.append(news_entry)
    
    return pd.DataFrame(news_data)
