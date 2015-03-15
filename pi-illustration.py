from turtle import*
reset()
 
def move(digit,d):
    if digit!=0:
        left((digit-1)*45)      
        forward(d)
    return
 
pencolor('white')
sety(150)
pencolor('black')
speed(0)
width(1)
 
fd = open('pi10k.txt','rU')
pi_digits = [3]
for line in fd:
   for c in line:
       d=int(c)
       pi_digits.append(d)
       
for member in pi_digits:
    move(member,5)