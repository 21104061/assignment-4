#question 1
print("Question 1")

def Towerofhanoi( n, startpoint, endpoint, extrapoint ): # it defines a function
    if n > 0:
        Towerofhanoi( n-1, startpoint, endpoint, extrapoint)
        print("tranfer disk from", startpoint, 'to', endpoint)
        Towerofhanoi( n-1 , extrapoint, startpoint, endpoint)

Towerofhanoi(3, 'A', 'B', 'C')
print('Done!!')
print()


#question 2
print("Question 2")
print("Pascal Triangle Maker")
print()

print("With Interations: ")

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
#to maker ncr
def ncr(n,r):
    x=factorial(n)/(factorial(n-r)*factorial(r))
    return int(x)

#to make rows
row = int(input("Enter the number of rows: "))
i=1
while i<=row:
    print(" "*(row-i),end="")
    j=0
    while j<i:
        print(ncr(i-1,j)," ",end="")
        j+=1
    print("\n")
    i+=1

print()
print("With recursion:")
def pt(n,s,m):
    if n==0:
        print(" "*(s-1),1,"\n")
        return pt(n+1,s,m)
    elif n==m:
        print("Done!")
        n=-1
    else:
        print(" "*(s-n),end="")
        x=0
        while x<=n:
            print(ncr(n,x),"",end="")
            x+=1
        print("\n")
        if n==m:
            n=-2
        return pt(n+1,s,m)
    
        
m=int(input("Enter the no. of rows:"))
n=m-m
s=m+m
pt(n,s,m)
print("Done")                 
print()
           
#Question 3
print("Question 3")
print()
int1, int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = int1 // int2
Remainder = int1 % int2

print()

print("3(a)")
print("Checking if the quotient and remainder is a callable value or not...")
print(callable(Quotient))
print(callable(Remainder))

print()
print("3(b)")
if (Quotient == 0):
    print(" The quotient is zero")
if (Remainder == 0):
    print("The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("All the values are non zero")

print()
print("3(c)")

partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f" Filtered out numbers that are greater than 4 are : {result}")

print()
print("3(d)")
setresult = set(result)
print("Set: ",setresult)

print()
print("3(e)")
immutableSet = frozenset(setresult) 
print("Immutable set: ",immutableSet)

print()
print("3(f)")
print("Hash value of the max value from the above set: ", hash(max(immutableSet)))
print("Done")
print()

#Question 4
print("Question 4")
print()
class Student:
    def __init__(self,name,rollnumber):
        self.name=name
        self.rollnumber=rollnumber
    def __del__(self):
        print("Object has been destroyed")

obj_1=Student("Tanveer Singh",21104061)
print(obj_1.name)
print(obj_1.rollnumber)
print("Done")
print()

#question 5
print("Question 5")
print()

class EmployeeDetails:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def func(self):
        print("Name of employee is:", self.name,"and salary is:",self.salary)

Emp_1 = EmployeeDetails("Mehak",40000)
Emp_2 = EmployeeDetails("Ashok",50000)
Emp_3 = EmployeeDetails("Viren",60000)
Emp_1.func()
Emp_2.func()
Emp_3.func()

print()
print("5(a)")
Emp_1.salary=70000
print("The updated salary of Mehak is: ",Emp_1.salary)

print()
print("5(b)")
del Emp_3
print("The record of Viren has been successfully deleted")
print("Done")
print()

print("Qusetion 6")
print()

def anagram(word):
    if len(word)==1:
        return [word];
    partial_words=anagram(word[1:])
    char=word[0]
    mylist=[]
    for perm in partial_words:
        for i in range(len(perm)+1):
            mylist.append(perm[:i]+char+perm[i:])
    return mylist       


George_word=input("Enter the word by George:")
Possible_words=anagram(George_word)
Barbie_word=input("Enter word by Barbie:")
print("Possible Words are:",Possible_words)
print("If Barbie's word is present in the list , then their friendship is real.")

if Barbie_word in Possible_words:
    print("Your Friendship is real.")
else:
    print("Your Friendship is fake.")
print("Done")