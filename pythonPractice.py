# most python code requires correct indentation
#correct
if 5 > 2:
    print("five is greater than two!")

if 5 > 2:
 print("five is greater than two!")
if 5 > 2:
            print("five is greater than two!")

 #incorrect
#if 5 > 2:
#print("five is greater than two!")
    #print("five is greater than two!") 

#variables 
x=5
y = "hello"
print(x) #i printed this version of x so it gives 5
print(y)
#can reasign values based on order
x="no"
print(x)# this version of x is different
#will not be shown
"frick"
5
#specifying data types
x=str(3)#string "3"
print(x)
print(type(x))
y=int(3)#number 3
print(y)
z=float(3)# decimal 3.0
print(z)
#if want to print datatype only
x=5
y="john"
print(type(x))
print(type(y))
#can use double or single quotes
# variable names are case sensitive
#must start with letter or underscore
#can only contain A-z 0-9 and _
#good
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#bad
# 2myvar = "John"
# my-var = "John"
# my var = "John"
#you can assign values to multiple variables in one line variables and values must be in order
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#you can assign the same value to multiple variables on the same line
x = y = z = "Orange"
print(x)
print(y)
print(z)
#Using = sign in an if statement it will be improper syntax

#There are 3 data types for numbers:

integer=3

float=3.0

complex=3j

#To verify the data type use print(type())

#Int: or integer, is a whole number, positive or negative, without decimals, of unlimited length.

#Float: "floating point number" is a number, positive or negative, containing one or more 

#decimals. (float can also be scientific numbers like E= power of ten EX: e100)

#Complex: numbers are written with a "j" as the imaginary part

#It’s possible to convert a datatype using 
#starts as 
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

#verify number
print(a)
print(b)
print(c)

#verify conversion
print(type(a))
print(type(b))
print(type(c))

#how to make random numbers

#no random function in python unlike javascript but there is a built in module you can import
#importing modules

import random
print(random.randrange(1, 10))

#With casting I can specify a the datatype i want

a=3.0 is a float but 

a=int(3.0) is no longer a float it is an integer

#Other example 
a=str(3) a=float(3)

#To have a multiline string use triple quotation marks single or double doesn’t matter.
#EX:
a=”””hello
There
Guys”””

#Strings are arrays each letter counts

A=”hello”

#Each letter h e l l o is separate and can be called separately

print(a[1])

#Would print letter e

#Python string arrays start at 0,1,2,3,4 and brackets are used to specify what you want to print from a string array

#n python I can use a for loop to print each letter on a separate line

for x in "banana":
  print(x)

#TO print the length of an array use print(len(x))

a = "Hello, World!"
print(len(a))

#To print something specific from an array use

txt = "The best things in life are free!"
print("free" in txt)

#In is used to specify 

#Way to use an if statement with string arrays and in 

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#How to check if something is not in an array and how to use an if statement with it

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#How to print only from a specified start to a specified end Slicing

b = "Hello, World!"
print(b[2:5])

#Unspecified start to specified end

b = "Hello, World!"
print(b[:5])

#Specified start to unspecified end

b = "Hello, World!"
print(b[2:])

#Negative indexing starts from the very end -1 going to left is -2 etc

#Positive starts from right to left
print(b[2:5])

#Negative starts from left to right
print(b[-5:-2])
 
#String modifications

#.upper can be used to make all letters in a string uppercase
a = "Hello, World!"
print(a.upper())

#Lower case
a = "Hello, World!"
print(a.lower())

#To remove white unneeded white space in a string

a = " Hello, World! "
print(a.strip())

#Would print Hello, World

#To replace values in a string use

a = "Hello, World!"
print(a.replace("H", "J"))

#The first value is what I want to replace while the second is what I am replacing it with

#I can split a string into two separate strings
a = "Hello, World!"
b = a.split(",")
print(b)

#Would print [‘hello’, ‘world’]

#The value you put in is where the string would be split from

#I can merge two variables into 1

a = "Hello"
b = "World"
c = a + b
print(c)
#‘Helloworld’

