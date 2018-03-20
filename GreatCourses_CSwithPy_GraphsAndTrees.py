"""
books referenced:
Lambert, Fundamentals of Python. ch. 10, 12

"""

#--Ch.22. Graphs and trees --
"""
Graphs offer a structure for capturing an incredibly wide diversity of relationships and 
the connections that are formed all over.  
i.e. connections between locations 

Vertex/node are represented entities. 
Edges - the connections between nodes.  
i.e. cities and roads.  

Codewise, graphs can have more than 1 representation. 
a)global 
b)focuses on adjacent neighbors 

# --Global - represent a graph as two lists: one list of nodes and one list of edges
Each node will contain information about itself. 
An edge would reference the two nodes.  
If it's a weighted graph, the edges will also store a weight. 
"""

"""
#2 classes

class node:
    def __init__(self, name, population=0):
        self._name = name
        self._pop = population

    #accessor functions
    def getName(self):
        return  self._name
    def getPopulation(self):
        return self._pop

class edge:
    def __init__(self, name1, name2, weight=0):
        self._city1 = name1
        self._city2 = name2
        self._distance = weight
    # accessor functions
    def getName1(self):
        return self._city1
    def getName2(self):
        return self._city2
    def getNames(self):
        return (self._city1, self._city2)
    def getWeight(self):
        return self._distance

#setup
cities=[]
roads=[]

city = node('Rivertown',100)
cities.append(city)
city = node('Brookside',1500)
cities.append(city)
city = node('Hillsview',500)
cities.append(city)
city = node('Forrest City',800)
cities.append(city)
city = node('Lakeside',1100)
cities.append(city)
#print(cities[0].getName())

road = edge('Rivertown', 'Brookside', 100)
roads.append(road)
road = edge('Rivertown','Hillsview', 50 )
roads.append(road)
road = edge('Hillsview','Brookside',130)
roads.append(road)
road = edge('Hillsview', 'Forrest City', 40)
roads.append(road)
road = edge('Forrest City','Lakeside', 80)
roads.append(road)

#using edges - i.e. find the total population that lives on a road
#need to find population of the cities on each end

road = roads[0]
pop1 = 0
pop2 = 0

for city in cities:
    if city.getName()==road.getName1():
        pop1 = city.getPopulation()
    if city.getName() == road.getName2():
        pop2 = city.getPopulation()
print (pop1 + pop2)
"""

"""
#note: O(n) operation just to get population - if a large list, this code won't work well
#use index of 2 cities instead of names 
#index makes it easier to find the cities, can jump right to the city
#don't even need to change the previously defined classes, but parameters in edge node are badly named
#=> redo

#2 classes

#same as before
class node:
    def __init__(self, name, population=0):
        self._name = name
        self._pop = population

    #accessor functions
    def getName(self):
        return  self._name
    def getPopulation(self):
        return self._pop
#change here
class edge:
    def __init__(self, idx1, idx2, weight=0):
        self._city1 = idx1
        self._city2 = idx2
        self._distance = weight
    # accessor functions
    def getIdx1(self):
        return self._city1
    def getIdx2(self):
        return self._city2
    def getIndices(self):
        return (self._city1, self._city2)
    def getWeight(self):
        return self._distance

#setup
cities=[] #same as before
roads=[]

city = node('Rivertown',100)
cities.append(city)
city = node('Brookside',1500)
cities.append(city)
city = node('Hillsview',500)
cities.append(city)
city = node('Forrest City',800)
cities.append(city)
city = node('Lakeside',1100)
cities.append(city)
#print(cities[0].getName())

#change here
road = edge(0, 1, 100)
roads.append(road)
road = edge(0, 2, 50 )
roads.append(road)
road = edge(2, 1, 130)
roads.append(road)
road = edge(2, 3, 40)
roads.append(road)
road = edge(3, 4, 80)
roads.append(road)

#way simpler code - have cities indices, can go directly to those cities, no need to loop
#this is a constant time operation, will take the same time regardless of how many things there're
#with linear it was - the more things we have, the longer it would take
road = roads[0]
pop1 = cities[road.getIdx1()].getPopulation()
pop2 = cities[road.getIdx2()].getPopulation()
print (pop1 + pop2)
#downside - the list of cities must remain unchanged.  must live with these restrictions
#indirection - using an index to refer to an item in a list instead of storing the actual name or value
"""

"""
Let's say want to take a city and find all the roads from to that city.
a painful operation in global approach - have to go thru the list of edges trying 
to find the edges that have our city as either first or second city in the edge.
Let's keep a local list of the edges for each node. 
Each node will keep track of all the edges connected to it. 

# --Adjaceny list - Keep a list of edges in each node. 
"""

