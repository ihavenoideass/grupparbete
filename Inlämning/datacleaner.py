import logging
import pandas as pd

class DataCleaner:
    """Klass för att städa data, flyttar ticker till en egen kolumn och tar bort NaN-värden."""
    
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def clean_and_format_data(self, data):
        """Rengör och formaterar data hämtad från API."""
        # Logga att datacleaner har startats.
        self.logger.info('Startar datarensning och formatering från api.fetch_data')

        try:
            # Flytta ticker från MultiIndex till en egen kolumn
            data_cleaned = data.stack(level=0).reset_index()

            # Byt namn på kolumnerna om det behövs (justera baserat på hur din data ser ut)
            data_cleaned.columns = ['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

            # Ta bort rader med NaN
            data_cleaned = data_cleaned.dropna()

            # Kontrollera om datan är tom.
            if not data_cleaned.empty:
                self.logger.info('Datan har rensats och transformerats korrekt.')
                return data_cleaned  # Returnera rensad och formaterad data.
            else:
                # Om data tom, logga nedan
                self.logger.error('Datan kunde inte rensas, filen är tom efter transformering.')
                return None

        except Exception as e:
            # Logga eventuella fel som inträffar under processen.
            self.logger.error(f'Ett fel uppstod vid datacleaner.py processen: {e}')
            return None
