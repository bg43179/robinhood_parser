from number_helper import parse_dollar

class Stock:
  def __init__(self, symbol, history = []):
    self.symbol = symbol
    self.history = history
    self.dict_history = []
    self.dividend_is_pending = False
    self.shares = 0
    self.total_cost = 0
    self.equity = 0
    self.dividend_gain = 0

  def performance(self):
    return "{} - cost: {:.2f}, equity: {:.2f}, profit: {:.2f}".format(self.symbol, abs(self.total_cost), self.equity, self.gain_loss())

  def dividend(self):
    return "{} - profit: {:.2f}".format(self.symbol, self.dividend_gain)
    
  def parse(self, exclude_dividend = False):
    for transaction in self.history:
      transaction_dict = {}
      attrs = transaction.split('\n')
      transaction_dict['action'] = attrs[0]
      transaction_dict['action_multiplier'] = self.convert_action(attrs[0])
      transaction_dict['date'] = attrs[1]
      transaction_dict['amount'] = parse_dollar(attrs[2])
      if len(attrs) == 4:
        if attrs[0] != 'Dividend':
          transaction_dict['shares'] = float(attrs[3].split(' ')[0])
          self.shares -= transaction_dict['action_multiplier'] * transaction_dict['shares']
        else:
          transaction_dict['is_pending'] = True

      self.dict_history.append(transaction_dict)

    for t in self.dict_history:
      if exclude_dividend and t['action'] == 'Dividend':
        continue

      self.total_cost += t['action_multiplier'] * t['amount']

      if t['action'] == 'Dividend':
        self.dividend_gain += t['amount']

  def gain_loss(self):
    return self.equity + self.total_cost

  def convert_action(self, action):
    if action in ['Market Sell', 'Limit Sell', 'Dividend', 'Stop Loss Sell']:
      return 1

    return -1

if __name__ == '__main__':
  # toss some unit test overhere
  all_history = [u'Dividend\nMay 15, 2020\n+$2.00\nPending', u'Limit Sell\nMay 6\n$90.00\n2 shares at $45.00', u'Dividend\nApr 16\n+$1.0', u'Limit Buy\nApr 16\n$105.00\n2 shares at $52.50', u'Limit Buy\nApr 16\nCanceled']
  stock = Stock('O', all_history)
  stock.parse()
  
  assert -12.0 == stock.total_cost
  assert 3.0 == stock.dividend_gain
  assert 0.0 == stock.shares

  stock = Stock('O', all_history)
  stock.parse(True)

  assert -15.0 == stock.total_cost
