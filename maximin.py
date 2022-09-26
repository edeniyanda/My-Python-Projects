# Developer - Eden Iyanda
# This program prompt you to enter as many number as you can 
# and will print out the maximum and minimum number you've entered so far when "done" is inputed
from itertools import count


print("Welcome!!")
largest = None
smallest = None
counts = 0
emotion_1 = ""
emotion_2 = ""
another = ""
a = "a "
try_again = True
while try_again:
    while True:
        val = input(f"{emotion_1}Enter {a}{emotion_2}{another}number:")
        if val == "done":
            break
        try:
            fv = float(val)
            if largest is None:
                counts += 1
                largest = fv
                emotion_1 = ""
                emotion_2 = ""
                another = "another "
                a = ""
            elif largest <  fv :
                counts += 1
                largest = fv
                emotion_1 = ""
                emotion_2 = ""
                another = "another "
                a = ""
            elif smallest is None:
                counts += 1
                smallest = fv
                emotion_1 = ""
                emotion_2 = ""
                another = "another "
                a = ""
            elif smallest > fv:
                counts += 1
                smallest = fv
                emotion_1 = ""
                emotion_2 = ""
                another = "another "
                a = ""
        except:
            print("Invalid input") 
            emotion_1 = "Please "
            emotion_2 = "valid "
            another = ""
            a = "a "
            continue  
    print("You've entered", counts, "inputs so far and your maximun input is", largest, "and your minimum input is", smallest)
    t_a = input("Do you want to run the progam again? (Enter (y) for Yes and (n) for no)")
    if t_a == "y":
        try_again = True
        another = ""
        a = "a "
        largest = None
        smallest = None
    elif t_a == "n":
        try_again = False
        print("Have a nice day!")
    else:
        print("Invalid Input")