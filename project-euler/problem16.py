# What is the sum of the digits of the number 2^1000

n=pow(2,1000)
print n
i=0
b=0
a=0
while(n>0):
  a=n%10
  b=a+b
  n=n/10
print b
  

