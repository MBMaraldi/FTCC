###CTI-110
###P5HW1 - Lists and Sets
## Mary Beth Maraldi
## 11/7/2021

########################### Part 1 ##########################
##Create function to call
##Create list, input numbers with loop(). Print list

created_list = []
N=10        ##(I did this so if we wanted to make it an imput, we wouldn't have to change the function later)

def list_creater(): #function to create a new list
    for i in range(N):
        i += 1
        num = float(input('Enter num {}:'.format(i)))
        created_list.append(num)
    print()
    print('Created List:\n', created_list)    
    return created_list
           
def evaluate_list():  #function to evaluate & display min/max/sum/avg
    print('Smallest number in list: \t', min(created_list))
    print('Largest number in list: \t', max(created_list))
    print('Sum of numbers in list: \t', sum(created_list))
    print('Average of numbers in list: \t', sum(created_list)/len(created_list))
    print()
    return

def list_to_set():  # function to convert list to set and display
    created_set = set(created_list)
    print('Created Set:\n', created_set)

##Call functions names to create and display part 1
#list_creater()
#evaluate_list()
#list_to_set()

######## I DID NOT KNOW IF YOU STILL WANTED US TO DISPLAY THE INFORMATION IN PART 1
######## OR IF IT WAS JUST TO SET UP THE MAIN FUNCTIONS NEEDED FOR PART 2

######################### Part 2 ##########################
created_list = []
menu = 'yes'
print()
while menu != 'no': #continues until 3 is entered
    print("--------Menu-------- \n1)Create List \n2)Display Results \n3)Exit \n--------------------")
    instruction_function = int(input('Please make your selection.'))
    print()

    if instruction_function == 1:   #create a list
        list_creater()
        
    elif instruction_function ==2:  #display
        if len(created_list) == 0:  #no list, back to menu
            print("No list has been created yet")
        else:                       #display results
            evaluate_list()
            list_to_set()
            
    elif instruction_function == 3: #exit program
        menu = 'no'
        print('Have a great day.')
    
    else:                           #(This is only if invalid option, return to menu.)
        print("That is not a valid option.")
    
    print('\n')









