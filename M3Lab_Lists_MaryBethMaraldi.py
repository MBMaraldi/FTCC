# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 18:29:45 2022

@author: mbsmi
"""

# Collect Week's Daily Sales and Generate Reports
# Feb 13, 2022
# CSC-121 M3Lab - Lists
# Mary Beth Maraldi


# request sales for each day of the week
# create list Days of week (Mon-Sun)
# Display min, max, and sum
# format for currency

Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

Sales=[]

def get_sales():
    
    for i in range(0,len(Days)):            
        n = float(input(f'Enter generated sales for {Days[i]}: '))
        Sales.append(n)     #adds values to list  
    return Sales
    


def dis_results(Sales):
    print('--------------Results--------------')   
    
    
    high = Sales.index(max(Sales))     # get index for  corresponding value    
    print('Highest\t\t', Days[high],'\t', '${:,.2f}'.format(max(Sales)))


    low = Sales.index(min(Sales))     # get index for corresponding value
    print('Lowest\t\t', Days[low],'\t', '${:,.2f}'.format(min(Sales)))


    print('-----------------------------------')
    print('Total Sales:\t\t\t', '${:,.2f}'.format(sum(Sales)))
    

dis_results(get_sales())

