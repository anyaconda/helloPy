#Great Courses - How to Program, Computer Science Concepts and Python Exercises
#Professor John Keyser, Ph.D.
#Texas A&M University
#https://www.thegreatcourses.com/courses/how-to-program-computer-science-concepts-and-python-exercises.html

#references
#python.org python tutorial


# --  Ch.5 Loops and Iterations --
"""
while loop when uncertain how many times to iterate
for loop with a well-defined set of items to loop thru
"""
"""
#equivalent while and for loops:
i=0
while i<5:
    print(i)
    i+=1

for i in range(5):
    print (i)
    
#Collatz Conjecture aka 3n+1 Conjecture, or Hailstone Sequence or Wondrous Numbers

#initialize
n=int(input("Enter a starting positive integer: "))
n_steps=0
while n!=1:
    if n%2==0:
        n=n/2
    else:
        n=n*3 + 1
    print(n)
    #increment number of steps
    n_steps+=1
print("Collatz Conjecture: we reached 1 in ", n_steps, " steps.")
"""

# --  Ch.6 Files and Strings --
"""
how to interact with files in storage
"""
"""
#open file for reading and read line by line
print ("Reading file foo.txt")
infile = open("data/foo.txt", "r")
#print (infile.readline(2))
print (infile.readlines())
infile.close()

with open("data/foo.txt", "r") as infile:
    l1 = infile.readline()
    l2 = infile.readline()
    print(l1 + l2)

#open file for reading and read the whole file into string    
with open("data/foo.txt", "r") as infile:
    wholefile = infile.read()
    print(wholefile)

#open file for writing
outfile = open("data/bar.txt", "w")
print (type(outfile))
outfile.writelines("bar1\n")
outfile.writelines("bar2")
outfile.close()
print ("Wrote file bar.txt")

#exercise
with open("data/data.txt", "w") as outfile:
    for i in range(1,11):
        outfile.write(str(i)+"\n")


#my - don't like that i have to count (unlike with vectors)
with open("data/data.txt", "r") as infile:
    sum=0
    i=0
    for l in infile: #don't even need 'for l in infile.readlines():'
        x=float(l)
        i+=1
        sum+=x
        #print(x, i)
print("\nCounted sum: " + str(sum) + " and average: " + str(sum/i))

#better way with enumarate
print("\nReading in file data.txt")
with open("data/data.txt", "r") as f:
    for i, l in enumerate(f):
        print (i, l)
        
#note: to work with plain text, use r w or a
#note: to work with binary files, use rb wb or ab
"""


# --  Ch.7 Operations with Lists --
"""
Python works particularly well with lists.  
History: started with processing census information
normally array, in Py array refers to something more memory efficient
while list is something more flexible
"""
mylist = [10,20,30,40,50,60,70] #the entire list
print (mylist[0]) #one element in the list

#how many elements in list
len(mylist)


#iterate over list
for i in mylist:
    print (i)
#sum without iteration
print (sum(mylist))

"""
#actions: appending, indexing, slicing and list of lists

#append: useful for building up lists
# merge lists with addition operator
list3 = [] #empty list
print(list3)

list1 = mylist
list2 = mylist
list3 = list1 + list2
print(list3)

list3+=list2
print(list3)

list3.append(100)
print(list3)

#index into a list
print(list3[0])
print(list3[-1]) #last element of the list
#slicing - a portion of the list
print(list3[0:3]) #first 3 elements, from 0 to 2
print(list3[:3])
print(list3[-3:]) #last 3
print(list3[:]) #entire list
#insert
list3[1:1] = [1,2,3] #insert 3 new values between 0 and 2
print(list3)

#want only first and last 3
list4=list3
n_list4=len(list4)
last3=n_list4-3
print(last3)
list4[3:last3]=[]
print(list4)

#strings are a slight variation of a list
#slicing on strings works similar
#except can't delete parts of a string

#lists of lists, can be of different types
lol = [[1,2,3], ["a","b","c"], [1.5, 2.5, 3.5]]
print(lol[1])
print(lol[2][0])
#useful: to represent a board of chess: 8 rows and and 8 columns

#lists can be of mixed types
# useful, i.e. credit card transactions
transaction = ['person1','iPhone',899.99,2]
transactions = [['person1','iPhoneX',1099.99,2],['person2','iPhoneSE',299.99,10]]
print(transaction)
#tuple - like a list but whose values can never changes; often with mixed data types
tuple_transaction = 'person1','iPhone',899.99,2
print(tuple_transaction)

tuple_car = "Buick","Century", 2007
make, model, year= tuple_car
print(make, model)
print(make, model, year)
"""

