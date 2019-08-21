number = 23
running = True
while running:
    guess = int(input('Some number'))
    if guess == number:
        print('Great job')
        running = False #stop loop
    elif guess < number:
        print('bigger')
    else:
        print('smaller')
else:
    print('ending')
