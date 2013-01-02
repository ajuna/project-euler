import pygame,sys
from pygame.locals import *

#initialise screeen
pygame.init()
screen=pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption("Conway's Game of Life")
screen.fill((192,192,192))

#drawing drid
j=0
while j<500:
  i=0
  while i<500:
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(j,i,20,20))
    i=i+22
  j=j+22

#drawing black cell
pixObj=pygame.PixelArray(screen)
pixObj[132:152,88:108]=(0,0,0)
pixObj[154:174,88:108]=(0,0,0)
pixObj[176:196,88:108]=(0,0,0)
pixObj[110:130,110:130]=(0,0,0)
pixObj[132:152,110:130]=(0,0,0)
pixObj[154:174,110:130]=(0,0,0)

m=44
while m<90:
  n=44
  while n<90:
    pixObj[m:m+20,n:n+20]=(0,0,0)
    n=n+22
  m=m+22

#checking neighbours
while 1:
  c=10
  while c<400:
    r=10
    while r<400:
      count=0
      if pixObj[c,r-22]==screen.map_rgb(0,0,0):
        count=count+1
      if pixObj[c,r+22]==screen.map_rgb(0,0,0):
        count +=1
      if pixObj[c-22,r-22]==screen.map_rgb(0,0,0):
        count +=1
      if pixObj[c-22,r]==screen.map_rgb(0,0,0):
        count+=1
      if pixObj[c-22,r+22]==screen.map_rgb(0,0,0):
        count+=1
      if pixObj[c+22,r-22]==screen.map_rgb(0,0,0):
        count+=1
      if pixObj[c+22,r]==screen.map_rgb(0,0,0):
        count+=1
      if pixObj[c+22,r+22]==screen.map_rgb(0,0,0):
        count+=1
      #conditions
      if pixObj[c,r]==screen.map_rgb(0,0,0):
        if count<2 or count>3:
          pixObj[c-10:c+10,r-10:r+10]=(255,255,255)
        else:
          pixObj[c-10:c+10,r-10:r+10]=(0,0,0)
      if pixObj[c,r]==screen.map_rgb(255,255,255):
        if count==3:
          pixObj[c-10:c+10,r-10:r+10]=(0,0,0)
     
      pygame.display.update()
      r+=22
    c+=22
    for event in pygame.event.get():
		if event.type==QUIT:			
			pygame.quit()
			sys.exit()
	        pygame.display.update()
			




