#what is the first term in the Fibonacci sequence to contain 1000 digits?

a=1
b=1
c=0
i=0
s=0
count=0
z=2
while(count<1):
    c=a+b
    a=b
    b=c
    z=z+1
    if len(str(c))==1000:
      print"the term is",z
      count=count+1
    



  
  
  
