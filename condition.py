# Program to indicate the conditional statement in Python
prince = 10000;

is_good_credit = True

if is_good_credit:
    print("Customer is eligible for loan")
    down_payment = 0.1*prince
else:
    print("customer is not eligible for loan")
    down_payment = 0.2*prince
print(f"Downpayment : ${down_payment}")

#now checking for AND condition in if statement
is_valid_user = True
is_valid_password = True

if is_valid_user and is_valid_password:
    print("User can be authenticate to access Restricted Data")
elif is_valid_password or is_valid_user:
    print("Only one condition is satisfied for user authentication")
else:
    print("User is Blocked to Access the Restricted Data")

# Checking for NOT operation
has_criminal_record = False
if is_valid_password and  not has_criminal_record:
    print(" Eligible for Access Record")
else:
    print("User has the criminal record")

#Checking for Numeric  value comparision
temperature =35
if temperature == 30:
    print(" Today is Hot Day")
else:
    print(" Today is Cold Day")

name="shrikant"

if len(name) < 3:
    print("Please Enter minimum 8 charectors")
else:
    print("You are entered the correct charector length")

