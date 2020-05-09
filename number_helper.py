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
