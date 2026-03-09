import pandas as pd
import matplotlib.pyplot as plt


def load_data():

    data = pd.read_csv("apple_data.csv")

    # convert date
    data["Date"] = pd.to_datetime(data["Date"], utc=True)

    # sort by date
    data = data.sort_values("Date")

    return data


def graphs(data):

    # daily change
    data["Daily Change"] = data["Close"] - data["Open"]

    plt.figure(figsize=(12,10))

    # 1 price trend
    plt.subplot(3,1,1)
    plt.plot(data["Date"], data["Close"])
    plt.title("Closing Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price")

    # 2 high low
    plt.subplot(3,1,2)
    plt.plot(data["Date"], data["High"], label="High")
    plt.plot(data["Date"], data["Low"], label="Low")
    plt.title("High vs Low Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()

    # 3 daily change
    plt.subplot(3,1,3)
    plt.bar(data["Date"], data["Daily Change"])
    plt.title("Daily Price Change")
    plt.xlabel("Date")
    plt.ylabel("Change")

    plt.tight_layout()
    plt.show()

    # 4 price distribution
    plt.figure()

    plt.hist(data["Close"], bins=20)

    plt.title("Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Frequency")

    plt.show()


data = load_data()

graphs(data)