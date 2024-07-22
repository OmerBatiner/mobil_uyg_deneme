import yfinance as yf

def get_stock_data(ticker, period="1d", interval="1m"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    return hist

# Örnek kullaným
if __name__ == "__main__":
    data = get_stock_data("AAPL")
    print(data)
