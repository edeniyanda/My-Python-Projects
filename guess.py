#Developer - Eden Iyanda
#This program prompt you to guess my name
#Hint - my nane is Eden
from itertools import count


print("Welcome!!")
guess_word = "EDEN"
guess_count = 1
guess_limit = 3
trial_off = False
trial = 3
count = 0
s = "s"
while True:
        wr = input("Enter my name")
        word = wr.upper()
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
                wr = input(f"You have {trial} trial{s} left, try again!!")
                fw = wr.upper()
            else:
                wr = input(f"You have {trial} trial{s} left, try again!!")
                fw = wr.upper()
        else:
            trial_off = True

if trial_off: 
    print("You LOSE!!")
else:
    print("You win")

