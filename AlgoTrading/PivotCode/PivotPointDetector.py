
# looking for candlestick formations
def pivotid(df1, l, n1, n2):  # n1 n2 before and after candle l
    if l - n1 < 0 or l + n2 >= len(df1):
        return 0

    pividlow = 1
    pividhigh = 1
    for i in range(l - n1, l + n2 + 1):
        if (df1.low[l] > df1.low[i]):
            pividlow = 0
        if (df1.high[l] < df1.high[i]):
            pividhigh = 0
    if pividlow and pividhigh:
        return 3
    elif pividlow:
        return 1
    elif pividhigh:
        return 2
    else:
        return 0

def PointPos(x):
    if x['pivot'] == 1:
        return (x['low']-1e-3)
    elif x['pivot'] == 2:
        return (x['high']+1e-3)
    else:
        return np.nan
