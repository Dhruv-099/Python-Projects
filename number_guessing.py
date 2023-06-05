import random
top_of_range=input('Type a number: ')
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range<=0:
        print('Please type a number greater than 0 next time. ')
        quit()
else:
    print('type in a number')
    quit()
    
random_num= random.randrange(0,top_of_range)
guess=0
while True:
    guess+=1 
    user_guess=input('Make a guess: ')
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print('Please type a no this time')
        continue
    if user_guess==random_num:
        print('You got it right')
        break
    elif   user_guess>random_num:
            print('you were above the number')
    else:
            print('You were below the number')
print('You got it in',guess,"guesses")       