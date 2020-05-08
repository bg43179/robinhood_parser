# Robinhood Parser
A selenium-based parser to extract trading history

## Why
Robinhood already have the summary, why do I need to parse the data on my own? [Read this](https://medium.com/@bg43179/why-dont-i-use-robinhood-s-average-price-d70c9383c6af)

## How to use
1. You need to edit exisitng  `defualt_mapper.json` file as follow
```json
{
  "AAPL": "https://robinhood.com/history/450dfc6d-5510-4d40-abfb-f633b7d9be3e",
  "AMZN": "https://robinhood.com/history/c0bb3aec-bd1e-471e-a4f0-ca011cbec711"
}
```

2. Open your console and input

```shell
#input
python parser.py [-e] [-c file_path]
```

- The browser will ask you to login your Robinhood account, also 2FA if you have it on.

``` shell
# output
MSFT - cost: -2964.42, equity: 3632.00, profit: 667.58
NFLX - cost: 240.12, equity: 0.00, profit: 240.12
...
```


## Setup
1. Set up selenium webdriver in env `PATH` or use `driver.Chrome(your_path)` instead

## Requirement

1. selenium webdriver
2. python v3.7


