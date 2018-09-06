mylist = [1,2,3,5,7,'hello']

print('Length of a list')
print(len(mylist))

print('\nSlicing through a list')
print(mylist[1:3])

print('\nAppending item to a list- always at the end of a list')
mylist.append(3)
print(mylist)

print('\nInsert- inserting using index')
mylist.insert(3,'apple')
print(mylist)

print('\nRemoving an item from list- pop')
print(mylist)
popped_item = mylist.pop(5)
print(mylist)
print('\nItem popped = ' + str(popped_item))

print('\nNested lists/Stacked lists')
mylist1=[0,1,2]
mylist2=[3,4,5]
mylist3=[6,7,8]

megalist=[mylist1,mylist2,mylist3]

print(megalist)
print('\n' + str(megalist[2][2]))

