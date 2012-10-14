#fibonocci sequence whose values do not exceed four million,find the sum of even#valued terms
i=0
a=1
b=2
c=0
s=2
print a
print b
while(i<1000000):
  c=a+b
  a=b
  b=c
  if c<4000000:
    print c
    if c%2==0:
      s=s+c
  else:
    i=1000000
  i=i+1
print"sum of even numbers is",s

  
  
