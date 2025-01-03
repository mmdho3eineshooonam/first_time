import random

count = 0
guess = random.randint(0, 100)
num = int(input("input the number [and AI gonna guess that!] :  "))
guess_lst = []
while guess != num:
    print(f"I think your number is {guess}")
    guess_lst.append(guess)
    print("I think I messed up.... ")
    count += 1
    txt = str(input("what should I do? go higher or lower? (h/l) "))
    try:
        if txt == "h":
            old_guess = guess
            guess_new = random.choice(
                [dig for dig in range(guess, 100) if dig not in guess_lst]
            )
            guess_lst.append(guess_new)
            guess = guess_new

        elif txt == "l":
            guess_new = random.choice(
                [dig for dig in range(0, guess) if dig not in guess_lst]
            )
            guess_lst.append(guess_new)
            guess = guess_new
        else:
            print("you entered a wrong input. try again")
            txt = str(input("what should I do? go higher or lower? (h/l) "))
    except IndexError:
        print(f"I think you are bothering me :(  \n  I am done with you... ")
else:
    print(f"your number was {guess}!!")
