def return_missing_balanced_numbers(input):
  # Write your code here
  dicts = {}
  for x in input:
    if x in dicts:
      dicts[x] += 1
    else:
      dicts[x] = 1
  z = max(dicts.values())
  new_dict = {key:z-val for key, val in dicts.items() if val != z}
  #for k,v in dicts.items():
   # if dicts[k] == z:
    #  dicts.pop(k)
    #else:
     # dicts[k] = z-v
      
  return new_dict