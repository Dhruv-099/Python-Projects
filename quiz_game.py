print("Welcome to my computer quiz")
playing= input("Do you want to play? ")
if playing.lower() != "yes" :
    quit()
print ("lets play")
score=0

answer= input('What does CPU stand for?')
if answer.lower() == ('central processing unit'):
    print('Correct')
    score+=1
else: print('Incorrect')

answer= input('What does GPU stand for?').lower()
if answer == ('graphics processing unit'):
    print('Correct')
    score+=1
else: print('Incorrect')

answer= input('What does RAM stand for?').lower()
if answer == ('random access memory'):
    print('Correct')
    score+=1
else: print('Incorrect')

answer= input('What does PSU stand for?').lower()
if answer == ('power supply'):
    print('Correct')
    score+=1
else: print('Incorrect')

print('You got' + str(score) + ' questions correct')