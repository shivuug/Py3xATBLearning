#Take two integer number frmo the user and add them

num1 = input("Enter the first number:") #because input function reads string from a function
num2 = input("Enter the second number:")
result = num1+num2 #This will give error because the input function will take the input as string
print(result) #This will print the concatenation of the string

#To overcome this we need to type cast the input to integer
#we have to convert this string to integer
num3 = int(input("Enter the first number:")) #Type casting to integer
num4 = int(input("Enter the second number:")) #Type casting to integer
result1 = num3+num4
print(result1)

#For example
name1 = input("Enter the first name:")
name2 = input("Enter the second name:")
result2 = name1+name2
print(result2) #This will print the concatenation of the string


#convert string -> integer = use int()
#convert string -> float = use float()
#convert string -> boolean = use bool()
#convert string -> complex = use complex()
print(type(int(num1)))