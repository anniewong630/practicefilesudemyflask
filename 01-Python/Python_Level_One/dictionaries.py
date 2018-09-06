salary = {'Bob': 30, 'Rob': 40}
print(salary)
print('Getting the value using key: ' + str(salary['Bob']))

print('\nAdding Cindy to the dictionary: ')
salary['Cindy'] = 50
print(salary['Cindy'])

print('\nAdjusting key value pairs:')
print('Before the raise: ' + str(salary['Rob']))

salary['Rob'] = salary['Rob'] + 10
print('After the raise: ' + str(salary['Rob']))

print('\nAdding a list as value: ')
d = {'John' : [1,2,3] , 'Kelly' : [4,5,6]}
print(d['John'])

print('\nNested dictionary: ')
people={'John': {'salary': 10, 'age': 50}}
print(people['John']['age'])

s = {'Bob': 30, 'Rob': 40}
print(s.keys())
print(s.values())
print(s.items())




