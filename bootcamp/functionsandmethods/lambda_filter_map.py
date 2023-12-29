nums = [1,2,3,4,5,6,7,8,9]
# map function applies a function to all the elements in an iterable object (lists,etc.)
# dont include parentheses at the end of a function passed in as a parameter to map
def square(x):
    return x*x
for x in map(square,nums):
    print(x)
print(list((map(square,nums))))
#filter function: for true and false values only
def checkeven(num):
    return num % 2 == 0
mynums = [1,2,3,4,5,6]
list(filter(checkeven,mynums))
for n in filter(checkeven,mynums):
    print(n)
# lambda expression
lambda num: num ** 2
print(list(filter(lamba num:num%2 == 0,mynums)))
