import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class StockAnalysis:

    def __init__(self, file):
        # load dataset
        self.df = pd.read_csv(file)

        # convert date column
        self.df['Date'] = pd.to_datetime(self.df['Date'])

        # extract year
        self.df['Year'] = self.df['Date'].dt.year

    # -------------------------------------------------

    def show_data(self):
        print("First 5 rows of dataset\n")
        print(self.df.head())

    # -------------------------------------------------

    def yearly_avg_close(self):

        yearly_price = self.df.groupby('Year')['Close'].mean()

        plt.figure(figsize=(10,5))
        plt.plot(yearly_price)

        plt.title("Average Closing Price Per Year")
        plt.xlabel("Year")
        plt.ylabel("Average Close Price")

        plt.show()

    # -------------------------------------------------

    def yearly_volume(self):

        yearly_volume = self.df.groupby('Year')['Volume'].sum()

        plt.figure(figsize=(10,5))
        plt.bar(yearly_volume.index, yearly_volume)

        plt.title("Total Trading Volume Per Year")
        plt.xlabel("Year")
        plt.ylabel("Total Volume")

        plt.show()

    # -------------------------------------------------

    def highest_price_yearly(self):

        yearly_high = self.df.groupby('Year')['High'].max()

        plt.figure(figsize=(10,5))
        plt.plot(yearly_high)

        plt.title("Highest Price Each Year")
        plt.xlabel("Year")
        plt.ylabel("Price")

        plt.show()

    # -------------------------------------------------

    def open_vs_close(self):

        yearly_open = self.df.groupby('Year')['Open'].mean()
        yearly_close = self.df.groupby('Year')['Close'].mean()

        plt.figure(figsize=(10,5))

        plt.plot(yearly_open,label="Open Price")
        plt.plot(yearly_close,label="Close Price")

        plt.title("Open vs Close Price")
        plt.xlabel("Year")
        plt.ylabel("Price")

        plt.legend()

        plt.show()

    # -------------------------------------------------

    def moving_average(self):

        self.df['MA50'] = self.df['Close'].rolling(window=50).mean()

        plt.figure(figsize=(10,5))

        plt.plot(self.df['Close'],label="Close Price")
        plt.plot(self.df['MA50'],label="50 Day Moving Avg")

        plt.title("Moving Average Analysis")

        plt.legend()

        plt.show()

    # -------------------------------------------------

    def daily_return(self):

        self.df['Daily Return'] = self.df['Close'].pct_change()

        plt.figure(figsize=(10,5))

        plt.hist(self.df['Daily Return'].dropna(), bins=50)

        plt.title("Daily Return Distribution")
        plt.xlabel("Daily Return")
        plt.ylabel("Frequency")

        plt.show()


# =========================================================
# MAIN PROGRAM
# =========================================================

stock = StockAnalysis("AAPL.csv")

stock.show_data()

stock.yearly_avg_close()

stock.yearly_volume()

stock.highest_price_yearly()

stock.open_vs_close()

stock.moving_average()

stock.daily_return()