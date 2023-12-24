newlist = [1,"yo",2]
print(len(newlist))
print(newlist[0])
secondlist = [3,4,"crazy"]
combinelist = newlist + secondlist
print(combinelist)

# Lists are mutable
combinelist[0] = "one"
print(combinelist)
combinelist.append(5)
print(combinelist)
combinelist.pop()
print(combinelist)
combinelist.pop(2)
print(combinelist)

#.sort sorts a list
listone = [1,3,4,6,9,3,6,2,6,3,9,3,4]
listtwo = ["a",'g','s','b','u','w','g','j','e','c','t','w','c']
listone.sort()
listtwo.sort()
print(listone)
print(listtwo)

#reverse reverses a method
listone.reverse()
print(listone)
