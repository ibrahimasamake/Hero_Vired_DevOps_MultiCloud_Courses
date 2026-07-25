print("Exo 1")

principal =  float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (as a percentage): "))
time = float(input("Enter the time in years: "))
interest = (principal * rate * time) / 100
print("The simple interest is:", interest)