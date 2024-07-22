import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_stock_data(data, ticker):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=data['Close'], label=ticker)
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig(f"{ticker}_stock_plot.png")  # Grafiði dosyaya kaydediyoruz
    plt.close()

def calculate_statistics(data):
    mean_price = data['Close'].mean()
    std_dev = data['Close'].std()
    moving_average = data['Close'].rolling(window=5).mean()
    price_change = data['Close'].pct_change().iloc[-1] * 100  # Yüzdelik deðiþim
    stats = {
        'mean_price': mean_price,
        'std_dev': std_dev,
        'moving_average': moving_average,
        'price_change': price_change
    }
    return stats

# Örnek kullaným
if __name__ == "__main__":
    from data_fetcher import get_stock_data
    
    data = get_stock_data("AAPL")
    plot_stock_data(data, "AAPL")
    stats = calculate_statistics(data)
    print(stats)
