my_dict = {'War': 1914, 'Seva': 1941, 'Marta': 1999, 'Gregor': 2010}
print(my_dict)
my_dict['Gnom'] = 1501
my_dict.update({'Sasha': 2024, 'Tank': 1915})
print(my_dict)
print('Existing value:', my_dict['Seva'])
print('Not existing value:', my_dict.get('Denis'))
print('Deleted value:', my_dict.pop('War'))
print('Modified dictionary:', my_dict)

my_set = {1,1,2,3,2,1,(123,456,789), 'zombie'}
print('Set:', my_set)
my_set.add('wow')
my_set.add(5)
my_set.remove('zombie')
print('Modified set:', my_set)