#To add a space use an empty string

a = "Hello"
b = "World"
c = a + “ ” +b
print(c)
#‘Hello world’

#I can not combine different datatypes a work around can be is changing the data types
a = "Hello"
b = 32
c = a + “ ” +b
print(c)
#‘Error’

#Another way to change to bypass the error is use .format to insert a number
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#My name is John, and I am 36

#I can use curly brackets to indicate where I want to insert

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 

#I want 3 pieces of 567 for 49.95 dollars.

#I can use indicators in the order 0-infinity to specify where I want the values to be placed

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

#To insert characters in a string that would produce an error EX:

exampleErrorString=”The book was called “Krik?Krak!” I think”

#Example with escape characters
exampleString=”The book was called /“Krik?Krak!/” I think”

#Other examples of escape characters 
Single quote
txt = 'It\'s alright.'
print(txt) 

#Backslash this example only allows one but can be infinite
txt = "This will insert one \\ (backslash)."
print(txt) 

#New line basically just pressing enter
txt = "Hello\nWorld!"
print(txt) 
#Windows, Linux and Unix use \n
#Return carriage the same as pressing enter but only window uses it

txt = "Hello\rWorld!"
print(txt)

3Makes a tab space
txt = "Hello\tWorld!"
print(txt) 

#Backspace
txt = "Hello\bWorld!"
print(txt) 

#The octal value is the numbers that correspond to letters 
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#Hex values to create letters
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

	#		Used in print
capitalize()
#Converts the first character to upper case
casefold()
#Converts string into lower case
center()
#Returns a centered string
count()
#Returns the number of times a specified value occurs in a string
encode()
#Returns an encoded version of the string
endswith()
#Returns true if the string ends with the specified value
expandtabs()
#Sets the tab size of the string
find()
#Searches the string for a specified value and returns the position of where it was found
format()
#Formats specified values in a string
format_map()
#Formats specified values in a string
index()
#Searches the string for a specified value and returns the position of where it was found
isalnum()
#Returns True if all characters in the string are alphanumeric
isalpha()
#Returns True if all characters in the string are in the alphabet
isdecimal()
#Returns True if all characters in the string are decimals
isdigit()
#Returns True if all characters in the string are digits
isidentifier()
#Returns True if the string is an identifier
islower()
#Returns True if all characters in the string are lower case
isnumeric()
#Returns True if all characters in the string are numeric
isprintable()
#Returns True if all characters in the string are printable
isspace()
#Returns True if all characters in the string are whitespaces
istitle()
#Returns True if the string follows the rules of a title
isupper()
#Returns True if all characters in the string are upper case
join()
#Joins the elements of an iterable to the end of the string
ljust()
#Returns a left justified version of the string
lower()
#Converts a string into lower case
lstrip()
#Returns a left trim version of the string
maketrans()
#Returns a translation table to be used in translations
partition()
#Returns a tuple where the string is parted into three parts
replace()
#Returns a string where a specified value is replaced with a specified value
rfind()
#Searches the string for a specified value and returns the last position of where it was found
rindex()
#Searches the string for a specified value and returns the last position of where it was found
rjust()
#Returns a right justified version of the string
rpartition()
#Returns a tuple where the string is parted into three parts
rsplit()
#Splits the string at the specified separator, and returns a list
rstrip()
#Returns a right trim version of the string
split()
#Splits the string at the specified separator, and returns a list
splitlines()
#Splits the string at line breaks and returns a list
startswith()
#Returns true if the string starts with the specified value
strip()
#Returns a trimmed version of the string
swapcase()
#Swaps cases, lower case becomes upper case and vice versa
title()
#Converts the first character of each word to upper case
translate()
#Returns a translated string
upper()
#Converts a string into upper case
zfill()
#Fills the string with a specified number of 0 values at the beginning

#Booleans true or false

print(i>5)greater
print(i<5)less
print(i==5)equal

#If and else
a = 200
b = 33

if b > a:
  print("b is greater than a") false
else:
  print("b is not greater than a") true

