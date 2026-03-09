import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def stock_data():
    prices=[]
    volumes=[]
    price=100
    for day in range(1,101):
        old_price=price

        if day%2==0:
            price+=2
        else:
            price-=1

        if price>old_price:
            volume=6000
        else:
            volume=3000

        prices.append(price)
        volumes.append(volume)
    return prices, volumes

def graphs(data):
    # data["Price Change"]=data["Price"].diff()
    # plt.plot(data["Day"],data["Price Change"])
    # plt.xlabel("Day")
    # plt.ylabel("Change")
    # plt.title("Daily Price Change")
    # plt.show()
    # plt.figure(figsize=(10,6))

    plt.subplot(2,1,1)
    plt.plot(data["Day"], data["Price"],color="blue")
    plt.title("Price Movement")

    plt.subplot(2,1,2)
    plt.bar(data["Day"], data["Volume"],color="gray")
    plt.title("Volume Movement")

    plt.tight_layout()
    plt.show()
    
prices, volumes=stock_data()
price_array=np.array(prices)
volume_array = np.array(volumes)
data=pd.DataFrame({
    "Day": range(1, 101),
    "Price": price_array,
    "Volume": volume_array
})
data.to_csv("stock_data.csv", index=False)
graphs(data)