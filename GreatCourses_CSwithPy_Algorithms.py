"""
books referenced:
Gires, Practical programming.  ch. 12,13
Lambert, Fundamentals of Python. ch. 3 p.60-70
Zelle, Python programming. ch. 13

"""

#--Ch.20. Algorithms: Searching and Sorting --
"""
A – a precise set of steps or rules to follow to accomplish some task.
#see OneDrive notes for pseudocode 

Search Algorithm 
Have a list and find whether a particular value is in a list or not. 
"""
#Linear search - go thru each element, checking to see if there's a match
"""
def isIn(L,v):
    i=0
    while i<len(L):
        if L[i]==v:
            return True
        else:
            i+=1
    return False

fave_foods = ['apples','pomegranates','cherries','salmon','potatoes','sushi']
doUHaveIt = isIn(fave_foods,'vodka')
print(doUHaveIt)
doUHaveIt = isIn(fave_foods,'cherries')
print(doUHaveIt)

#of course there's a built-in 'in' command - same in the background
print ('cherries' in fave_foods)

#Binary search
#let's assume the list is sorted, from smallest to largest

def binaryIn(L,v):
    #check if list is empty
    if len(L)<1:
        return False

    #if list is not empty
    low = 0
    high = len(L)-1
    if L[low]==v or L[high]==v:
        return True
    while low < (high - 1):
        midpoint = low + (high - low) // 2 #integer division
        if L[midpoint]==v:
            return True
        elif L[midpoint]< v:
            low = midpoint
        else:
            high = midpoint
    return False

fave_foods = ['apples','cherries','pomegranates','potatoes','salmon','sushi']
doUHaveIt = binaryIn(fave_foods,'vodka')
print(doUHaveIt)
doUHaveIt = binaryIn(fave_foods,'cherries')
print(doUHaveIt)

#find where in the list
def binaryIn(L,v):
    #check if list is empty
    if len(L)<1:
        return -1

    #if list is not empty
    low = 0
    high = len(L)-1
    if L[low]==v:
        return low
    elif L[high]==v:
        return high

    while low < (high - 1):
        midpoint = low + (high - low) // 2 #integer division
        if L[midpoint]==v:
            return midpoint
        elif L[midpoint]< v:
            low = midpoint
        else:
            high = midpoint
    return -1

fave_foods = ['apples','cherries','pomegranates','potatoes','salmon','sushi']
doUHaveIt = binaryIn(fave_foods,'vodka')
print(doUHaveIt)
doUHaveIt = binaryIn(fave_foods,'cherries')
print(doUHaveIt)
"""

"""
Sort algorithms
"""
"""
#Selection sort
def selectionSort(L):
    max_idx = len(L)-1

    for i in range(0,max_idx+1):
        # find the smallest remaining
        min_idx=i
        for j in range(i+1,max_idx+1):
            if L[j]<L[min_idx]:
                min_idx=j
        #swap that item
        temp=L[i]
        L[i]=L[min_idx]
        L[min_idx]=temp
#in-place sorting
fave_foods = ['apples','pomegranates','cherries','salmon','potatoes','sushi']
selectionSort(fave_foods)
print(fave_foods)

#Insertion sort
def insertionSort(L):

    for i in range(0,len(L)-1):
        # next element
        temp=L[i]
        j=i-1
        while j>=0 and L[j]>temp:
            L[j+1]=L[j]
            j-=1
        L[j+1]=temp

#in-place sorting
fave_foods = ['apples','pomegranates','cherries','salmon','potatoes','sushi']
selectionSort(fave_foods)
print(fave_foods)

#sorting is a common operation and Python has a built-in sorting function.
#for a list, call L.sort() - this in-place sort
#out-of-place sort, use function sorted()

fave_foods = ['apples','pomegranates','cherries','salmon','potatoes','sushi']
print('in-place sort: ', fave_foods.sort()) #error - didn't work
fave_foods = ['apples','pomegranates','cherries','salmon','potatoes','sushi']
fave_foods_sorted = sorted(fave_foods)
print('out-of-place sort: ', fave_foods_sorted)
print('out-of-place sort in reverse: ', sorted(fave_foods, reverse=True))
print('original list: ', fave_foods)
#Built-in sort() function is great.
# actually combines an insertion sort with merge sort (next lecture)
"""

# --  Ch.21 Recursion and Running Times --
"""
Recursion: Merge Sort 
Recursion can be, but not always, a great way to create efficient code.   
The great trick in recursion is that a function is calling itself. 
"""

"""
"""
#i.e. print a countdown
#function to take a number and then count down to 0
def countdown(n):
    print (n)
    if n>0:
        countdown(n-1)
#call
countdown(5)

#define merge
def merge(L,L1,L2):
    i=j=k=0
    while (j<len(L1)) or (k<len(L2)):
        if j<len(L1):
            if k<len(L2):
                #not at the end of L1 or L2, so pull the smaller value
                if L1[j] < L2[k]:
                    L[i]=L1[j]
                    j+=1
                else:
                    L[i]=L2[k]
                    k+=1
            else:
                #at the end of L2, so pull the smaller value from L1
                L[i]=L1[j]
                j+=1
        else:
            # at the end of L1, so pull the smaller value from L2
            L[i]=L2[k]
            k+=1
        i+=1
    return

#Merge sort - pull the smallest value from either L1 or L2, and put into L array
def mergeSort(L):
    n=len(L)
    if n<=1:
        return L
    #splitting point
    L1= L[:n//2] #using slicing operation to take a subset of the list; #integer division - drop a remainder
    L2= L[n//2:]

    mergeSort(L1)
    mergeSort(L2)
    merge(L,L1,L2)
    return

fave_foods = ['apples','pomegranates','cherries','salmon','potatoes','sushi']
mergeSort(fave_foods)
print(fave_foods)

#Quicksort
def quickSort(L):
    n=len(L)
    if n<=1:
        return L #a list of 1 is already sorted

    pivot=L[0]
    L1=[]
    L2 = []

    #form 2 lists
    for item in L[1:]: #except the first element that's alreay in pivot
        if item<pivot:
            L1.append(item)
        else:
            L2.append(item)

    #sort sublists
    quickSort(L1)
    quickSort(L2)

    #join the sublists and pivot
    L[:]=[] # delete elements already in L; have to modify elements in L
    for item in L1:
        L.append(item)
    L.append(pivot)
    for item in L2:
        L.append(item)

    return

fave_foods = ['apples','pomegranates','cherries','salmon','potatoes','sushi']
quickSort(fave_foods)
print(fave_foods)

#Asymptotic analysis - as input grows larger and larger.  what will happen if i double size?
#best case? worst case? or avg case?
#$ac insert 2 videos from iPad