#print(bool()) is used to test if something is true or false

#Rules of whether or not something is true.
#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones
#All of these rules apply to functions as well

#function with if yes or no
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#how to make a true or false if a variable is a certeain datatype
x = 200
print(isinstance(x, int))
#asking is X and integer
#using print I can use math operaters to add, subtract, multiply, divide, modulus, exponents, and floored division
a=10
b=20
print(a + b)
print(a - b)
print(a * b)
print(b / a)
print(a ** b)
print(10 // 2)
print(10.0 // 2.0)
print(-10.0 // 2.0)
print(-10 // 2)
#camparison operaters
a=10
b=20
if (a==b):
	print("yes it is")
else:
	print("no it is not")

a=10
b=20
if (a > b): #if (a < b) if (a<=b) if (a>=b)
	print("yes it is")
else:
	print("no it is not")

#python math variables in a varaible
a=10
c=20
c+=a
c-=a
c*=a
c/=a
#modules
c%=a
c**=a
c//=a

#logical operaters
#if both are true
a=10
b=20
a=10
b=20
#both have to be true
print(a>5 and b>15)

#if one is false are non zero
print(a or b)
   
#returns false if true and returns true if false
print(not(a and b))
print(not(a>15 and a>20))

#returns true if both variables are the same object
x=10
y=10
print(x is y) # true
print(x is not y) # false
x=12
y=13
print(x is y) #false
print(x is not y)# true

#lists, tuples, sets, and dictionarys are used to store multiple items
#list
myList= ["apple", "banana", "cherry"]
# list items are ordered in index [0-infinite], allows duplicates, and changeble
# the order of the numbers will not change
#new items added through code will be added at the end of the list
#len() function works on lists
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#the letters are not counted but each item is counted
# True and False need to be capitilzed
#using type will identify only that its a list but not whats inside unless using and index
#using the list constructor can specifcally identify that its a list
#negative indexing starts from the end not from 0 but -1
#I can specify a range of indexes that I want to print
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#I can not specify a start and it wil start from the begining and I might not specify a end so it will print all of the items
#negative indexing can be used as well
#the specified end index will not be included. True for negative indexing as well
#in can be used to test if a specified item is in a list
myList = ["apple", "banana", "cherry"]
if "apple" in myList:
  print("Yes, 'apple' is in the fruits list")
#I can change what the index equates to
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#I can change a range of values using index also possible with negative index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#if you edit an index with more values
thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)
#['apple', 'blackcurrant', 'watermelon', 'cherry']
#with less
thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)
#['apple', 'watermelon']
#insert can be used to add an item in a specific area wthout replacing the value
thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist) 
#append can be used to add to the end of the list
thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)
#.extnd will add 2 lists
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)
#to remove an index
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#to pop an index the deleted index will be returned
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#if you don't specify the index the last index will be removed
#del is the same as remove but with different syntax
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#del can also delete an entire list
thislist = ["apple", "banana", "cherry"]
del thislist
#clear does not delete the list but deletes the indexes inside th list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#to sort a list this eill sort all strings with letter a into the new array
#x is used as a variable that can change as its iterated through the array
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#list comprehension allows shorthand old list is unchanged
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#if i want to make a new list without a specific element
newlist = [x for x in fruits if x != "apple"]
#range can be used to iterate through a number starting from 0 ending at 9. Ten is not included only works on lists tuples and sets
newlist = [x for x in range(10)]

print(newlist)
#this allows numbers lower than 5 range can be anything and sign can be anything as well
newlist = [x for x in range(10) if x < 5]
#any types of manipulations and loops can be done in list
newlist = [x.upper() for x in fruits]
#I can overide values in a list the original fruit list will stay
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)
#while the x is iterating and copying the fruits array once x=banana x will be replaced with orange
newlist = [x if x != "banana" else "orange" for x in fruits]
#.sort is used in a list to sort items aplabetically and numerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thisList=[100,10,1,1000]
thisList.sort()
print(thisList)
#setting sort reverse = true will reverse the alphabetical order or number order Z-A
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#
