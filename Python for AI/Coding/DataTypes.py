# int and float
#integers - whole numbers
print(type(2+4))
print(type(2-4))
print(type(2*4))
print(type(2/4))

print(2**3) # 8
print(5//4) # 1
print(6%4) # 2

# type() -> gets type of the data
# we require more memory for float than int

# math functions not required to memorize we will google them
print(round(5.83))
print(abs(-10)) # convert to positive number

# Developer fundamentals
# Don't read dictionary no need to read all things

# operator precedence
# (),**, *, /, +, -

# Complex numbers 4+5j 
print(bin(5)) # return binary representation 0b101 0b - binary representation
print(int('0b101',2))


# variables - container to store information
iq = 190 # iq is variable 
print(iq)

# naming rules for Varaibles 
# snake_case
# start with lowercase or underscore(private variable)
# Letters,numbers, underscores allowed
# case sensative
# don't overwrite keywords (inbuilt python keywords like print, if, for)
# shouldn't create variables with double underscore (dunder)

a,b,c =1,2,3
print(a)
print(b)
print(c)

# Expressions vs Statements
# Expression -- piece of code that returns value

iq = 100 #> statement
iq/4 #> expression
user_age = iq/4 #> statement

# augmented assignment operator
# +=
# -=
# /=
# /=
some_value = 5
some_value += 2
some_value = some_value + 2