#what is largest prime factor of the number 600851475143

n=600851475143
i=2
list=[]
while(i<=n):
  if n%i==0:
    list.append(i)
    n=n/i
  i=i+1
print "largest prime factor is",max(list)


