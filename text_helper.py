import functools

def process(arr):
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
  print(action_values)
  result = functools.reduce(lambda acc, pairs: (acc + pairs[0] * pairs[1]), action_values, 0)

  return "{:.2f}".format(result)

def convert_action(action):
  if action in ['Market Sell', 'Limit Sell', 'Dividend', 'Stop Loss Sell']:
    return 1
  
  return -1

def parse_dollar(number):
  start_idx = 0
  if number.startswith('+'):
    start_idx = 2
  else:
    start_idx = 1
  
  return float(number[start_idx:].replace(',', ''))
  try:
    return float(number[start_idx:].replace(',', ''))
  except ValueError:
    return 0


if __name__ == '__main__':
  # toss some unit test overhere
  assert 1000.12 == parse_dollar('$1,000.12')
  assert '2000.12' == process(['Market Sell', '$1,000.12', 'Dividend', '$2,000.99', 'Market Buy', '$1,000.99'])
