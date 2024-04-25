# 1.  sum of two numbers


'''def sum(a,b):
  return print( a+b)
sum(1,2)'''

# 2. increment the one number
'''
num=int(input("enter number"))
print(num,"is your nuber")
def increment(num):
      return print( num+1,'answer')
increment(num) '''

# 3. return the remindar of two paramters with function



'''def reminder(num1,num2):
    return print(num1%num2)
reminder(7,2)'''

# 4. find the largest number in the list


'''my_list=[21,21,2332,1000000,100000000,2000000,30000000000000,0,324,1234,324,23,234,1423]
my_list.sort()
print(my_list)
print(my_list[-1])'''

# for smallest number ...index should be[0]  same code
'''a='sdafb'
b='aefhwrfjf'
b=list(a)
print(b)
b.sort()            
for i in b:
     print(i,end='' )  ''' # end method take word in string show in one line 

#5. two arg of string  add it in list and remove dublicate

'''a='ajdfhwjnfv'
b='biwufsch'
def sorting(a,b):
    print(sorted(set(a+b)))   # answer in list and remove dublicate


    # c.sort()
    
    # for i in c:
         
    #  print(i,end="")  #answer in string 
         
sorting(list(a),list(b))'''

# example
'''
a1=[12,132,35,54,62,12,12]
a2=[12,3124,123,13,4]
print(sorted(set(a1+a2)))'''

# 6. make a class that give us area and perimeter of circle
'''class circle:
    def __init__(self,r):
        self.r=r

    def getperimeter(self):
        print(self.r*3.141*2 )

    def getArea(self):
        print(3.141*self.r**2)     

circle=circle(11)
circle.getArea()  '''          
        
 # 7. print werid or not
'''n=int(input('enter number '))
if (n%2)!=0:    # odd number is weired
    print('weird')
if (n%2)==0:
    if n>20:
        print('lat werid')
    if n>5 and n<=20:
        print( 'w')
    if n<=5:
        print('not weird')'''
 
# 8.     The provided code stub reads and integer,n , from input. For all non-negative integers i<n , print i square

             #range (n)  means value given by user
                        #    loop cannot iletrat on integer value
'''n=int(input('enter number '))
for i in range(n):         
   print(i*i)
'''
# 9.   program checking a year is leap year or not ...    
'''
def is_leap(year):   
    if year%4==0:
       print("leap year")
       if year%100==0:
           if year%400==0:
               print('leap year')
           else:
              print('not a leap year')             
    
           
    return leap

year = int(input())
print(is_leap(year))'''

#  second method to check leap year ony if condition
'''year= int(input('enter year'))

if (year%400==0) and (year%100==0):
    print('leap year')
elif (year%4==0) and (year%100!=0):
    print('leap year')
else:
    print('not a leap year')   '''     





# 10.  Print the list of integers from  through n as a string, without spaces exm.. input 3 print 123 
'''n=int(input('enter number '))
c=[]
for i in range(1,n+1):
    
   c.append(str(i))

print(''.join(c))
print(c)'''

#.11 input number than add it in list

'''
n = input()
list=[]
# list.extend(n)
for i in n:
   a=int(i)
   list.extend(a)
print(a)'''

# 12 find the squr root of any number like the sqr of 49 is 7.

'''n =int(input())

sqr=n**(1/2)
print(sqr)'''
#  using  math module for square root
'''import math
n =int(input())
sr=math.sqrt(n)
print(sr)
'''

#.13 swap two number

# method 1 with temporay varriable
'''a=12
b=13
tem=a
a=b
b=tem
print(a,b)'''
#  second method
'''a=14
b=15
a,b=b,a
print(a,b)'''

#.14  check number is positive ,negative or 0
'''a=-12

if(a>0):
    print( 'positve nuber')
elif a==0:
    print('number is zero')
else:
    print('number is negative')   '''     

#.15  check a number is a prime number or not

'''num=int(input('number '))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print('not a prime')
            break
    else:
      print(' prime')  '''    

#.16  generate a random number 


'''import random

num =random.randint(0,12)
print(num)'''

#.17  print all prime number  of range()

'''lower=int(input())
upper=int(input())

for num in range(lower,upper+1):
    if num >1:
        for i in range(2,num):
            if num%i==0:
                break                 
        else:
            print(num)   '''
