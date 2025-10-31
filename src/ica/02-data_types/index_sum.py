n1=input("Please add one number of your choice")
n2=input("Please add one number of your choice")
n3=input("Please add one number of your choice")
n4=input("Please add one number of your choice")
n5=input("Please add one number of your choice")
n6=input("Please add one number of your choice")
n1=int(n1)
n2=int(n2)
n3=int(n3)
n4=int(n4)
n5=int(n5)
n6=int(n6)
lst = [n1, n2, n3, n4, n5, n6]
even_index_sum = lst[0]+lst[2]+lst[4]
odd_index_sum = lst[1]+lst[3]+lst[5]
print(even_index_sum)
print(odd_index_sum)
