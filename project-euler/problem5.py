#Evaluate the sum of all amicable numbers under 10000

x=0
for i in range(1,10000):
  s=0
  c=[]
  for j in range(1,i):
    if i%j==0:
      c.append(j)
      s=s+j
  d=[]
  z=0
  for k in range(1,s):
    if s%k==0:
      d.append(k)
      z=z+k
  if i==z and i!=s:
    print i,s
    x=x+i
print"Sum of all amicable number: ",x
  

  
  
      
      
  

