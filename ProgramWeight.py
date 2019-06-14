#Program to convert the Weight in KG or in LBS

weight = int(input('WEIGHT : ')) # return value in string and converted to Integer
unit  = input('L(BS) or K(G)')

if unit.upper() == "L":
    converted = weight*0.45
    print(f"You are {converted} Kilos")
else:
    converted=weight / 0.45
    print(f"You are {converted} pounds")
