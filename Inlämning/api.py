# pip install yfinance
# pip install TA-Lib
# https://ta-lib.org/functions/
# https://aroussi.com/post/python-yahoo-finance


import logging
import yfinance as yf
from datetime import datetime
import os



class API:
    """Klass för att hämta data från apiet yfinance."""

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def fetch_data(self, tickers, start, end):
        """Hämtar datan från yahoo finance med hjälp av ticker_symbol, start_date och end_date."""
        # Loggar att api.py har startats, vilka tickers o tidpunkter.
        self.logger.info(f'Hämtar datan för: {tickers} från och med {start} till och med {end}.')

        try:
            # Försöker ladda ned via apiet med mina variabler.
            data = yf.download(tickers, start=start, end=end, group_by="ticker", keepna=False)

            # Kontrollera om datan är tom.
            if not data.empty:
                self.logger.info(f'Data har hämtats korrekt för:  {tickers}')
                return data # Retunerar data om ej tom.
            
            # Om data tom, logga nedan.
            else:
                self.logger.error(f'Datan kunde inte hämtas, {tickers}, filen är tom')
                return None
            
        except Exception as e:
            # Logga eventuella fel som inträffar under processen.
            self.logger.error(f'Ett fel uppstod vid api.py processen: {e}')
            return None




