list1=[20,4,'python','java']

print(list1)

list2 = [20,4,'python','java']
list1.extend(list2)

print(list1)
list1.append(list2)
print(list1)

list3 = list1 + list2