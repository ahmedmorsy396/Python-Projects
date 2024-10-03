# This code take characters from user and concatenate it
# By Ahmed Abdelhamed
# 3/10/024
from math import inf

word = ''
for i in range(100000):
    Char = str(input('Please enter char of the word:'))  # take characters from user
    word = word + Char
    End_com = int(input('Enter 0 to finish the word: '))  # take end commend from user
    if End_com == 0:
        break
print('The word is:', word) # print the word on screen
