# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:19:59 2022

@author: mbsmi
"""

# Randomly quiz Country Capitals from Dictionary
# Mar 2, 2022
# CSC-121 M4HW - Country Capitals
# Mary Beth Maraldi

# import needed modules
import random

# Create dictionary Country:Capital
dict = {'China':'Beijing', 'Japan':'Tokyo', 'Russia':'Moscow', 'Indonesia':'Jakarta', 'South Korea':'Seoul', 'Egypt':'Cairo', 'United Kingdom':'London', 'Mexico':'Mexico City', 'Banladash':'Dhaka', 'Peru':'Lima', 'Iran':'Tehran', 'Thailand':'Bangkok', 'Saudi Arabia':'Riyadh', 'Hong Kong':'Hong Kong', 'Colombia':'Bogota', 'Chile':'Santiago', 'Singapore':'Singapore', 'Vietnam':'Hanoi', 'Iraq':'Baghdad', 'Turkey':'Ankara'}


cont = ''               # sentinel
correct = 0             # correct count
wrong = 0               # incorrect count

while cont != 'no':     # This is for the sentinel (this could also be done in the elif if they make we used answer == 'end' instead of asking Continue)
    
    country = random.choice(list(dict))                                 # Choose Capital at random    
    answer = input('What is the capital of {}?'.format(country))        # Get answer input
    
    if answer == dict[country]:            
        print('That is correct, great job.')
        correct += 1                                                    # add count to correct
    else:
        print('That is not correct.')    
        wrong += 1                                                      # add count to incorrect
        
    cont = input("Do you wanna try another? 'yes' or 'no'")             # sentinel question
    

print('\nYou got {} correct and {} incorrect.'.format(correct, wrong))  # return stats