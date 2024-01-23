## Installation
- Faite dans l'environneemnt conda (taskweaver env)
- Suivre les instructions
- Attention : le fichier "taskweaver_config.json" doit être mis dans C:\Users\test\Documents\Formation IA\taskweaver\TaskWeaver\ **project** pour être reconnu
- Le fichier "taskweaver_config.json" en local: 
```Python
{
    "llm.api_base": "http://localhost:1234/v1",
    "llm.api_key": "anything",
    "llm.model": "local llm"
  }
```
- Installer aussi chainlit:
![Capture d'écran 2024-01-22 142201](https://github.com/jpbrasile/formationIA2.0/assets/8331027/11c8a1a5-2f88-4ea2-9177-78f7917d6172)


![Capture d'écran 2024-01-22 141630](https://github.com/jpbrasile/formationIA2.0/assets/8331027/58ee0298-aa10-44c2-b83e-1e2ca77eeac9)

- Taskweaver a la capacité de lire des fichiers locaux. En fait il crée le code ad hoc pour y arriver ! Malheureusement il perd du temps à itérer car les bibliothèques requises ne sont pas charger au départ ! Il perd donc quelques itérations à le constater et à faire les "pip install" nécessaires.
- Donc bien que très lent , taskweaver a une fonctionnalité intéressante: il crée le code pour se donner des fonctionnalités manquantes  et l'exécute ensuite...
- [Des plugins (codes disponibles pour être exécuté en fonction du contexte)](https://www.youtube.com/watch?v=o4zmEEKvdTY) existe aussi.
- Il suffit d'ajouter dans le répertoire "C:\Users\test\Documents\Formation IA\taskweaver\TaskWeaver\project\plugins", les fichiers suivant (c'est un exemple)
**stock_price.yaml**
```Python
  name: stock_price
enabled: true
required: false
description: >-
  The StockPricePlugin connects to the Yahoo Finance API using yfinance to fetch
  real-time stock market data. It retrieves and returns the latest stock price
  information based on the provided stock symbol, including the current market price.

parameters:
  - name: stock_symbol
    type: str
    required: true
    description: The stock symbol for which the current market price is to be retrieved.

returns:
  - name: stock_data
    type: dict
    description: >-
      A dictionary containing the stock symbol and its current market price. The format is:
      {
        "symbol": <stock_symbol>,
        "current_price": <current_market_price>
      }
```
**stock_price.py**
```Python
import yfinance as yf
from taskweaver.plugin import Plugin, register_plugin

# Define the detailed prompt for the plugin
stock_price_prompt = r"""
This plugin is designed to fetch real-time stock market data. It performs the following tasks:
- Retrieves the latest stock price information based on the provided stock symbol.
- Extracts key financial details such as the current market price.
- Finally, it returns this information in a structured dictionary format, as shown below:
  {
    "symbol": <stock_symbol>,
    "current_price": <current_market_price>
  }
"""

@register_plugin
class StockPricePlugin(Plugin):
    def __call__(self, stock_symbol: str):
        # Fetch stock data using yfinance
        stock = yf.Ticker(stock_symbol)

        # Check if stock exists and has info
        if not stock.info:
            return {"error": f"No data found for symbol: {stock_symbol}"}

        # Extract the current stock price
        current_price = stock.history(period="1d")['Close'].iloc[-1]

        # Check if current price is available
        if current_price is None:
            return {"error": f"Current price not available for symbol: {stock_symbol}"}

        # Return a dictionary containing the stock symbol and its current price
        return {
            "symbol": stock_symbol,
            "current_price": current_price
        }
```
