# coding: utf-8
"""
Python Data Structures
my notes
"""

import numpy as np
print ('--- Python Data Structures ---')
#  --  python data type List --
print('\n*** data type List ***')
items = []

items.append("apple")
items.append("orange")
items.append("banana")

print ("Type: ", type(items))
print ("Size: ", len(items))
print (items)
print (items[0])


# working with Data Structures
# Comprehensions
# very elegant

#Index based select
l_predict_multi=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx=[2,7,3,7]
#use Comprehensions to select
# how to read: from the list 'l', give me an items with index 'x' for each 'x' in index 'idx'
l1=[l_predict_multi[x] for x in idx]
print ('Use Comprehensions: ', l1)


n=len(l_predict_multi)
idx=np.arange(5,n)
#use Comprehensions to select
l2=[l_predict_multi[x] for x in idx]
print ('Use Comprehensions: ', l2)
#easier
print ('Here better without Comprehensions: ', l_predict_multi[5:])

#  --  python data type Dictionary --
print('\n*** data type Dict *** \nTBD')

#  --  from List to Dict --
print('\n*** from List to Dict ***')
print('src: creating REST API for SD Visibility')

l_names=['Tier','Category']
l1 = ['Tier0','Tier0']
l2 = ['Cat1','Cat2']

"""
create a json of prediction items, each item predicts Tier and Category
manually
"""
#init list
l_predict_multi=[]
#creaete list
for i,j in zip(l1,l2):
    #print("Tier:{}, Category:{}".format("'"+i+"'","'"+j+"'"))
    item={'Tier': i, 'Category': j}
    l_predict_multi.append(item)
print(l_predict_multi)

"""
create a json of prediction items, each item predicts only Category
with a function
"""
#define function: create a list of dict items
#input: key and a list of items
#output: list of items of type Dict
def fromList2ListOfDict(k,v):
    # create a list of dict items
    this_list = []
    for i in v:
        this_list.append({k: i})
    return this_list

#init list
l_predict_uni=[]
#creaete list
l_predict_uni=fromList2ListOfDict('Category',l2)
print(l_predict_uni)




"""
#not
print ("don't do this: ")
d2 = dict(('Tier',i) for i in l1)
print (d2)

#yes
print ("do this: create a list of dict items ")
l=[]
for i in l1:
    l.append({'Tier': i})
print(l)

#not
print ("don't do this: assigns a constant to 2 diff cats ")
d2 = dict((k,2) for k in l_names)
print ("d2:", d2)

print ("don't do this: doen't map between 2 diff cats and a list of items in 1 cat ")
for k, v in zip(l_names,l2):
    print("k and v:", k,v)
"""
