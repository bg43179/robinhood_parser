class Summary:
  def __init__(self, name):
    self.name = name
    self.history = []
    self.total_cost = 0
    self.equity = 0

  def __str__(self):
    return "{} - cost: {:.2f}, equity: {:.2f}, profit: {:.2f}".format(self.name, self.total_cost, self.equity, self.equity + self.total_cost)

if __name__ == '__main__':
  # toss some unit test overhere
  summary = Summary('NFLX')
  summary.history = [(1, 100), (2, 200)]
  summary.total_cost = 100
  print(summary)
