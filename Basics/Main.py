print("please enter your first number")
num1 = int(input())
print("please enter your second number")
num2 = int(input())
#checking if the second number is zero
if num2 > 0:    
    #print the total
    print(num1/num2)
else:
    print("you cannot divide by zero")