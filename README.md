# Robinhood Parser
A selenium-based parser to extract trading history

## How to use
1. Put the company symobol and corrsponding robinhood url in `company_mapper` array

```python
def company_mapper():
  return [ 
    ('NFLX', "https://robinhood.com/history/81733743-965a-4d93-b87a-6973cb9efd34"),
  ]
```


2. Open your console and input `python parser.py`, You will have to login your Robinhood account, also 2FA if you have it on.
   
```
# output
NFLX https://robinhood.com/history/81733743-965a-4d93-b87a-6973cb9efd34
[(1, 200), (-1, 100.00), (-1, 300)]

# Total money that have spent in buying NFLX
NFLX -200
3. Support customized mapper `python parser.py -c`. You need to create a `custom_mapper.json` file as follow
```json
{
   "AAPL": "https://robinhood.com/history/450dfc6d-5510-4d40-abfb-f633b7d9be3e",
  "AMZN": "https://robinhood.com/history/c0bb3aec-bd1e-471e-a4f0-ca011cbec711",
  ...
}
```

## Setup
1. Set up selenium webdriver in env `PATH` or use `driver.Chrome(your_path)` instead

## Requirement

1. selenium webdriver
2. python v3.7


