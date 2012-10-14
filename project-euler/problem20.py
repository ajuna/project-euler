#find the sum of the digits in the number 100!

n=100
s=1
a=0
b=0
while(n>0):
  s=s*n
  n=n-1
while(s>0):
  a=s%10
  b=b+a
  s=s/10
print "sum of the digits in 100!=",b
