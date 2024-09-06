#simple calculator for mathimatical operations wih user input support 

user_input1=float(input("enter first number : "))
user_input2=float(input("enter second number : "))

user_cal=input("which operation you want to perfume :\n  \n 1- (+) for Sum \n 2-(-) for Diffrence \n 3-(/) for Division \n 4-(*) forMultiplication ")

if user_cal=='+':
    result=user_input1+user_input2
    print(f"Sum of {user_input1} and {user_input2} is = {result} ")
elif  user_cal=='-':
    result=user_input1-user_input2
    print(f"Diffrence of {user_input1} and {user_input2} is = {result} ")
elif user_cal=='/':
    result=user_input1/user_input2
    print(f"Division of {user_input1} and {user_input2} is = {result} ")
elif user_cal=='*':
    result=user_input1*user_input2
    print(f"Multipliction of {user_input1} and {user_input2} is = {result} ")
else:
    print("Operation not found")
