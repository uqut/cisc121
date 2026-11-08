#cyclic rotation
a_input=input("Enter a list of numbers (each seperated with a space): ")
a=[int(x) for x in a_input.split()]
k=int(input("Enter the number of elements the list will be shifted: "))

def solution(a,k):
    a_shifted=a[-k:]+a[:-k]
    print(a_shifted)
    
solution(a,k)

#frog jump
import math
start=int(input("Enter your starting number: "))
end=int(input("Enter your end number: "))
jump=int(input("Enter the number you'd like to jump by: "))

def solution(x,y,d):
    diff=y-x
    steps=diff/d
    steps=math.ceil(steps)
    print(steps)

solution(start,end,jump)

#perm missing elem
a_input=input("Enter a list of numbers (each seperated with a space): ")
a=[int(x) for x in a_input.split()]

def solution(a):
    seen=set(a)
    for i in range(1,len(a)+2):
        if i not in seen:
            print(i)

solution(a)

#missing integer
a_input=input("Enter a list of numbers (each seperated with a space): ")
a=[int(x) for x in a_input.split()]

def solution(a):
    seen=set(a)
    i=1
    while i in seen:
        i+=1
    print(i)

solution(a)

#permutation check
a_input=input("Enter a list of numbers (each seperated with a space): ")
a=[int(x) for x in a_input.split()]

def solution(a):
    seen=set(a)
    for i in range(1,len(a)+1):
        if i not in seen:
            print(0)
            break
    else:
        print(1)
        
solution(a)