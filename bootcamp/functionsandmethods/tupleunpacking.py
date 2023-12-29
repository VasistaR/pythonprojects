# example of tuple unpacking
stockprice = [("APPL",200),("MSFT",234)]
for x in stockprice:
    print(x)
# returns name with most hours
workhours = [("a",100),("b",500),("c",300)]
def check(hourslist):
    min_y = hourslist[0][1]
    min_x = hourslist[0][0]
    count = 0
    for x,y in hourslist:
        if y > min_y:
            min_y = y
            min_x = hourslist[count][0]
        count += 1
    return min_x
print(check(workhours))
