from datetime import datetime, timezone
import time
from django.core.management.base import BaseCommand
from market.models import CryptoPrice
import requests

class Command(BaseCommand):
    help = 'Fetches historical price data for selected cryptocurrencies from CoinGecko'

    def handle(self, *args, **options):
        coins = ['bitcoin', 'ethereum', 'solana', 'ripple']
        days = 7                                                                                        

        for coin in coins:
            print(f'Fetching data for {coin}...')
            time.sleep(1.5)

            url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days={days}'

            try:
                response = requests.get(url)
                data = response.json()

                for timestamp, price in data.get('prices', []):
                    dt = datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc)

                    if not CryptoPrice.objects.filter(coin=coin, timestamp=dt).exists():
                        CryptoPrice.objects.create(
                            coin=coin,
                            timestamp=dt,
                            price=price
                        )
                        print(f'Saved: {coin} - {dt} - ${price:.2f}')
                    else:
                        print(f'Already exists: {coin} - {dt}')
            
            except Exception as e:
                print(f'Failed to fetch {coin}: {e}')