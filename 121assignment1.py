#cyclic rotation
#input elements of list
a_input=input("Enter a list of numbers (each seperated with a space): ")
#put elements into list
a=[int(x) for x in a_input.split()]
#input num of times list will be shifted right
k=int(input("Enter the number of elements the list will be shifted: "))

#define function
def solution(a,k):
    #loop for each shift
    for i in range(k):
        #remove last element from list
        last=a.pop()
        #insert last element to the front
        a.insert(0,last)
    #display shifted list
    print(a)

#call function
solution(a,k)

#frog jump
#import
import math
#input first number
start=int(input("Enter your starting number: "))
#input last number
end=int(input("Enter your end number: "))
#input jump value
jump=int(input("Enter the number you'd like to jump by: "))

#define function
def solution(x,y,d):
    #find the gap between first and last numbers
    diff=y-x
    #calculate the number of steps
    steps=diff/d
    #round the number of steps
    steps=math.ceil(steps)
    #display the number of steps
    print(steps)

#call function
solution(start,end,jump)

#perm missing elem
#input elements for list
a_input=input("Enter a list of numbers (each seperated with a space): ")
#create list with elements
a=[int(x) for x in a_input.split()]

#define function
def solution(a):
    #put list into a set
    seen=set(a)
    #check if each value is in the set
    for i in range(1,len(a)+2):
        #display value if not in set
        if i not in seen:
            print(i)
#call function
solution(a)

#missing integer
#enter elements for list
a_input=input("Enter a list of numbers (each seperated with a space): ")
#make list of elements
a=[int(x) for x in a_input.split()]

#define function
def solution(a):
    #put list in a set
    seen=set(a)
    #initalize i as 1
    i=1
    #check all values to see if they're in the set
    while i in seen:
        i+=1
    #print first value not in the set
    print(i)

#call function
solution(a)

#permutation check
#input elements for list
a_input=input("Enter a list of numbers (each seperated with a space): ")
#make list of elements
a=[int(x) for x in a_input.split()]

#define function
def solution(a):
    #put list in a set
    seen=set(a)
    #check values to see if they're in the set
    for i in range(1,len(a)+1):
        #if a value needed for permutation isnt in the set, display 0
        if i not in seen:
            print(0)
            break
    #otherwise display 1
    else:
        print(1)

#call function
solution(a)
