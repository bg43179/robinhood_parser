import json

def custom_mapper(file_name):
  print('Fetch mapper from ' + str(file_name))
  
  f = open(file_name)
  data = json.load(f) 
  f.close()

  return list(data.items())