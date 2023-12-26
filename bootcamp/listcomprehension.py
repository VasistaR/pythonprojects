mystring = "vasista"
list1 = []
for x in mystring:
    list1.append(x)
print(list1)
# or do this
list2 = [x for x in mystring]
print(list2)
list3 = [x**2 for x in range(0,11)]
print(list3)
list4 = [x for x in range(0,11) if x % 2 == 0]
print(list4)
list5 = [1,23,24,4,34,43,5]
list6 = [(9/5)*x + 32 for x in list5]
print(list6)
list7 = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(list7)
