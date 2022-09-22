#Developer - Eden Iyanda
#This program prompt you to guess my name
print("Welcome!!")
guess_word = "Eden"
guess_count = 1
guess_limit = 3
trial_off = False
word = input("Enter my name")
while word != guess_word and not(trial_off):
    if guess_count < guess_limit:
        word = input("Try again, you are almost there!")
        guess_count += 1
    else:
        trial_off = True

if trial_off: 
    print("You LOSE!!")
else:
    print("You win")
    




