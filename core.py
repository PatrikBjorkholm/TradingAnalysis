import pandas as pd

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