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

