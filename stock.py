from number_helper import parse_dollar

class Transaction:
  def __init__(self, data):
    attrs = data.split('\n')
    self.action = attrs[0]
    self.multiplier = self.convert_action(attrs[0])
    self.date = attrs[1]
    self.amount = parse_dollar(attrs[2])
    self.shares = 0
    self.is_pending = False

    if len(attrs) == 4:
      if self.action != 'Dividend':
        self.shares = float(attrs[3].split(' ')[0])
      else:
        self.is_pending = True

  def convert_action(self, action):
    if action in ['Market Sell', 'Limit Sell', 'Dividend', 'Stop Loss Sell']:
      return 1

    return -1

class Stock:
  def __init__(self, symbol, history = []):
    self.symbol = symbol
    self.tansaction_history = history
    self.dividend_is_pending = False
    self.shares = 0
    self.total_cost = 0
    self.equity = 0
    self.dividend_gain = 0

  def performance(self):
    if self.gain_loss() > 0:
      return "{} - cost: {:.2f}, equity: {:.2f}, profit: \033[1;32;40m {:.2f}".format(self.symbol, abs(self.total_cost), self.equity, self.gain_loss())
    else:
      return "{} - cost: {:.2f}, equity: {:.2f}, profit: \033[1;31;40m {:.2f}".format(self.symbol, abs(self.total_cost), self.equity, self.gain_loss())

  def dividend(self):
    return "{} - profit: {:.2f}".format(self.symbol, self.dividend_gain)
    
  def parse(self, exclude_dividend = False):
    for t in self.tansaction_history:
      if exclude_dividend and t.action == 'Dividend':
        continue

      self.total_cost += t.multiplier * t.amount
      self.shares -= t.multiplier * t.shares

      if t.action == 'Dividend':
        self.dividend_is_pending |= t.is_pending
        self.dividend_gain += t.amount

  def gain_loss(self):
    return self.equity + self.total_cost

if __name__ == '__main__':
  # toss some unit test overhere
  all_history = [u'Dividend\nMay 15, 2020\n+$2.00\nPending', u'Limit Sell\nMay 6\n$90.00\n3 shares at $30.00', u'Dividend\nApr 16\n+$1.0', u'Limit Buy\nApr 16\n$100.00\n4 shares at $25.00', u'Limit Buy\nApr 16\nCanceled']
  stock = Stock('O', map(lambda x: Transaction(x), all_history))
  stock.parse()
  stock.equity = 35.0
  
  assert -7.0 == stock.total_cost
  assert 3.0 == stock.dividend_gain
  assert 1.0 == stock.shares
  assert stock.dividend_is_pending

  print(stock.performance())

  stock = Stock('O', map(lambda x: Transaction(x), all_history))

  stock.parse(True)
  assert -10.0 == stock.total_cost
  assert not stock.dividend_is_pending