# --  Ch.8 Top-Down Design to Data Analysis Program --
"""
Weather patterns
.csv file with temps: date, high temp, low temp, rainfall 
Questions to answer:
-past temp on a specific day
-hottest/coldest temps
-average daily high/low
-largest one-day temp swing
-high/low in a month with a date in question
"""
"""
myProgram: top level design
-read in data
-analyze data
-present results
"""
"""

#### 1. read in data ####
#open .csv file - if .csv format, an extra step to handle line separator \r
with open("data/austin_weather_small.csv", "r") as filein:
    #print (filein.readline()) #for testing only, don't comment out
    s=filein.read()
    lines = s.split('\r')
    print(lines)
"""

"""
##my program
#open .txt file - no extra step, if .txt format and line separator \n
with open("data/austin_weather_small.txt", "r") as filein:
    #print (filein.readline()) #for testing only, don't comment out

    # read lines from file
    datalist = []

    for l in filein:
        # get data from line
        d, h, l, r = (l.split(',')) #want a tuple
        m, d, y = d.split('/')
        month = int(m)
        day = int(d)
        year = int(y)
        hightemp = int(h)
        lowtemp = int(l)
        rain = float(r)

        # put data into list
        datalist.append([month, day, year,  lowtemp, hightemp, rain])

print(datalist)

#### 2. analyze data ####
#find historical data for a specific date
month = int(input("Enter month: "))
day = int(input("Enter day: "))

#pull out historical data
mydata = []
for singleday in datalist:
    if singleday[0]== month and singleday[1]==day:
        mydata.append(singleday)
print(mydata)

#get aggregates - avg high and low
#skipped
myavg = (mydata[0][3]+ mydata[0][4])/2

#### 3. present results ####
print ("Avg temp on your day was: ", myavg )
"""

# --  Ch.9 Functions and Abstractions --


#  --  FUNCTION --

def f(a,b,c):
    """inputs: a, b
output: c"""
    return (a + b) / float(c)

#a = float(input("enter a: "))
#b = float(input("enter b: "))
#c = float(input("enter c: "))

#a docstring - standard way to document a function
#print (f.__doc__)
#help(f)

"""
result = f(3, 5, 7)
print (result)

#can return multiple variables, technically one value - a tuple, or a list of columns
myTuple = ("anya", "cha")
first, last = myTuple
print (first) #can access variables assigned from a tuple
print (myTuple[1]) #can access individual variables of a tuple
"""

def getBirthday():
    """ example function on using a tuple assignment"""
    m = '01'
    d = '02'
    y = '2018'
    return y, m, d




#to see function documentation
help(getBirthday)


#myBday_y, myBday_m, myBday_d = getBirthday()
#print (myBday_y)

def myFactorial(n):
    """get a factorial of n: product of all the numbers from 1 to n"""
    this_factorial = 1
    for i in range(1,n+1):
        this_factorial *= i
    return this_factorial

#print (myFactorial(4))

#potential side effects, aka bugs
def sumList(myList):
    for i in range(1, len(myList)):
        myList[i]+= myList[i-1]
    return myList[len(myList) - 1]
