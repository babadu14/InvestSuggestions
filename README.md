# 💹 AI-Powered Crypto Dashboard

A Django-based web application that fetches real-time cryptocurrency price data, visualizes it with charts, and provides intelligent trading suggestions using technical indicators such as **RSI**, **EMA**, **momentum**, and **ATR-based TP/SL**. It also suggests a **leverage level** based on market signals.

---

## 🚀 Features

- 📊 Visualize price trends for top cryptocurrencies (e.g., Bitcoin, Ethereum, etc.)
- 🤖 AI-based trading advice (Go LONG / SHORT / NEUTRAL)
- 🔄 Technical indicators:
  - Relative Strength Index (RSI)
  - Exponential Moving Average (EMA)
  - Momentum Trend Detection
  - ATR-based Take Profit and Stop Loss
- ⚙️ Management command to fetch and store historical price data
- 💡 Suggested leverage level (e.g., 10x, 15x) based on signal strength
- 🕒 Hourly or daily chart support (based on data availability)

---

## 🧠 How It Works

1. **Fetch Data**: 
   - Management command hits the [CoinGecko API](https://www.coingecko.com/en/api) and stores price data in your database.
   
2. **Analyze**:
   - RSI: Measures overbought/oversold conditions.
   - EMA: Highlights recent trend strength.
   - Momentum: Analyzes direction consistency.
   - ATR: Calculates realistic stop loss / take profit levels.

3. **Suggest**:
   - Leverage suggestion is based on RSI + momentum.
   - TP/SL are calculated using ATR for dynamic market conditions.

---

## 🛠️ Tech Stack

- **Python** & **Django** for backend
- **Chart.js** for chart rendering
- **Pandas** for technical analysis
- **HTML/CSS** + Bootstrap (optional) for UI
- **SQLite** (default), but you can plug in PostgreSQL or MySQL

---

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/crypto-dashboard.git
   cd crypto-dashboard
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run migrations:

bash
Copy
Edit
python manage.py migrate
Fetch historical data:

bash
Copy
Edit
python manage.py fetch_prices
Start the server:

bash
Copy
Edit
python manage.py runserver
Go to: http://localhost:8000/dashboard/bitcoin

# ⚠️ Disclaimer
This tool is for educational purposes only and not financial advice. Trading cryptocurrencies is highly volatile and can result in financial losses. Use at your own risk.