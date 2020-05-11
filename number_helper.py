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
  num = '$1.2'
  assert 1.20 == parse_dollar(num)

  num = '+$1.2'
  assert 1.20 == parse_dollar(num)

