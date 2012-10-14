#what is the 10001st prime number?


count=0
for i in range(2,20000):
  c=0
  for j in range(1,i+1):
    a=i%j
    if a==0:
      c=c+1
  if c==2:
    count=count+1
    if count==1001:
      print i
  
