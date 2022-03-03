#   Account with Interest Calculator
#   1/27/2022
#   CSC121 M1HW1-Debugging
#   Mary Beth Maraldi

#   Display the amount of money in an account for each year from 1-30 with 7% interest (this is demonstrated as an initial investment of 1000)
# 
#   create "for" loop that:
#      increase year (n) and displayes f'string   

for i in range (30):
    n = i+1
    print(f'Amount after {n} years:', 1000 * (1 + .07) ** n)

