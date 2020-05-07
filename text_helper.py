import functools

def process(arr, exclude_dividend):
  def convert_action(action):
    if action in ['Market Sell', 'Limit Sell', 'Stop Loss Sell']:
      return 1

    if action == 'Dividend':
      if exclude_dividend:
        return 0
      else:
        return 1

    return -1

  actions = []
  values = []
  for idx, val in enumerate(arr):
    if idx % 2 == 0:
      actions.append(val)
    else:
      values.append(val)

    if val == 'Canceled':
      actions.pop()
      values.pop()

  action_values = list(zip(map(convert_action, actions), map(parse_dollar, values)))
  result = functools.reduce(lambda acc, pairs: (acc + pairs[0] * pairs[1]), action_values, 0)

  return action_values, result

def parse_dollar(number):
  start_idx = 0
  if number.startswith('+'):
    start_idx = 2
  else:
    start_idx = 1
  
  try:
    return float(number[start_idx:].replace(',', ''))
  except ValueError:
    return 0


if __name__ == '__main__':
  # toss some unit test overhere
  assert 1000.12 == parse_dollar('$1,000.12')
  assert ([(1, 3.0), (-1, 1000.99)], -997.99) == process(['Dividend', '+$3.00', 'Market Buy', '$1,000.99'], False)