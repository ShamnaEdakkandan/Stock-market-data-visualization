import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

price_array = np.array(prices)
volume_array = np.array(volumes)

print(prices[:10])
print(volumes[:10])

data = pd.DataFrame({
    "Day": range(1,101),
    "Price": price_array,
    "Volume": volume_array
})

print(data.head())
data.to_csv("stock_data.csv", index=False)

data["Price Change"] = data["Price"].diff()

plt.plot(data["Day"], data["Price Change"])
plt.xlabel("Day")
plt.ylabel("Change")
plt.title("Daily Price Change")
plt.show()

# # price
# plt.plot(data["Day"], data["Price"])
# plt.xlabel("Day")
# plt.ylabel("Price")
# plt.title("Price Movement")
# plt.show()

# # Volume
# plt.plot(data["Day"], data["Volume"])
# plt.xlabel("Day")
# plt.ylabel("Volume")
# plt.title("Volume Movement")
# plt.show()

plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
# subplot(row,cols,position)
plt.plot(data["Day"], data["Price"])
plt.title("Price Movement")

plt.subplot(2,1,2)
plt.plot(data["Day"], data["Volume"])
plt.title("Volume Movement")

plt.tight_layout()
plt.show()

 