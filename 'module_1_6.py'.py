my_dict={'Mikhail':1993, 'Vladislav':2004,'July':2020}
print(my_dict)
print(my_dict['Mikhail'])
my_dict['Asya']=2006
print(my_dict)
my_dict.update({'Larisa':1969,
                'Oleg':1956})
print(my_dict)
#my_dict.pop('Asya')
#print(my_dict)
a=my_dict.pop('Asya')
print(a)
print(my_dict)
my_set ={7, 'Dragon', 3.14, 'Dragon', 3.14, 7}
print(my_set)
print(my_set.add('Snake'))
print(my_set)
print(my_set.add(5))
print(my_set)
print(my_set.discard(3.14))
print(my_set)