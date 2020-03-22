msg = 'hello python'
print(msg)


###############################################
# calculate area and env 
r = input('enter r please : ')
r_int = float(r)
pi = 3.14

env =( r_int + r_int )* pi
area = r_int * r_int * pi
# here we print area and env
print (f'area : {area} , env : {env}')

###############################################
#if statement

name = 'mahmoud'

if name == 'mahmoud':
    print('name is ok')
else:
    print('WTF')    
    
#################################################### 
#while_loop

chuck = 20 

while (chuck > 0):
    print (f'i ate chuck number {chuck}')
    chuck = chuck - 1

#########################################################
#babylonian algorythm is real babe 
print('\nbabylonian example is RUN **** :')
error = 0.01

number = input ('Please Enter Your Guess Number : ')

number = float(number)
guess_number = number / 2 

while ( abs(number - guess_number**2) > error):
    print (f'==> my guess is {guess_number}')
    taghsim = number / guess_number
    guess_number = (taghsim + guess_number) / 2 

print (f'Your final Guess is {guess_number}')

###########################################################
# for loop 

name_list = ['mahmoud','sajjjad','mohsen','reza','ali',]

for name in name_list:
    print(name)

###########################################################
#breack continu

for char in 'Make it easy take it easy':
    if(char == ' '):
        continue
    print(char)
    
print('END')    

#########################################################
#nested loop
#check prime number 

number = 2 

while (number < 60):
    is_prime = True
    counter = 2
    while (counter < number - 1):
        if((number % counter)==0):
            is_prime = False
            break
        counter += 1            
    if(is_prime):
        print (number)
    number += 1

#######################################################
#prime number with for 


for number in range(2,51):
    prime = True
    for counter in range(2,number):
        if(number % counter == 0):
            prime = False
    if(prime):
        print(number)        

##########################################################
#functions 

#func define with def keyword in py

##########################################################
#String Encoding

#give me asci code
ord('a')
#give me char of each code
chr(97)


#############################################
#Advance python started 
# 1 - oop 
# 2 - database
# 3 - web scraping
# 4 - machine learning 
# 5 - project 
# 6 - working with api
##############################################
# 1 - oop :
############################################## 

#lambda functions ,filter ,map

myfunc = lambda x : x * 2 

myfunc(2)

a = [(1,2),(3,4),(6,1),(7,7)]

a.sort() # sort per first value 

a.sort(key = lambda x : x[1]) # sort per second value 

mylist = [1,4,7,9,0,6,5,3,2]

#member of list go to power 2

list(map(lambda x : x**2 , mylist ))

numbers = [10,23,41,1,5,66,230,21,55]

# new form of if else **********************
list(map(lambda x : 'big' if x>10 else 'small',numbers))

list(filter(lambda x : x%2 == 0,numbers))

# generator ,function ,yield

def firstn():
    yield 1
    yield 2
    yield '...'
    yield 100

for i in firstn():
    print(i)


def numConter(n):
    num = 0
    while (num<n):
        yield num
        num += 1

#gerator func just can use in iteration 
for i in numConter(100):
    print(i)
