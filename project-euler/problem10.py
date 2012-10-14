# find the sum of all the primes below thousand

s=0
for i in range(2,10000):
  c=0
  for j in range(1,i+1):
    a=i%j
    if a==0:
      c=c+1
  if c==2:
    s=s+i 
print s

