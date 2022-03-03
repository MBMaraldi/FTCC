#CTI-110
#P4HW1-Expenses
#Mary Beth Maraldi
#10/24/2021

#Prompt user to enter initial amount
start_amount = float(input('Enter starting amount in account $'))
total = start_amount
cont = 'y'
num_expense = 0



while cont == 'y':                              #create loop forward if n, loop if y\n ---while cont =='y'
    num_expense += 1                            #calculate number of expenses
    print('Enter expense', num_expense, ':')    #Prompt user to enter expense
    expense = float(input())
    total = total - expense                     #Calculate total
    print('Do you have another expense? (y/n)') #Prompt user if they have another expense to add (y/n)
    cont = input()
    


# Display results Include formating for currency.

print('Amount in account before expenses subtracted', "${:,.2f}".format(start_amount))
print('Number of expenses entered:', num_expense)
print('Amount in account After expenses subracted is', "${:,.2f}".format(total))
