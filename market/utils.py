import pandas as pd

def calculate_rsi(data, period=14):
    delta = data.diff()
    gain = delta.copy()
    loss = delta.copy()

    gain[gain < 0] = 0
    loss[loss > 0] = 0

    avg_gain = gain.ewm(com=period-1, adjust=False).mean()
    avg_loss = abs(loss.ewm(com=period-1, adjust=False).mean())

    rs = avg_gain / avg_loss
    rsi = 100 - (100/(1+rs))
    return rsi


def atr(df, n=14):
    data = df.copy()
    
    high = data['high']
    low = data['low']
    close = data['close']
    
    data['tr0'] = abs(high - low)
    data['tr1'] = abs(high - close.shift())
    data['tr2'] = abs(low - close.shift())
    
    data['tr'] = data[['tr0', 'tr1', 'tr2']].max(axis=1)
    
    # Use EMA (Exponential Moving Average) for ATR
    data['atr'] = data['tr'].ewm(span=n, adjust=False).mean()
    
    return data['atr']
