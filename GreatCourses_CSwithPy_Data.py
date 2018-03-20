"""
books referenced:
Matthes, Python Crash Course. ch.15
Gires, Practical programming.  ch. 14, 11
Lambert, Fundamentals of Python. ch. 5,6,7,8,11
Zelle, Python programming. ch. 9, 12

"""

# --  Ch.16 Visualizing Data and Creating Simulations --
""" how to visualise data that we have and don't have
1) how to create charts, plots and graphs from data
2) beyond existing data -> simulations
"""

import matplotlib.pyplot as plt
import random

# --  1. Visualizing Data  --
"""
from matplotlib import pyplot

#empty plot
plt.axes()
pyplot.show() #block=True if want to see the image


#basic plot
plt.plot([0,1,2,3,4,5],[0,1,4,9,16,25])
plt.axes([0,5,0,25])
plt.show()


from matplotlib.pyplot import plot, axis, show, legend #importing functions from pyplot

#draw squares
xlist=range(0,6)
ylist =[]
for i in xlist:
    ylist.append(i*i)
plot(xlist,ylist, label = 'Squares', marker='+', color='red',markeredgecolor='blue')
axis([0,5,0,25])
legend()
show()


from matplotlib.pyplot import plot, axis, show, legend #importing functions from pyplot

#can also make 2 plots on the same graph
#draw squares and cubes

xlist=range(0,6)
ylist =[]
ylist2=[]
for i in xlist:
    ylist.append(i*i)
    ylist2.append(i**3)
plot(xlist,ylist, label = 'Squares', marker='+', color='red',markeredgecolor='blue')
plot(xlist,ylist2, label = 'Cubes', marker='o', color='green',markeredgecolor='blue')

axis([0,5,0,125])
legend()
show()
"""
# --  2. Creating Simulations --
"""
2 main ideas:
Model - tells us what the laws, rules or processes that we're trying to compute should follow
Actual simulation takes the model and some set of conditions and uses it to determine 
how the situations develops (over time)
The model is most important, if incorrect won't get the correct answer.  
Important to have the correct initial conditions.  Tiny initial errors can have large effects later.

"""

"""
#i.e. how the account accumulates interest over time

#set initial conditions
time=0
balance = 1000
interest = 0.03
#set initial vars
timelist =[time]
balancelist =[balance]

while (time < 100):
    #increase balance and time
    time += 1
    balance += balance * interest
    timelist.append(time)
    balancelist.append(balance)

#output the simulation results
for i in timelist:
    print (timelist[i], ": ", balancelist[i])
plt.plot(timelist, balancelist)
plt.show()
"""

# --  2a. Monte Carlo Simulations --
"""
based on the idea of simulation lots of random events
but doing it enough times that the overall outcome will be more understandable
useful in situations with uncertainty: physics, finance
"""

"""
#compute change per year
def changeInBalance(initial_balance):
    #rate = 0.03 #fixed, guaranteed
    rate = random.uniform(0.0, 0.06) #pick a random rate
    return initial_balance * rate

time=0
balance = 1000

#set initial vars
timelist =[time]
balancelist =[balance]

while (time < 100):
    #increase balance and time
    time += 1
    balance += changeInBalance(balance)
    timelist.append(time)
    balancelist.append(balance)

#output the simulation results
for i in timelist:
    print (timelist[i], ": ", balancelist[i])
plt.plot(timelist, balancelist)
plt.show()


#to get a better feel for average performance, wrap the simulation into a loop and run over and over
#compute change per year
def changeInBalance(initial_balance):
    #rate = 0.03 #fixed, guaranteed
    rate = random.uniform(0.0, 0.06) #pick a random rate
    return initial_balance * rate

#generalize
n_years = 10
n_sims = 1000

#keep track of final balances only
final_balances =[]

for i in range(n_sims):

    #set initial conditions
    time=0
    balance = 1000

    while (time < n_years):
        #increase balance and time
        time += 1
        balance += changeInBalance(balance)

    # keep track of final balances for each simulation
    final_balances.append(balance)

#output the simulation results
for i in range(n_sims):
    print (final_balances[i])

#output the simulation results - as a plot of # simulations
plt.plot(range(n_sims), final_balances)
plt.show()
#output the simulation results - as a histogram
plt.hist(final_balances, bins=20)
plt.title('Great Courses - Financial Simulations')
plt.show()

#Conclusion:
#when we run this we get a wide distribution of results, with cases where we earned a little to cases where we earned a lot
#to understand an overall performance, we can compute some basic statistics
import statistics as stats

print(stats.mean(final_balances), stats.stdev(final_balances))
"""

