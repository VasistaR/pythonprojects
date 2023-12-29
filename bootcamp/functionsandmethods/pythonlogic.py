## Make sure to capitalize booleans
def evenornot(num):
    if num % 2 == 0:
        return True;
    else:
        return False;
print(evenornot(3455))

## for lists
def evenornot_lists(numlist):
    for x in numlist:
        if x % 2 == 0:
            return True;
    return False;
print(evenornot_lists([1,3,5,7]))

## returns all the even numbers in a lists
def evenornot_lists_all(numlist):
    evenlist = []
    for x in numlist:
        if x % 2 == 0:
            evenlist.append(x)
    return evenlist
print(evenornot_lists_all([1,3,5,7,9]))
