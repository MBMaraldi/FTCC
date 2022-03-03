# CTI-110
# P3HW2-Salary  
# Mary Beth Maraldi
# 8 Oct 2021 
# Salary Counter

################# UPDATED ######################

#CTI-100
#P4HW2-SalarCal
#Mary Beth Maraldi
#updated 10/24/2021
# Salary Counter

# create a Salary Calculator and display results

import math
#create variables 
emp_name = input("Enter employee's name or \"None\" to terminate: ")
emp_count = 0
total_emp_ot = 0
total_gross_pay = 0
total_reg_pay = 0

# Create loop to enter new employee info
while emp_name != 'None':
    #Requests and gather input data
    hrs_worked  = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    #Determine if there is overtime, if so, then calculate reg pay and ot pay
    if (hrs_worked <= 40):
        over_time = 0
                 
    else:
        over_time = abs(40 - hrs_worked)
        hrs_worked = 40

    # Primary Equations needed for calculations
    emp_hrs = hrs_worked + over_time
    ot_pay = over_time * (1.5 * pay_rate)
    reg_pay = pay_rate * hrs_worked
    gross_pay = ot_pay + reg_pay
    emp_count += 1
    
    # Calculate overall totals
    total_emp_ot = total_emp_ot + ot_pay
    total_reg_pay = total_reg_pay + reg_pay
    total_gross_pay = total_gross_pay + gross_pay
    

    ##Print table with calculations
    print("----------------------------------------------")
    print("Employee name:\t", emp_name)
    print()
    print("Hours Worked \t Pay Rate \t OverTime \t OverTime Pay \t RegHour Pay \t Gross Pay")
    print("-------------------------------------------------------------------------------------------")
    print(emp_hrs, '\t\t', pay_rate, '\t\t', over_time, '\t\t', ot_pay, '\t\t', '${:,.2f}'.format(reg_pay), '\t', '${:,.2f}'.format(gross_pay))
    print()
    print()
    emp_name = input("Enter employee's name or \"None\" to terminate: ")

print()
print()
print("Total number of employees entered:", emp_count)
print("Total amount payed for overtime:", "${:,.2f}".format(total_emp_ot))
print("Total amount payed for regular hours:", "${:,.2f}".format(total_reg_pay))
print("Total amount payed in gross:", "${:,.2f}".format(total_gross_pay))






