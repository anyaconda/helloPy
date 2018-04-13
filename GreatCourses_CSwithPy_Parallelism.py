"""
books referenced:
Lambert, Fundamentals of Python. ch. 10, 12

"""

#--Ch.24. Parallel Processing --
from multiprocessing import Process

"""

#Hello World multiprocessed
def print_function():
    print('Hello World!')

if __name__ == '__main__':
    p=Process(target=print_function())
    p.start()
"""
#modified
def print_function(name):
    print('Hello ', name)

if __name__ == '__main__':
    p=Process(target=print_function, args=("John",)) #arguments passed to a fn by using 'args'
    #comma is used because 'args' expects at least 2 params passed,
    # bcs args list turns into a tuple, which makes it non-mutable.
    # a tuple of one is not possible. by adding , gives an appearance of two args to work with.
    p.start()

#example
def print_process(number):
    print('Printing from process ', number)

if __name__ == '__main__':
    process_list=[]
    for i in range(20):
        p=Process(target=print_process, args=(i,))
        process_list.append(p)

    for p in process_list:
        p.start()
