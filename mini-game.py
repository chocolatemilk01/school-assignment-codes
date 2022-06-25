#simple

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
----------------------------------------------------------------------------------
#advance

import random #make the comp generate a random number

print('Mini game')
print('Made by choco_milk and Nasikuning46 for contribution')
print()
print('Please select level')
print('Level 1 - Easy')
print('Level 2 - Moderate')
print('Level 3 - Hard')
a=int(input('Type the level number - '))
if a == 4 :
    print()
    print('Extreme, 1 to 1.000.000')
    number=random.randint(1,1_000_000) #select number randomly within the range inside it
elif a == 3 :
    print()
    print('Level 3, 1 to 10.000')
    number=random.randint(1,10_000)
elif a == 2 :
    print()
    print('Level 2, 1 to 1.000')
    number=random.randint(1,1_000)
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
    print('No less than 0 and more than 4')
    quit()
    
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
print('Made by Ray 8F and Kenneth 8G for contribution')
print()
print('Please select level')
print('Level 1 - Easy')
print('Level 2 - Moderate')
print('Level 3 - Hard')
a=int(input('Type the level number - '))
if a == 4 :
    print()
    print('Extreme, 1 to 1.000.000')
    number=random.randint(1,1_000_000) #select number randomly within the range inside it
    max=25 #variable counter for limiter
elif a == 3 :
    print()
    print('Level 3, 1 to 10.000')
    number=random.randint(1,10_000)
    max=20
elif a == 2 :
    print()
    print('Level 2, 1 to 1.000')
    number=random.randint(1,1_000)
    max=15
elif a == 1 :
    print()
    print('Level 1, 1 to 100')
    number=random.randint(1,100)
    max=10
elif a == 0 :
    print()
    print('Too easy, 1 to 10')
    number=random.randint(1,10)
    max=10
else :
    print('No more than 4 and less than 0')
    quit()
	
count=0 #variable counter
b=input('Guess the number: ')
while b.isnumeric() and b != number :
    count+=1
    max-=1
    if max > 0 and max <= 11 or max <= 16 or max <= 21 or max <= 26 :
        if int(b) < number :
            print('Your number is too small! Guess again. Guesses: ',count)
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
            print('Attempt limits: ',max)
            break #to close
    else :
        print('You\'ve reached the limit!')
        break #close due to limit
        #note, can't use 'break' outside while/for
else :
    print('No alphabet or alphanumeric')
