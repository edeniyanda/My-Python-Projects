#Developer - Eden Iyanda
#This program prompt you to guess my name
#keep it in mind that you have 3 trials
print("Welcome!!")
guess_word = "Eden"
guess_count = 1
guess_limit = 3
trial_off = False
trial = 3
s = "s"
while True:
    word = input("Enter my name")
    try:
        float(word)
        print("Invalid input, Please enter a Alphabetical data")
        continue
    except:
        fw = str(word)
        break

while fw != guess_word and not(trial_off):
    if guess_count < guess_limit:
        guess_count += 1
        trial -= 1
        if trial == 1:
            s =""
            fw = input(f"You have {trial} trial{s} left, try again!!")
        else:
            fw = input(f"You have {trial} trial{s} left, try again!!")
    else:
        trial_off = True

if trial_off: 
    print("You LOSE!!")
else:
    print("You win")
    




