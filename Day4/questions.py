# # Accept two numbers from user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))


# if num1 > num2:
#     print("The greater number is:", num1)
# elif num2 > num1:
#     print("The greater number is:", num2)
# else:
#     print("Both numbers are equal.")
    

# gender= (input("What is your gender: ")) 

# if gender == 'M':
#     print("Good morining sir!")
# elif gender == 'F':
#     print("Good Morning Mam!") 
# else:
#     print("Good Morinig!")


# Accept an integer and check whether it is an even number or odd.  

# num1 = int(input("wirte the first num1 :  " ))
# num2 = int(input("wirte the second num2 :  " ))

# if num1%num2 == 0:
#     print("Number is even")
    
# else:
#     print("number is odd ")


#Accept name and age from the user. Check if the user is a valid voter or not. 
name = input("Please write you name:  ")
age  = int (input("Please provide you age : " )) 


if age > 18 :
    print("You are eligible  for for vote!")
    
else:
    print(f"Hello {name} You are not eligible for vote ")