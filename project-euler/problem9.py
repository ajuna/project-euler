#there exists exactly one Pythagorean triplet for which a+b+c=1000. find the product abc


for a in range(1,1000):
  for b in range(a,1000):
     c=1000-a-b
     if c*c==(a*a)+(b*b):
        print a
        print b
        print c
        print "product of abc is",a*b*c
