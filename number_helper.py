from datetime import datetime, date

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

def parse_date(date_str):
  if len(date_str.split(',')) == 1:
    date_str = date_str + ', ' + str(date.today().year)
  datetime_object = datetime.strptime(date_str, '%b %d, %Y')

  return date(datetime_object.year, datetime_object.month, datetime_object.day)

if __name__ == '__main__':
  # toss some unit test overhere
  num = '$1.2'
  assert 1.20 == parse_dollar(num)

  num = '+$1.2'
  assert 1.20 == parse_dollar(num)

  date_str = 'Mar 30'
  assert date(date.today().year, 3, 30) == parse_date(date_str)

  date_str = 'Dec 25, 2019'
  assert date(2019, 12, 25) == parse_date(date_str)