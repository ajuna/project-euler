# What is the value of the triangle number to have over 90 divisors

p=0
for i in range(1,225):
  c=[]
  s=sum(range(1,i+1))
  j=1
  while(j<=s):
    if s%j==0:
      c.append(j)
    j=j+1
  print s,c
  
 
  
    
  
  
    
  
  
    
  
