#Function to calculate factorial using loop

def factorial(user): #making function
    base_value = 1
    for fact in range(1,user+1):
        base_value *= fact
    print(f"Factorial of {user} is {base_value}")


user = int(input("Enter number to calculate factorial : "))
factorial(user)#calling function


    
