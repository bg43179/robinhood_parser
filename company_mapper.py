import json

def default_mapper():
  return [ 
    ('AAPL', "https://robinhood.com/history/450dfc6d-5510-4d40-abfb-f633b7d9be3e"),
    ('CVX', "https://robinhood.com/history/7a6a30e2-cf4d-40dd-8baa-0cea48de85e4"),
    ('DIS', "https://robinhood.com/history/2ed64ef4-2c1a-44d6-832d-1be84741dc41"),
    ('JPM', "https://robinhood.com/history/43c1172a-9130-420a-ac9b-b01a6ff5dd54"),
    ('KO', "https://robinhood.com/history/bb9a01df-5982-42d4-88db-8662f23cdab5"),
    ('MSFT', "https://robinhood.com/history/50810c35-d215-4866-9758-0ada4ac79ffa"),
    ('NFLX', "https://robinhood.com/history/81733743-965a-4d93-b87a-6973cb9efd34"),
    ('T', "https://robinhood.com/history/2b456f6a-3287-4757-abf9-327383d2c708"),
  ]

def custom_mapper():
  f = open('./custom_mapper.json',) 
  data = json.load(f) 
  
  return list(data.items())