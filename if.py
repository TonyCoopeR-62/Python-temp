number = 23
guess = int(input('Number :'))

if guess == number:
    print('congratulations')
elif guess < number:
    print('little')
else: 
    print('bigger')

print('end')
