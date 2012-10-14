#find all sum of multiples of 3 or 5 below 1000

i=0
n=0;m=0;s=0
while(i<350):
  a=i*3
  b=i*5
  if a<1000:
    m=m+a
  if b<1000:
    n=n+b
  i=i+1
s=m+n
print s

   