#--  Ch.18 JSON and Pickle
"""
2 important python modules, that make objects much more usable. 

1. JSON (javascript object notation) 
is a way of structiuring data in a text format.   
A human readable string as opposed to binary data.   
Groups information in objects using {name: value}.  Value can be a nested object. 
Common format to transfer data over the web. 
 
"""
import json
"""
myfile = open('json.txt','w')
#create json string
data = ['hello','goodbye']
json_string = json.dumps(data)
myfile.write(json_string+'\n')
myfile.close()

#read json file
myfile1 = open('json.txt','r')
json_string1 = myfile1.readline()
data1 = json.loads(json_string1)
myfile1.close()
print(data1)


#create a file containing 3 json strings
length = 20.0
width = 15
outfile = open('datafile.dat','w')
#create json string
json_string = json.dumps(length)
outfile.write(json_string+'\n')
json_string = json.dumps(width)
outfile.write(json_string+'\n')
json_string = json.dumps("Data for an example")
outfile.write(json_string+'\n')
outfile.close()

#read and use json file
infile = open('datafile.dat','r')
#create json string
json_string = infile.readline()
l = json.loads(json_string)
json_string = infile.readline()
w = json.loads(json_string)
json_string = infile.readline()
description = json.loads(json_string)
infile.close()
print(description, ':', l*w)

#use object.__dict__ 

"""

"""
Pickle 
Read and write data other than strings more easily.   
Lets read and write data from a file in binary format (images, word-processing files, models) 
Python specific format.  if writen with pickle commands, needs to be read by a python program also using pickle commands.  
Don't read pickled by other data, unless sure of the source.  easy to contain malicious code. 
Only use it for pickling your own data [need to preserve state]. 
"""

"""

import pickle

account = '12345'
owner = 'me'
balance = 10000

#write a file with pickle
outfile = open('BankAcct.data','wb')
pickle.dump(account,outfile)
pickle.dump(owner,outfile)
pickle.dump(balance,outfile)
outfile.close()

#read a file produced with pickle
infile = open('BankAcct.data','rb')
account_in = pickle.load(infile)
owner_in = pickle.load(infile)
balance_in = pickle.load(infile)
infile.close()
#actually get an object back, not a string
print(owner_in, ' has ', balance_in)
"""

#--Ch.19. Data Structures: Stacks, Queue, Dictionary, Set --
"""
Stack - push and pop operations
Represented using a list.
"""

""" 
class Book:
    title=''
    author=''

#create specific books
long_book = Book()
long_book.title='War and Peace'
long_book.author='Tolstoy'

med_book = Book()
med_book.title='the Great Gatsby'
med_book.author='Fitzgerald'

short_book = Book()
short_book.title='Vegies I like'
short_book.author='John Keyser'

#to push a book onto the stack, use append command
book_stack =[]
book_stack.append(med_book)
book_stack.append(short_book)
book_stack.append(long_book)
#in memory, this set of books is treated as a list, whith books listed in order.
#conceptially, visualize as a stack.
#pop the top book off of the stack.
#lists have a built-in method named 'pop', which removes the last item from a list and returns it.
next_book = book_stack.pop()
print (next_book.title + " by " + next_book.author)

#key is to think of it as a stack, even though implemented as a list
#stacks gives LIFO
# create a separate Stack class, with push and pop operations

class Stack():
    _stack = []
    def push(self,item):
        self._stack.append(item)
    def pop(self):
        self._stack.pop()
"""

"""
#i.e. Solitaire - not completely setup
waste_pile = Stack()
#setitng up game here
while not (noTurnLeft()):
    # get the player's move

    if move=='Draw':
        #get next 3 cards on push them onto waste stack
        next_card1=draw_next_card()
        next_card2 = draw_next_card()
        next_card3 = draw_next_card()
        waste_pile.push(next_card1)
        waste_pile.push(next_card2)
        waste_pile.push(next_card3)

    elif move=='Play from Waste':
        #player wants to play the top card from the waste pile
        current_card=waste_pile.pop()

        #have player play current card
"""

