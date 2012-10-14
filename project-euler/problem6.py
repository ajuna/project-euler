#find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

import math
i=1
s=0
p=0
n=0
m=0
while(i<101):
  p=pow(i,2)
  s=s+p
  i=i+1
print "Sum of squares of 1 to 100 numbers:",s
m=sum(range(1,101))
n=pow(m,2)
print "Square of sum of 1 to 100 numbers:",n
print "difference is:" ,n-s


