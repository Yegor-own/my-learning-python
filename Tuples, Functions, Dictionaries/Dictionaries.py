# first declaration method
d = dict(Ivan='manager',
         Mark='worker')
print(d)
print(type(d))

# second declaration method
d1 = {'A1': '123',
      'A2': '456'}
print(d1)
print(type(d1))

cuntries = {'Russia': 'Moscow', 'USA': 'Washington'}
# add new key and value
cuntries['China'] = 'Beijing'
# delete element with key USA
del cuntries['USA']
print(cuntries)
# prints size of dict
print(cuntries.__sizeof__())
# check is there in dict key Russia
print('Russia' in cuntries)
# get value by key Russia
print(cuntries.get('Russia'))
# get all items in dict
print(cuntries.items())
# get all keys
print(cuntries.keys())
# delete and return element
print(cuntries.pop('Russia'))
# add new default key and default value
cuntries.setdefault('USA', 'Washington')
# update values
cuntries.update({'China': 'Tokyo'})
print(cuntries)
