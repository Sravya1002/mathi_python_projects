
# dictionary are a data type which is defined using key:value pair
# dictionary are created with {} and comma (,) separated.
# dictionary are mutable.

dict_item = {'Name':'Sravya','Batch':' Automation Testing'}
print(dict_item)

# pop() is used to remove item based on key provided
dict_item.pop('Batch')
print(dict_item)

# get() is used to fetch value of a particular key
dict_item.get('Name')
print(dict_item)

# clear() is used to clear/emptying a dictionary
dict_item.clear()
print(dict_item)

# for adding / updating new key:value in a dictionary
dict_item['Role'] = 'Sr.AT'
print(dict_item)

dict_item['Batch'] = 'GUVI'
print(dict_item)
