# Strings
# Bunch of characters it would take
# ' ' , " " , ''' ''' , """ """ these are valid
name = 'Shivam'
print(name)
name = "Harry"
print(name)
name = """Harry is a good person, he love to walk alone
he has a dog, he believe in god"""
print(name)

dir1 = "c:\nomediar\somedir"
# if we use double quotes or single quotes while in the case of directory,
# \n is creating a new line here, now how to do it , let's go
print(dir1)

dir2 = r'c:\nomediar\somedir'
# r is used to treat the backslash as a normal character or raw string
print(dir2)

# Format of the string
first_name = 'Shivam'
Last_name = 'Kumar'
print(first_name + " " + Last_name)
print(first_name, "", Last_name)  # This is the format of the string and both of them are same
print(first_name, Last_name)  # This is the format of the string and both of them are same
print(f'Your full name is {first_name} {Last_name}') #here f is used for formatting
#if we remove f, it would not take the same values as it would consider it as a complete string
#f -> used for formatting and it would replace the value of variables
# {} -> Placeholders

# String Slicing
name = "Shivam"
