# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:07:23 2022

@author: mbsmi
"""

# Create an ecrytped function using a loop from a dictionary
# Mar 2, 2022
# CSC-121 -Encryption
# Mary Beth Maraldi

# import needed modules
import string
import random

# Create 2 lists one to use as keys, 2 as a pool to use as random values for the keys
s1 = list(string.ascii_letters + string.punctuation)
s2 = list(string.ascii_letters + string.punctuation)

# Create dictionary
code = {}

# Def to make code dictionary
def create_code(s1,s2):
    for i in range(len(s1)):        # evaluate accross chr set
        value = random.choice(s2)   # randomly choose value
        pair = {s1[i]:value}        # new pair         
        index = s2.index(value)
        s2.pop(index)               # index needed to remove value from the value pool 
                                    # (This is needed if it is to be decrypted)
        code.update(pair)           # update dictionary with new pair
    return code


def encrypt(code,sentence):
   new = ''
  
   for let in sentence:
        if let != ' ':         
            new += code[let]
        else:
            new += ' '
   return new

sentence = input('Enter sentntence you want to encrypt below:')

print('Sentence encryption below:')
print(encrypt(create_code(s1,s2),sentence))



    