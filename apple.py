import pandas as pd
import matplotlib.pyplot as plt

def new_data():
    data = pd.read_csv("apple_data.csv")
    return data

def process_data(data):
    data["Date"] = pd.to_datetime(data["Date"], utc=True)
    data["Daily Change"] = data["Close"].diff()
    
    return data

def graphs(data):
    plt.figure(figsize=(10,5))
    plt.plot(data["Date"], data["Daily Change"], color="purple")
    plt.title("Daily Price Change")
    plt.xlabel("Date")
    plt.ylabel("Change")
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10,5))
    plt.plot(data["Date"], data["Close"], color="blue")
    plt.title("Closing Price Movement")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.xticks(rotation=45)
    plt.show()

data = new_data()
data = process_data(data)
graphs(data)