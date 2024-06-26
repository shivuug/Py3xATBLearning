#string
#strings have some prebuild functions
#Function -> Repeat a task - you can use a function
# print, type, input, format, max, min, ID(gives memory address), length, sum, average
name="SHivam"
print(name)
print(type(name))
print(id(name)) #return of the identity and stored in memory address
print(len(name)) #length of the string, always count from 1
name=name.upper() #returns a copy of the string with all characters converted to uppercase
print(name)
name=name.lower() #returns a copy of the string with all characters converted to lowercase
print(name)
#name=name.(Can have multiple functions available here)
a=name.count('a') #Return the number of non overlapping occurance of sub string in the string
print(a)
print(name[0])
print(name[5]) #this is index which is (length-1)
#print(name[6]) #this will give error as index is out of range
print(name[-1]) #this will print the last character of the string

#Python - Strings are immutable which means that can't be changed.
name[0]='P' #'str' object does not support item assignment means you won't change the value in a string but
 #you can reassign it.