"""
class node:
    def __init__(self, name, population=0):
        self._name = name
        self._pop = population
        self._roads = []

    # accessor functions
    def getName(self):
        return self._name
    def getPopulation(self):
        return self._pop

    def getRoads(self):
        return self._roads
    def addNeighborRoad(self,e):
        self._roads.append(e)
    def addNeighbor(self,city, weigth=0):
        e=edge(city, weigth)
        self._roads.append(e)

class edge:
    def __init__(self, city, weight=0):
        self._city = city
        self._weight = weight
    def getCity(self):
        return self._city
    def getWeight(self):
        return self._weight

#create cities, just like before
cities=[] #same as before

city = node('Rivertown',1000)
cities.append(city)
city = node('Brookside',1500)
cities.append(city)
city = node('Hillsview',500)
cities.append(city)
city = node('Forrest City',800)
cities.append(city)
city = node('Lakeside',1100)
cities.append(city)
#print(cities[0].getName())

#creating a road between 2 cities is more complicated
def addRoad(name1, name2, weight=0):
    e1=edge(name2, weight)
    e2=edge(name1, weight)
    for city in cities:
        if city.getName()==name1:
            city.addNeighborRoad(e1)
        if city.getName()==name2:
            city.addNeighborRoad(e2)

#alternative - using addNeighbor routine
def addRoad2(name1, name2, weight=0):
    for city in cities:
        if city.getName()==name1:
            city.addNeighbor(name2, weight)
        if city.getName()==name2:
            city.addNeighbor(name1, weight)

#adding connections - adding 5 roads
addRoad("Riverton", "Brookside", 100)
addRoad("Riverton", "Hillsview", 50)
addRoad("Brookside", "Hillsview", 130)
addRoad("Hillsview", "Forrest City", 40)
addRoad("Forrest City", "Lakeside", 80)

#find neighbors
for city in cities:
    print('Neighbors of '+city.getName())
    roads = city.getRoads()
    for road in roads:
        print ('    ', road.getCity(), 'at a distance ', road.getWeight())

#easier to find neihbors of a particular node; but more complex routines
#not well suited for finding every edge.  previous one was better.
"""

"""
#--Tree
structure of parent and children
usually an adjacency list
"""
class node:
    def __init__(self, name, parent=-1):
        self._name = name
        self._parent = parent
        self._children = []

    # accessor functions
    def getName(self):
        return self._name
    def getParent(self):
        return self._parent
    def getChildren(self):
        return self._children

    #setter functions
    def setParent(self, p):
        self._parent = p
    def addChildren(self, c):
        self._children.append(c)

"""
Binary Trees
Every node has no more than 2 children: a left and a right child 
So a node holds a paretn, a left child and a right child. 
"""

"""
class nodeBinary:
    def __init__(self, name, parent=-1):
        self._name = name
        self._parent = parent
        self._child_left = -1
        self._child_right = -1

    # accessor functions
    def getName(self):
        return self._name
    def getParent(self):
        return self._parent
    def getChildLeft(self):
        return self._child_left
    def getChildRight(self):
        return self._child_right

    #setter functions
    def setParent(self, p):
        self._parent = p
    def addChildLeft(self, lc):
        self._children.append(lc)
    def addChildRight(self, rc):
        self._children.append(rc)

#$ac insert code from video here
"""

#--Ch.23. Graph Search using BFS --
"""
breadth-first search
Searching thru a graph to connect a starting noe with another node can take one of two approaches: 
-follow edges as far as you can until u can go no further, or  
-gradually spread out from the starting point == BFS 

We have a social network where people form the nodes, and we have an edge connecting friends.  
we want to know the shortest way to connect two people thru a sequence of friends
"""

class node:
    def __init__(self, name):
        self._name = name
        self._friends = []
        self._status = 0 #designate as seen/unseen
        self._discoveredby = 0 #keep track which node discovred during the search

    # accessor functions
    def getName(self):
        return self._name
    def getFriends(self):
        return self._friends

    #setter functions
    def addFriend(self, friend_idx):
        self._friends.append(friend_idx)

    #handle seen/unseen
    def isUnseen(self):
        if self._status==0:
            return True
        else:
            return False
    def isSeen(self):
        if self._status==1:
            return True
        else:
            return False
    # setter functions
    def setUnseen(self):
        self._status=0
    def setSeen(self):
        self._status=1

    #handle discovery
    def discover(self,n):
        self._discoveredby = n
    def discovered(self):
        return self._discoveredby


#people =[] will be set later
def makeFriends(name1, name2):
    for i in range(len(people)):
        if people[i].getName()==name1:
            n1=i
        if people[i].getName()==name2:
            n2=i

    people[n1].addFriend(n2)
    people[n2].addFriend(n1)

#now write function to do the search for us
class Queue():
    def __init__(self):
        self._queue = []
    def enqueue(self,item):
        self._queue.append(item)
    def dequeue(self):
        return self._queue.pop(0)
    def isEmpty(self):
        return len(self._queue)==0

def retrievePath(nodelist,start,goal):
    # return the path from start to goal, using recursion
    if start==goal:
        path=[]
        path.append(start)
        return path
    else:
        previous=nodelist[goal].discovered()
        previous_path=retrievePath(nodelist,start,previous)
        previous_path.append(goal)
        return previous_path

#Bacon number
def BFS(nodelist,start,goal):
    to_visit=Queue()
    nodelist[start].setSeen()
    to_visit.enqueue(start)
    print('start',start)
    print(to_visit.isEmpty())

    found=False
    while(not found) and (not to_visit.isEmpty()):
        current=to_visit.dequeue()
        #print(current)
        neighbors = nodelist[current].getFriends()
        for neighbor in neighbors:
            if nodelist[neighbor].isUnseen():
                nodelist[neighbor].setSeen()
                nodelist[neighbor].discover(current)
                if neighbor == goal:
                    found = True
                else:
                    to_visit.enqueue(neighbor)

    return retrievePath(nodelist,start,goal)

people =[]
person=node('John')
people.append(person)
person=node('Joe')
people.append(person)
person=node('Sue')
people.append(person)
person=node('Fred')
people.append(person)
person=node('Kathy')
people.append(person)

makeFriends('John','Joe')
makeFriends('John','Sue')
makeFriends('Joe','Sue')
makeFriends('Sue','Fred')
makeFriends('Fred','Kathy')

pathlist=BFS(people,0,4)
for idx in pathlist:
    print (people[idx].getName())