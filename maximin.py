# Developer - Eden Iyanda
# This program prompt you to enter as many number as you can 
# and will print out the maximum and minimum number you've entered so far when "done" is inputed
print("Welcome!!")
largest = None
smallest = None
emotion_1 = ""
emotion_2 = ""
another = ""
a = "a "
while True:
    val = input(f"{emotion_1}Enter {a}{emotion_2}{another}number:")
    if val == "done":
        break
    try:
        fv = float(val)
        if largest is None:
            largest = fv
            another = "another "
            a = ""
        elif largest <  fv :
            largest = fv
            another = "another "
            a = ""
        elif smallest is None:
            smallest = fv
            another = "another "
            a = ""
        elif smallest > fv:
            smallest = fv
            another = "another "
            a = ""
    except:
        print("Invalid input") 
        emotion_1 = "Please "
        emotion_2 = "valid "
        another = ""
        a = "a "
        continue  
print("So far your maximun input is", int(largest), "and your minimum input is", int(smallest))
print("Have a nice day!")