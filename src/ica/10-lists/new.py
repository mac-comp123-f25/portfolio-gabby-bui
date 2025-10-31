list1 = [5, 6, 7]
list2 = [4, 3, 2, 1]
list1.append(8)
list2.extend([0, -1])
list1.extend([5])
list1.insert(0, 4.5)
list2.insert(2, 3.5)
list1.remove(7)
list2.pop(1)
list1.index(8)
list1.count(5)
list1.reverse()
list2.sort()

print(list1)
print(list2)