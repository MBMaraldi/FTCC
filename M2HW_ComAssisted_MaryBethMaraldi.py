# Using Computer to Educate Students on Simple Multiplication
# Feb 7, 2022
# CSC121 M2HW - Computer Assisted
# Mary Beth Maraldi


# continue if answer is correct
# generate 2 ransom positive 1 or 2 digit numbers (depending on dif lvl)
# establish difficulty lvl
# print question
# if wrong state and ask for new question
# generate response randomly
# establish if they wish to continue to new question

import random
            
            
def gen_qu():   
    dif_lvl = int(input('Difficulty Level? 1=Easy, 2=Hard')) #define difficulty lvl
    # if statement to establish random value
    
    x=0
    if dif_lvl ==1:
        n1=random.randrange(1,9)
        n2=random.randrange(1,9)
    elif dif_lvl == 2:
        n1=random.randrange(1,99)
        n2=random.randrange(1,99)
     

    while x == 0: # This allows question to be repeated if wrong
        answer = int(input(f'How much is {n1} times {n2}?'))
        y = (n1 * n2)
        p=random.randrange(1,3) # used to generate different responses
        
        
        if answer == y:
            if p == 1:
                print("Very Good!")
            elif p == 2:
                print('Nice work!')
            elif p== 3:
                print("Keep up the good work!")
            x=1
        else:
            if p==1:    
                print('No. Please try again.')
            elif p==2:
                print("Wrong. Try once more.")
            elif p ==3:
                print('No. Keep trying.')


cont = 'yes'
while cont != 'no': # allows program to ask another question
    gen_qu()  #Call to function
    
    cont =input('Do you wish to continue? Enter yes or no.')
    
print('Good bye.') # end program response
 
