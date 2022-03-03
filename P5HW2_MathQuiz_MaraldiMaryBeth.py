# Randomized MathQuiz
# 11/7/2021
# CTI-110 P5HW2_MathQuiz
# Mary Beth Maraldi
#
########


import random
######Part 1





def generate_numbers():
    global num_1 
    global num_2 
    num_1 = random.randint(-200,200)
    num_2 = random.randint(-200,200)
    return num_1, num_2


generate_numbers()
print(num_1, num_2)
def create_add_question():
    print(num_1,'+',num_2,'=')
    global answer 
    answer = (num_1+num_2)
    global response
    response = input()
    return 

create_add_question()
if response == (answer):
    print('con')
else:
    print('wrong', answer)

 
