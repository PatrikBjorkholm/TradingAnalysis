import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as make_subplots
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from AlgoTrading.PivotCode import PivotPointDetector as PPD


# Read and clean out data ans null values
df = pd.read_csv('./Data/EURUSD_Candlestick_1_Hour_BID_04.05.2003-15.04.2023_2.csv', sep=',')

#print(df.headers)
#df.columns['time','open','high','low','close','volume']
df = df[df['volume'] != 0]
df.reset_index(drop=True,inplace=True)
df.isna().sum()

print(df.head(10))

# Look for pivot points
df['pivot'] = df.apply(lambda x: PPD.pivotid(df, x.name,10,10), axis=1)

print(df.head(10))
print(df.head(-10))
df['pointpos'] = df.apply(lambda row: PPD.PointPos(row), axis=1)

dfpl = df[-300:-1]

fig = go.Figure(data=[go.Candlestick(x=dfpl.index,open=dfpl['open'],high=dfpl['high'],
                                     low=dfpl['low'],close=dfpl['close'],increasing_line_color='green',
                                     decreasing_line_color='red')])

fig.add_scatter(x=dfpl.index, y=dfpl['pointpos'], mode="markers", marker=dict(size=5,color="MediumPurple"),name="pivot")
fig.update_layout(xaxis_rangeslider_visible=False)
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.update_layout(paper_bgcolor='black',plot_bgcolor='black')

#fig.show()

# Find resistance levels

dfkeys = df[:]

# Filter the dataframe based on the pivot column
high_values = dfkeys[dfkeys['pivot'] == 2]['high']
low_values = dfkeys[dfkeys['pivot'] == 1]['low']

# Define the bin width
bin_width = 0.003  # Change this value as needed

# Calculate the number of bins
bins = int((high_values.max() - low_values.min()) / bin_width)

print((high_values))


# Create the histograms
plt.figure(figsize=(10, 5))
plt.hist(high_values, bins=bins, alpha=0.5, label='High Values', color='red')
plt.hist(low_values, bins=bins, alpha=0.5, label='Low Values', color='blue')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of High and Low Values')
plt.legend()

#plt.show()