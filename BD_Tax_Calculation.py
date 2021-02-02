income = int(input("Please enter your income amt:"))
flag = 0
tax = 0
tax_per = 0

if income > 300000:

     income -= 300000
     tax_per = 0
     tax = 0
    
while income > 0:


    
    if income > 100000:

        income -= 100000
        tax_per += 5
        tax += 100000 * (tax_per/100)

    elif income > 300000:

        income -= 300000
        tax_per += 5
        tax += 300000 * (tax_per/100)

    elif income > 400000:

        income -= 400000
        tax_per += 5
        tax += 400000 * (tax_per/100)

    elif income > 500000:

        income -= 500000
        tax_per += 5
        tax += 500000 * (tax_per/100)

    elif income > 0:
        
        tax_per += 5
        tax += income * (tax_per/100)
        income -= income


print(tax)