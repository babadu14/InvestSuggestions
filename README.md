🚀 Crypto Trading Assistant Dashboard
A Django-based web application that analyzes recent cryptocurrency price movements using technical indicators like RSI, EMA, ATR, and momentum to provide trading advice, leverage suggestions, and take-profit/stop-loss levels.


🧠 Features
📊 Price Tracking for multiple coins (e.g., Bitcoin, Ethereum, Solana, Ripple).

📈 RSI (Relative Strength Index): Detects overbought/oversold conditions.

📉 EMA (Exponential Moving Average): Identifies trend direction.

📦 ATR (Average True Range): Used for realistic TP/SL levels based on volatility.

🧭 Momentum Detection: Checks short-term trends (up/down/flat).

🔮 Smart Trading Advice: Based on the combination of RSI + EMA.

⚖️ Leverage Suggestions: Dynamically adjusts based on signal strength.

✅ Built with Django class-based views and background management commands for fetching real-time data.

🏗️ How It Works
Data Fetching
A Django management command fetches crypto price data from the CoinGecko API every day/hour (depending on your plan).

Analysis
The dashboard uses technical indicators:

RSI: Over 70 = sell, below 30 = buy

EMA: If price > EMA = upward trend

ATR: Used to calculate TP and SL

Momentum: Analyzes 3-candle trend

Advice & Leverage
Based on the above, the app gives:

Trade direction: LONG / SHORT

TP & SL points

Suggested leverage (e.g., 10x, 15x) based on confidence

🧪 Tech Stack
Backend: Django (Python)

Data Source: CoinGecko API

Front-end: Django templates (HTML/CSS)

Database: SQLite (by default)

Visualization: Simple price chart using chart data

🚀 Getting Started
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/yourusername/crypto-trading-dashboard.git
cd crypto-trading-dashboard
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Apply migrations and create a superuser
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
4. Fetch price data
bash
Copy
Edit
python manage.py fetch_crypto_prices
5. Run the server
bash
Copy
Edit
python manage.py runserver
⚠️ Disclaimer
This project is for educational purposes only.
It does not provide financial advice. Trading cryptocurrencies involves high risk, and past performance does not guarantee future results.

🙌 Contributing
Contributions are welcome! Feel free to fork the repository and create a pull request with improvements or new indicators.
