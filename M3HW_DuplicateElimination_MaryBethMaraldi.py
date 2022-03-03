# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:37:17 2022

@author: mbsmi
"""

# Duplicate Elimination
# Feb 13, 2022
# CSC-121 M3HW - Duplicate Elimination
# Mary Beth Maraldi

import numpy as np

# request how many items are needed in list
# recieve list
# return sorted, unique list

num=[]
word=[]

def num_list():    
    print('Let us start with the number list\n')
    p = int(input('How many numbers do you want to add to list?'))    #number of items in list
   
    for i in range(0, p):            
        n = float(input(f'Enter element number {i+1}:')) 
        num.append(n)     #adds values to list  
    return num


def word_list():
    print('Now we move on to list of words/strings \n')
    x = int(input('How many elements do you want to add to list?'))         # number of items in list
   
    for i in range(0, x):            
        w = str(input(f'Enter element number {i+1}:')) 
        word.append(w)     #adds values to list  
    return word


def display():
    num_list()      #Calls function to run
    word_list()     #Calls function to run
    
    print('Original Number List:', num, '\n')       #display original
    print('List without duplicates:', sorted(np.unique(num)), '\n')         #display sorted
    print('Original Word List:', word, '\n')        #display original
    print('List without duplicates:', sorted(np.unique(word)), '\n')        #display sorted




display()       

