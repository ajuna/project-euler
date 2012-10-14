#using following rule generate sequence
#n->n/2(n is even)   n->3n+1(n is odd)

print "Enter a number"
n=input()
c=[]
i=n
c.append(n)
while(i>1):
  if n%2==0:
    n=n/2
    c.append(n)
  else:
    if n==1:
      i=1
    else:
      n=(3*n)+1
      c.append(n)
  i=n
print c
      
