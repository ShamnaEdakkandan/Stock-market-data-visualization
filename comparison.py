import pandas as pd
import matplotlib.pyplot as plt

class StockComparison:
    def __init__(self,apple_file,msft_file):
        self.apple=pd.read_csv(apple_file)
        self.msft=pd.read_csv(msft_file)
        self.apple['Date']=pd.to_datetime(self.apple['Date'])
        self.msft['Date']=pd.to_datetime(self.msft['Date'])
        self.apple['Year']=self.apple['Date'].dt.year
        self.msft['Year']=self.msft['Date'].dt.year

    def price_graph(self):
        plt.figure(figsize=(10,8))
        plt.subplot(2,1,1)
        plt.plot(self.apple['Date'],self.apple['Close'],color="green")
        plt.title("Apple Stock Price")
        plt.xlabel("Year")
        plt.ylabel("Close Price")
        plt.grid(True)

        plt.subplot(2,1,2)
        plt.plot(self.msft['Date'],self.msft['Close'],color="blue")
        plt.title("Microsoft Stock Price")
        plt.xlabel("Year")
        plt.ylabel("Close Price")
        plt.tight_layout()
        plt.grid(True)
        plt.show()
        
    def volume_graph(self):
        apple_vol = self.apple.groupby('Year')['Volume'].sum()
        msft_vol = self.msft.groupby('Year')['Volume'].sum()
        plt.figure(figsize=(10,8))

        plt.subplot(2,1,1)
        plt.bar(apple_vol.index,apple_vol,color="green")
        plt.title("Apple Trading Volume")
        plt.xlabel("Year")
        plt.ylabel("Volume")
        plt.grid(True)

        plt.subplot(2,1,2)
        plt.bar(msft_vol.index,msft_vol,color="blue")
        plt.title("Microsoft Trading Volume")
        plt.xlabel("Year")
        plt.ylabel("Volume")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

stock = StockComparison("AAPL.csv","MSFT.csv")
stock.price_graph()
stock.volume_graph()