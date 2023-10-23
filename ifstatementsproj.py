print("Kilograms to pounds and pounds to kilograms converter")
weight = input("What is your weight (number only)? ")
kgorl = input("Kilograms (kg) or pounds (lb)? Write only k or l. ")
if kgorl == "k":
    poundweight = float(weight) * 2.2
    print("Your weight in pounds is", poundweight)
if kgorl == "l":
    kgweight = float(weight) / 2.2
    print("Your weight in kilograms is", kgweight)