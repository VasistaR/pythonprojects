#args treated as a tuple, allows to take as many arguments as desired
def sumofnumbers(*args):
    return sum(args)
print(sumofnumbers(1,2,4,5,7,8,3,2,5,6,7,4,6,2,4,76,3,4))
#kwargs creates a dictionary of keywords
def myfunc(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")
myfunc(fruit = "apple",veggie = "lettuce")
