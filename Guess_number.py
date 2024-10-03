# this app create magus name for series of numbers take range from user
# By Ahmed Abdelhamed
# 2/10/2024

import random  # Import random lib

Lower = int(input('please enter lower value:'))  # Take smallest numer from user
Higher = int(input('please enter higher value:'))  # Take high numer from user
All_values = range(Lower, Higher, 1)  # make series of number with step 1
value = random.choice(All_values)  # chose random value

print('You have six times to try')  # detect number of try for user

for i in range(1, 7):
    print('number', i, end='')
    Guss = int(input(' please guess the number :'))
    if Guss == value:
        print('you are true')
        break
    elif abs(Guss - value) > 5:
        print('you are far from true value')
    else:
        print('you are near from value')
