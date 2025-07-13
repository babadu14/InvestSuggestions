from django.shortcuts import render
from market.models import CryptoPrice
from django.views.generic import ListView
from market.utils import calculate_rsi
import pandas as pd
from market.utils import atr

# Create your views here.

class DashboardView(ListView):
    model = CryptoPrice
    template_name = 'market/dashboard.html'
    context_object_name = 'prices'

    def get_queryset(self):
        coin = self.kwargs.get('coin', 'bitcoin')
        return CryptoPrice.objects.filter(coin=coin).order_by('-timestamp')[:24]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        coin = self.kwargs.get('coin', 'bitcoin')
        prices = CryptoPrice.objects.filter(coin=coin).order_by('-timestamp')[:24]
        prices = prices[::-1]  
        advice_text = "Not enough data"
        advice_key = None  
        suggested_leverage = '10x'
        latest_atr = None

        latest_price_obj = CryptoPrice.objects.filter(coin=coin).order_by('-timestamp').first()
        current_price = latest_price_obj.price if latest_price_obj else None

        price_values = [p.price for p in prices]

        if len(price_values) >= 14:
            price_series = pd.Series(price_values)
            rsi_series = calculate_rsi(price_series)
            latest_rsi = round(rsi_series.iloc[-1], 2)
            context['rsi'] = latest_rsi
        else:
            latest_rsi = None
            context['rsi'] = None

        ema = None
        if len(price_values) >= 10:
            ema = price_values[0]
            k = 2 / (len(price_values) + 1)
            for price in price_values[1:]:
                ema = price * k + ema * (1 - k)

        if latest_rsi and ema:
            if latest_rsi < 30 and price_values[-1] < ema:
                advice_text = "Go LONG (RSI oversold + price below EMA)"
                advice_key = "long"
            elif latest_rsi > 70 and price_values[-1] > ema:
                advice_text = "Go SHORT (RSI overbought + price above EMA)"
                advice_key = "short"
            else:
                advice_text = "No strong signal (RSI and EMA disagree)"
                advice_key = "neutral"
        elif latest_rsi:
            if latest_rsi < 30:
                advice_text = "Go LONG (RSI suggests oversold)"
                advice_key = "long"
            elif latest_rsi > 70:
                advice_text = "Go SHORT (RSI suggests overbought)"
                advice_key = "short"
            else:
                advice_text = "RSI is neutral"
                advice_key = "neutral"
        elif ema:
            if price_values[-1] < ema:
                advice_text = "Go LONG (price below EMA)"
                advice_key = "long"
            elif price_values[-1] > ema:
                advice_text = "Go SHORT (price above EMA)"
                advice_key = "short"
            else:
                advice_text = "Price is near EMA"
                advice_key = "neutral"
        else:
            advice_text = "Not enough data for advice"
            advice_key = None


        if len(price_values)>=24:
            if price_values[-3] < price_values[-2] < price_values[-1]:
                context['momentum'] = 'up' 
            elif price_values[-3] > price_values[-2] > price_values[-1]:
                context['momentum'] = 'down' 
            else:
                context['momentum'] = "flat"
        
        if len(price_values)>=14:
            if advice_text == "No strong signal (RSI and EMA disagree)" or advice_text == "Not enough data for advice":
                context['suggested_leverage'] = 'N/A'
            elif context['momentum'] == 'up' and latest_rsi < 30:
                context['suggested_leverage'] = '15x Strong LONG indicator'
            elif context['momentum'] =='down' and latest_rsi > 70:
                context['suggested_leverage'] = '15x Strong SHORT indicator'
            else:
                context['suggested_leverage'] = suggested_leverage
        else:
            advice_text = 'Not enough data'
        
        date_list = [p.timestamp.strftime('%Y-%m-%d') for p in prices]
        price_list = [p.price for p in prices]
 

        df = pd.DataFrame([{
            'timestamp': p.timestamp,
            'close': p.price,
            'high': p.price,  
            'low': p.price,   
        } for p in prices])

        if len(df) >= 14 and all(c in df.columns for c in ['high', 'low', 'close']):
            df['atr'] = atr(df)
            latest_atr = df['atr'].iloc[-1]
            context['atr'] = round(latest_atr, 2)



        def calculate_tp_sl_by_atr(position_type, current_price, atr_value, multiplier=1.5):
            if current_price is None or atr_value is None:
                return None, None

            tp = sl = None

            if position_type == 'long':
                tp = current_price + (multiplier * atr_value)
                sl = current_price - (multiplier * atr_value)
            elif position_type == 'short':
                tp = current_price - (multiplier * atr_value)
                sl = current_price + (multiplier * atr_value)

            return round(tp, 2), round(sl, 2)

        if current_price and advice_key in ['long', 'short'] and latest_atr:
            tp, sl = calculate_tp_sl_by_atr(advice_key, current_price, latest_atr)
        else:
            tp = sl = None
      

        context['tp'] = tp
        context['sl'] = sl
        context['atr'] = round(latest_atr, 2) if latest_atr else None
        context['coin'] = coin
        context['advice'] = advice_text
        context['date_list'] = date_list
        context['price_list'] = price_list

        return context