"""
#lists are mutable
testList = [5,3,2,1,4]
print(sumList(testList))
print(testList) #but in the process it changed the values of the list, not intended
"""


# --  Ch.10 Parameter Passing, Scope and Mutable Data --
""" how functions handle parameters and data
how to work with data types that are mutable 
parameters with default values"""
def myScope(myA, myB):
    """show how value of a, from main, is available for reading
    but if assign value to a inside function, that would be different local variable"""
    myA += a # go back to most recently defined a, which is in main routine below
    this_value=myA/float(myB)
    return this_value
"""
a=12
b=20
c=myScope(a,b)
print(c)
"""

"""sometimes need to access something outside the function
how to modify smth that not passed as a param"""
"""
def initialize():
    fuellevel = 100

fuellevel=0
initialize()
print(fuellevel) #still 0

def initialize():
    global fuellevel
    fuellevel = 100 #do change value in main program, discouraged

fuellevel=0
initialize()
print(fuellevel) #now 100
"""

""" languages differ in how scope works
pass by value - lack of effect on the calling function. only transmit the value of a param
pass by reference - local param is the same as the calling param, same memory location 
in python always pass by value
ways to affect params outside:
a) global var
b) mutable variables - can affect the value on the calling side
mutable means changeable when passed as a param
immutable: int, float, string; stays the same on the calling side
mutable: list, object; value can change"""

"""
def adder(v1,v2):
    v1+=v2 # append to existing list, same memory
n1=3
n2=4
adder(n1,n2)
print(n1) #still 3

n1=[1,2]
n2=[3,4]
adder(n1,n2)
print(n1) #now [1, 2, 3, 4]

#but
def adder(v1,v2):
    v1=[5] # assign a new list to value 1

n1=[1,2]
n2=[3,4]
adder(n1,n2)
print(n1) #still [1, 2]

#here's why
l1=[3,5]
l2=l1 #list2 points to the same list as list1
l2+=[7] #append one more item to existing list, same memory
# [3, 5, 7] this changes both lists
print (l1)

l2=[2,4,6] #assign a whole new list to l2
#list 2 points to a new list, list 1 stays the same
print(l1)
print(l2)
"""

#default params - in order or by key

# --  Ch.11 Error Types, Systematic Debugging, Exceptions --
""" 1) Syntax errors
2) run-time errors
3) logic errors

Build test suites - set of tests to run against code
-edge cases, aka extreme cases (or corner cases), jan 1, dec 31
-and a few in the middle, some other dates
-special cases, i.e. for dates Feb 29

Exceptions
way of handling the special error conditions that can occur when a program is running

try:
except e1:
except e2:
except:
else:
finally:
"""

"""
try:
    12/0 #ZeroDivisionError: integer division or modulo by zero
except ZeroDivisionError:
    print("Can't divide by 0")

try:
    filename = input("Enter filename: ")
    myfile = open(filename, 'r')
except NameError:
    print("Not defined")

#can raise an exception ourselves
month = input("Enter month: ")
try:
    if month <= 0 or month >12 :
        raise TypeError
except TypeError:
    print("Invalid month")
"""

# --  Ch.12 Python Standard Library, Modules, Packages --
""" many powerful functions in Python std library
modules knowns as libraries
packages, or bundles of modules

import command
"""

"""
import math
print (math.pi)

#how many already installed
#help("modules")

import moduleA #loads that file into your program

#bring in specific function(s)
from moduleA import functionA
print(functionA())

#Python standard library modules
#still have to import them to use them
print (math.sqrt(16))

import calendar
print(calendar.month(2020,1))
import time
print(time.ctime())

#3rd party packages: numpy, scipy, Beautiful soup
#not automatically included with python installation
#refer to pypi.python.org, search for pypi ranking.
#recommended tool to install packages: pip - from command line python -m pip install <pkg_name>
#import numpy as np
#a = np.arange(15).reshape(3, 5)
#print(a)
#didn't work, help("module") didn't show numpy
"""