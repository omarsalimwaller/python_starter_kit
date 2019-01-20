# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 10:32:10 2019

@author: Visitor
"""

# Or Truth Table

# 0 | 0 | 0 (False)
# 0 | 1 | 1 (True)
# 1 | 0 | 1 (True)
# 1 | 1 | 1 (True)

# And Truth Table

# 0 | 0 | 0 (False)
# 0 | 1 | 1 (False)
# 1 | 0 | 1 (False)
# 1 | 1 | 1 (True)
print("Part 1: ")

omars_list = ["Omar", 11, 345.43, 3+2j, "Waller", ]

for item in omars_list:
    if type(item) == int:
        print("That was an integer \n")
    elif type(item) == str:
        print("That was a string \n")
    elif type(item) == float:
        print('That was a float \n')
    elif type(item) ==  complex:
        print('That is a complex number \n')
    else:
        print('Im not programmed to know what that is \n')
        

# If J. Cole is better than Kendrick and Chance print to the screen 
# Cole is the goat, if not print "Is he better than Soulja Boy, yes or no". If he is print
# I don't know bro, Soulja is a legend, if not print "FIYAA" and ask, "What is your 
# favorite Soulja dance, then respond, "I like that one too". 

print("Part 2: ")
first_response = input("Is Cole better than Kendrick and Chance (yes or no): ")

first_response = first_response.lower()

if first_response == 'yes':
    print("I dont know bro, Soulja is a legend")
elif first_response == 'no':
    print('FIYAAA')
    second_response = input('What is your favorite Soulja dance: ')
    second_response = second_response.lower()
    
    print('I like that one too')
else:
    print('Im not programmed to know what that is \n')

print('\n')

# Top rap album quiz. Guess how many rap albums were sold in the first week for a given artist.
# If they get the question wrong they lose 10 points, they start at 100. If their
# score is already zero they will stay at zero. Make this a game with 8-10 artists
# store album sale and artist in a dictionary. 
print("Part 3: ")

artists = {'J. Cole: KOD' : 395000, 'Meek Mill: Championships' : 229000, 'The Carters: Everything is Love': 124000,
           'Drake: Scorpion': 749000, 'Travis Scott: Astro World': 553000, 'Cardi B: Invasion of Privacy': 254000,
            'Various Artists: Black Panther Album': 156000, 'Migos: Culture 2': 200000, 'Eminem: Kamikaze': 434000,
            'Kanye West: Ye':210000}
# https://djbooth.net/features/2019-01-04-biggest-first-weeks-2018-hip-hop-albums

print("Welcome to the 2018 Hip-Hop Quiz Game")
print("Your curent score is 100. You lose 10 whenever you get an answer wrong. ")
print('Good luck!')

score = 100

for key,value in artists.items():
    user_response = input("How many albums do you think were sold the first week for " +key+': ')
    user_response = int(user_response)
    
    if user_response <= value +25000 and user_response >= value - 25000:
        print("Correct you are in the right range")
        print("Your score: "+str(score))
    else:
        print("Incorrect -10 points")
        score -= 10 #score = score -10
        print("Your score: "+str(score))
        
        if score < 0:
            score = 0

print('Bonus Question: Who had the greatest comeback in 2018: ')
print('A: Meek Mill')
print('B: Tyga')
print('C: Soulja Boy Tellem')
bonus = input()
bonus = bonus.lower()
if bonus == 'a':
    print('I agree')
    score +=20
    print("Your score: "+str(score))
elif bonus == 'b':
    print('Nahh')
    print("Your score: "+str(score))
elif bonus == 'c':
    print('Fiyaaahh')
    score +=10
    print("Your score: "+str(score))
    

















































#score = 100
#
#for key,value in artists.items():
#    user_guess = input('How many album sales did '+ key+ ' have: ')
#    user_guess = int(user_guess)
#    if user_guess >= value - 25000 and user_guess <= value +25000:
#        print("Correct, you're in the right range")
#        print('Your score: '+ str(score))
#    else:
#        print("Incorrect, -10")
#        score -= 10                     # same as score = score -10
#        print('Your score: '+ str(score))
#        
#print('Bonus question: Who had the biggest comeback of 2018? ')
#print('A: Soulja')
#print('B: Tyga')
#print('C: Meek Mill \n')
#bonus = input()
#        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
