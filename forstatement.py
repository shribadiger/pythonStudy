#Program to Illustrate about the FOR loop and while Loop

"""
while consition:
    statement to execute after conditions apply
"""
i = 1
while i <= 5:
    print('*' * i)
    i=i+1

print("Done")

#Check the for loop
words = ["Shriaknt", "shruti", "gowthami"]
for w in words:
    print(f"Name:  {w} - Length: {len(w)}")

print("For Loop Done")

# Loop over a slice copy of the entire list.
for w in words[:]:
    if len(w) > 7: # find the value length in more than 7 and insert in that list and continue from  that location
        words.insert(0,w)
print(words)

#arithemetic range() function in for loop

for i in range(5):
    print(i)
print("Done Range")

#range() method to iterate the for loop indices
for i in range(len(words)):
    print(i, words[i])

print("Range Loop Done")

#car program to illustrate the break and while loop

command = ""
is_car_started = False

while command != "quit":
    command = input("Enter your command : --> ")
    if command == "start":
        if is_car_started:
            print("Car is already started")
        else:
            is_car_started = True;
            print("Car is Started")
    elif command == "stop":
        if not is_car_started:
            print("Car already Stopped")
        else:
            is_car_started=False
            print("Car Stopped")
    elif command =="quit":
        print("Game Over..!!")
        break
    elif command=="help":
        print("""
               start- To start the car
               stop - To Stop the Car
               help - To get the help
               """)
    else:
        print("Invalid option")

# checking the pass functionality
while True:
    pass
    