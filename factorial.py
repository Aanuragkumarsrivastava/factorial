#program to calculate the factorial of the number

num=int(input("Enter number:"))#taking the number whose factorial is to be calculated

fact=1#setting  the value of fact as 1

while(num>0):#checking the number which is entered by the user is greater than zero

    fact=fact*num#calculating factorial
    
    num=num-1#entered value will be decremented by 1 and loop continues
    
print("Factorial of the number is: ")#printing the result ,the factorial of the number

print(fact)