"""
Queue 
If we want the opposite of stack, or FIFO.   
Can implement with a list. 
Order of queue is same as list order. 
Can push new objects onto the end of the list using the append command. 
Instead of popping from the end of the list, an element is taken off the front. Pop command can take a param, indicating which element gets taken off the list.  default param is the final element.   
to take off the first element, we pass in 0 and the 1st element is removed.   """

""" 
#create a book queue - empty list.  to add a book, use append command
book_queue =[]
book_queue.append(med_book)
book_queue.append(short_book)
book_queue.append(long_book)
#take a book from the queue
next_book = book_queue.pop(0)
print (next_book.title + " by " + next_book.author)

#queues gives FIFO
# create a separate Queue class, with push and pop operations

class Queue():
    _queue = []
    def enqueue(self,item):
        self._queue.append(item)
    def dequue(self):
        self._queue.pop(0)  #$acadd return here
    def isEmpty(self):
        return (len(self._queue)==0)
"""

""" 
Hash table aka Dictionary
"""
"""
my_dictionary = {}
nicknames = {'a':'anya','b':'banya','s':'sanya','d':'danya'}
print(nicknames)
#access with an index which is not a numerical value, but key
print(nicknames['b'])

#can build up in a different way, begin with an empty dict and assign elements one by one
nicknames={}
nicknames['a']='alpha'
nicknames['b']='beta'
nicknames['g']='gamma'
nicknames['d']='delta'
nicknames['e']='epsilon'
print(nicknames['b'])

#Putting something into a dict requries 2 parts: a key and a value
#key - any immutable data type (no list or object)
#value - can be mutable or immutable

#to delete an item
del nicknames['e']
#to check whether or not a key is in dict
print ('b' in nicknames)
print ('e' in nicknames)

#loop
for nickname in nicknames:
    print("the nickname for "+nicknames[nickname]+" is "+nickname)
#may not be in the same order as put in
#underneath is a hash table, and order based on the values that the keys were hashed to.
#that specific information is hidden but we see the effects.
"""

"""
Sets
A diff way that hash tables can be used is accessible with another built-in Python data struct: the set 
A set is a collection of items stored using a hash table instead of a list 
so that it does mathematical set operations and checks set membership very quickly. 
"""

"""
#in contrast to dict, no kv pairs, just individual value items
ingredients = {'flour','suger','eggs','milk'}
if 'flour' in ingredients:
    print('yes')
else:
    print('no')

#can do the same with set command - takes a list as a param
#big advantage - set command allows to create an empty set
ingredients_set = set(['flour','sugar','eggs','milk'])
if 'flour' in ingredients_set:
    print('yes')
else:
    print('no')

#Sets have some addl operations defined on them that can be very useful.
#Add – to add a new element to a set
#Remove - to remove an element from the set
print(ingredients_set)
ingredients_set.add('baking soda')
print(ingredients_set)
ingredients_set.remove('milk')
print(ingredients_set)

#Set supports all the standard set operations such as union and intersection. But diff notation.
ingredients_cake = set(['flour','sugar','eggs','milk','butter'])
ingredients_omelet = set(['bell pepper','mushrooms','eggs','onion','butter'])
# minus - in one set but not the other
print ('diff :', ingredients_cake - ingredients_omelet)
# logical or - in one set or the other
print ('union : ',ingredients_cake | ingredients_omelet)
# and - in both sets
print ('intersection : ',ingredients_cake & ingredients_omelet)
# exclusive or - in either set but not in both; aka union - intersection
print ('xor : ',ingredients_cake ^ ingredients_omelet)

#another example - 3 dishes to make -> shopping list -> and list on hand
"""

"""
Summary 
Data structs provide an organization that lets us perform operations more effectively.  
Linear, sequential (using list) 
-Stacks 
-Queue 

Non-linear, non-sequential (using hash tables) 
-Dictionaries 
-Sets 

Just the beginning, in future lectures see a couple more: graphs and trees.  Hundreds are there used for specific operations. 
Idea: speed up operations on that data 
"""
