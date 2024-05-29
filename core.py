import pandas as pd

# Read and clean out data ans null values
df = pd.read_csv("./Data/EURUSD_Candlestick_1_Hour_BID_04.05.2003-15.04.2023")
df.columns['time','open','high','low','close','volume']
df[df['volume']!=0]
df.reset_index(drop=True,inplace=True)
df.isna().sum()