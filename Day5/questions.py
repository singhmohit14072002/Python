# print the table  of 5 

# n = int(input("Which table you want print :  "))


# for i in range(n,(n*10)+1,n): 
#     print(i)


    
#Accept an integer and Print hello world n times  

# n = int(input("How many times you want to print the hello world:   ")) 


# for i in range(n):
#     print("Hello world!")   


# Reverse for loop. Print n to 1  

# n = int(input("Enter the number! ")) 

# for i in range(n, 0 , -1):
#     print(i)   

#Sum up to n terms   


# n = int(input("Enter  the number: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
#     print(f" your answer is :  {sum}")

#Print all the factors of a number  

# n = int(input("Enter the number you want that factorial! :  "))

# fact = 1

# for i in range(1, n+1):
#     fact = fact * i
    
#     print(f"the factorial of your number is {fact}")

#Accept a number and check if it a perfect number or not.
# A number whose sum of factors is equal to the number itself   


# n = int(input("Enter your number : -  ")) 

# for i in range(1, n):
#     if n%i == 0:
#         sum = sum +i 
#     if sum == n:
#         print ("Your number is perfect number")
#     else:
#         print("your number is not perfect number ")
# n = int(input("tell your number "))
# even = 0
# odd = 0
# for i in range(1, n+1):
#     if i%2  == 0:
        
#         even = even + i 
        
#     else:
#         odd = odd + i
#         print(f"thrn sum of even and odd are {even}, {odd}")    


# Reverse a string without using the build in function 

# a = "MOHIT"
# print(a[::-1])  


#Check string is palidrome or not 


# a = "NMAN"
# b = ""

# Reverse the string
# for i in range(len(a) - 1, -1, -1):
#     b += a[i]

# Check if palindrome
# if b == a:
#     print("String is a palindrome")
# else:
#     print("String is not a palindrome")


# Count all letters, digits, and special symbols from a given
# string
# Given: str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total counts of chars, digits, and symbols
# Chars = 8
# Digits = 3
# Symbol = 4


a = "P@#yn26at^&i5ve"

char = 0
dig = 0
spchr = 0
for i in a:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char +=1
    else:
        spchr  += 1
        
        print(f"your digit are {dig} , your character are {char} , your special char {spchr}")
        
    
        