# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# #  Create 200 days
# days = 200

# # Generate random daily changes
# np.random.seed(42)  # for same result every time
# price_changes = np.random.normal(0, 1, days)

# #  Create stock price starting from 100
# price = 100 + np.cumsum(price_changes)

# # Create date range
# dates = pd.date_range(start="2024-01-01", periods=days)

# #  Create DataFrame
# df = pd.DataFrame({
#     "Date": dates,
#     "Close": price
# })

# df.set_index("Date", inplace=True)

# #  Create High, Low, Volume
# df["High"] = df["Close"] + np.random.uniform(0, 2, days)
# df["Low"] = df["Close"] - np.random.uniform(0, 2, days)
# df["Volume"] = np.random.randint(1000, 10000, days)

# #  Moving Average
# df["MA20"] = df["Close"].rolling(20).mean()

# #  Daily Return
# df["Daily Return"] = df["Close"].pct_change()

# print(df.head())

# # =====================
# #  VISUALIZATION
# # =====================

# # Closing Price
# plt.figure(figsize=(10,5))
# plt.plot(df["Close"])
# plt.title("Simulated Stock Closing Price")
# plt.show()
# # 
# # Moving Average
# plt.figure(figsize=(10,5))
# plt.plot(df["Close"], label="Close")
# plt.plot(df["MA20"], label="MA20")
# plt.legend()
# plt.title("Moving Average")
# plt.show()

# # Volume
# plt.figure(figsize=(10,5))
# plt.bar(df.index, df["Volume"])
# plt.title("Trading Volume")
# plt.show()

# # Daily Return
# plt.figure(figsize=(10,5))
# plt.plot(df["Daily Return"])
# plt.title("Daily Returns")
# plt.show()