for num in range(2,50,5):
    print(num)
print(list(range(1,10,2)))
index_count = 0
for x in "abcde":
    print(f"The index of {index_count} contains the string {x}")
    index_count += 1
word = "abcde"
for x,y in enumerate(word):
    print(x)
    print(y)
list1 = [1,2,3,4,5]
list2 = ["a",'b','c','d','e']
for x in zip(list1,list2):
    print(x)
list1 = [1,2,3,4,5]
print("x" in list1)
print("a" in "a world")
print(max(list1))
print(min(list1))
from random import randint
print(randint(0,100))
number = input("Enter a number here: ")
print(number)
print(type(number))
