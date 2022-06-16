#base

import random
count=0
number=random.randint(1,100)
Tebak=input('Enter your number : ')
while Tebak.isnumeric() :
    count=count+1
    if int(Tebak)<number:
        print('Your number is too small, guess again! Guesses =',count)
        Tebak=input('Enter your number : ')
    elif int(Tebak)>number:
        print('Your number is too big, guess again! Guesses   =',count)
        Tebak=input('Enter your number : ')
    else:
        print('Good job! You guessed the number in',count,'attemps!')
        break
else :
   print('Please input number not text/alphanumeric')

#advance

import random #make the comp generate a random number

print('Mini game')
print('Made by choco_milk and Kenneth 8G for contribution')
print()
print('Please select level')
print('Level 1 - Easy')
print('Level 2 - Moderate')
print('Level 3 - Hard')
a=int(input('Type the level number - '))
if a == 4 :
    print()
    print('Extreme, 1 to 1000000')
    number=random.randint(1,1000000) #select number randomly within the range inside it
elif a == 3 :
    print()
    print('Level 3, 1 to 10000')
    number=random.randint(1,10000)
elif a == 2 :
    print()
    print('Level 2, 1 to 1000')
    number=random.randint(1,1000)
elif a == 1 :
    print()
    print('Level 1, 1 to 100')
    number=random.randint(1,100)
elif a == 0 :
    print()
    print('Too easy, 1 to 10')
    number=random.randint(1,10)
else :
    print()
    print('No less than 0 and more than 4 also if you input number on the guess it will crash... so yeah')
    
count=0 #variable counter
b=input('Your guess: ')
while b.isnumeric() : #to indicate that the number you input is a number
    #.isdigit() and .isnumeric are the same
    count+=1 #simplified count = count+1
    if int(b) < number :
        print('Your number is too small, guess again! Guesses =',count)
        print()
        b=input('Enter your number: ')
    elif int(b) > number :
        print('Your number is too big, guess again! Guesses   =',count)
        print()
        b=input('Enter your number: ')
    else:
        print('Good job! You guessed the number in',count,'attemps!')
        break #to close
else :
    print('No alphanumeric or alphabet')

----------------------------------------------------------------------------------
#more advance

import random #make the comp generate a random number

print('Mini game')
print('Made by choco_milk and Kenneth 8G for contribution')
print()
print('Please select level')
print('Level 1 - Easy')
print('Level 2 - Moderate')
print('Level 3 - Hard')
a=int(input('Type the level number - '))
if a == 4 :
    print()
    print('Extreme, 1 to 1000000')
    number=random.randint(1,1000000) #select number randomly within the range inside it
elif a == 3 :
    print()
    print('Level 3, 1 to 10000')
    number=random.randint(1,10000)
elif a == 2 :
    print()
    print('Level 2, 1 to 1000')
    number=random.randint(1,1000)
elif a == 1 :
    print()
    print('Level 1, 1 to 100')
    number=random.randint(1,100)
elif a == 0 :
    print()
    print('Too easy, 1 to 10')
    number=random.randint(1,10)
else :
    print('No alphabet/alphanumeric/more than 0 and 4')
    
count=0 #variable counter
max=10 #variable counter for limiter
b=input('Guess the number: ')
while b != number :
    count+=1
    max-=1
    if max > 0 and max <= 10 :
        if int(b) < number :
            print('Your number is too small! Guess again. Guesse: ',count)
            print('Attempt limits: ',max)
            print()
            b=input('Guess the number: ')
        elif int(b) > number :
            print('Your number is too big! Guess again. Guesses : ',count)
            print('Attempt limits: ',max)
            print()
            b=input('Guess the number: ')
        else :
            print('You guessed the number in',count,'attempts!')
            break #to close
    elif b.isalpha() and b.isalphanumeric() :
        print('No alphabet or alphanumeric')
        break #stop it from repeating randomly
    else :
        print('Yo\ve reached the limit!')
        break #close due to limit
    #note, can't use 'break' outside while/for
else :
    print('No alphabet or alphanumeric')
