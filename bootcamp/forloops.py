mylist = [1,2,3,4,5,6,7,8,9]
for x in mylist:
    print(x)
    if x % 2 == 0:
        print(" is even")
listsum = 0
for y in mylist:
    listsum += y
print(listsum)
for y in "hello world":
    print(y)
com = [(1,2,3,4,5,6),(1,2,3,4,5,6),(1,2,3,4,5,6),(1,2,3,4,5,6)]
for x in com:
    print("new")
    for y in x:
        print("yo")
for (x,y,a,d,v,b) in com:
    print(x)
    print(y)
    print(a)
    print(d)
    print(v)
    print(b)
d = {"a":1,"b":2,"c":3}
for x,y in d.items():
    print(y)
