import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def stock_data():
    dates = []
    opens = []
    highs = []
    lows = []
    closes = []
    volumes = []

    price = 100
    start_date = datetime(2026, 2, 25)

    for day in range(1, 101):
        old_price = price
        if day % 2 == 0:
            price += 2
        else:
            price -= 1

        volume = 6000 if price > old_price else 3000

        open_price = old_price
        close_price = price
        high_price = max(open_price, close_price)  
        low_price = min(open_price, close_price)  

        dates.append(start_date + timedelta(days=day-1))
        opens.append(open_price)
        highs.append(high_price)
        lows.append(low_price)
        closes.append(close_price)
        volumes.append(volume)

    return dates, opens, highs, lows, closes, volumes

def graphs(data):
    data["Daily Change"] = data["Close"].diff()

    plt.plot(data["Date"], data["Daily Change"], color="purple")
    plt.xlabel("Date")
    plt.ylabel("Change")
    plt.title("Daily Price Change")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10,6))

    plt.subplot(2,1,1)
    plt.plot(data["Date"], data["Close"], color="blue", label="Close")
    plt.plot(data["Date"], data["High"], color="green", linestyle="--", label="High")
    plt.plot(data["Date"], data["Low"], color="red", linestyle="--", label="Low")
    plt.plot(data["Date"], data["Open"], color="orange", linestyle=":", label="Open")
    plt.title("Price Movement ")
    plt.legend()

    plt.subplot(2,1,2)
    plt.bar(data["Date"], data["Volume"], color="gray")
    plt.title("Volume Movement")

    plt.tight_layout()
    plt.show()
dates, opens, highs, lows, closes, volumes = stock_data()

data = pd.DataFrame({
    "Date": dates,
    "Open": opens,
    "High": highs,
    "Low": lows,
    "Close": closes,
    "Volume": volumes
})

data.to_csv("stock_last_data.csv", index=False)

graphs(data)