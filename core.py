import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.subplots as make_subplots
from datetime import datetime
import numpy
def PointPos(x):
    if(x['pivot'] == 1):
        return x['low']-1e-3
    elif(x['pivot'] == 2):
        return x['high']+1e-3
    else:
        return np.nan

# looking for candlestick formations
def PivotID(df1,l,n1,n2):
    if(l-n1<0 or l+n2>0):
        return 0

    pividlow = 1
    pividhigh = 1

    for i in range(l-n1,l+n2+1):
        if(df1.low[1]>df1.low[i]):
            pividlow=0
        if(df1.high[1]<df1.high[i]):
            pividhigh=0
        if pividhigh and pividlow:
            return 3
        elif pividlow:
            return 1
        elif pividhigh:
            return 2
        else:
            return 0






# Read and clean out data ans null values
df = pd.read_csv('./Data/EURUSD_Candlestick_1_Hour_BID_04.05.2003-15.04.2023.csv', sep=',')
#df.columns['time','open','high','low','close','volume']
df[df['volume']!=0]
df.reset_index(drop=True,inplace=True)
df.isna().sum()
# Look for pivot points
df['pivot'] = df.apply(lambda x: PivotID(df,x.name,10,10),axis=1)
df['pointpos'] = df.apply(lambda row: PointPos(row), axis=1)

print(df.head())

# Print Figure

dfpl = df[-300:-1]
fig = go.Figure(data=[go.Candlestick(x=dfpl.index,open=dfpl['open'],high=dfpl['high'],
                                     low=dfpl['low'],close=dfpl['close'],increasing_line_color='green',
                                     decreasing_line_color='red')])

fig.add_scatter(x=dfpl.index, y =dfpl['pointpos'], mode="markers", marker=dict(size=5,color="MediumPurple"),name="pivot")
fig.update_layout(xaxis_rangeslider_visible=False)
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.update_layout(paper_bgcolor='black',plot_bgcolor='black')

fig.show()
