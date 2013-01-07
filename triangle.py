import pygame,sys
from pygame.locals import*

pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Sierpinski triangle")
screen.fill((192,192,192))
while 1:
 a=240
 h=120*pow(3,.5)

 (x1,y1)=(0,a)
 (x2,y2)=(a,a)
 (x3,y3)=(a/2,a-h)
 def triangle_main():
	pygame.draw.polygon(screen,(0,0,0),((x1,y1),(x2,y2),(x3,y3)))
	pygame.display.update()
 triangle_main()
 clock=pygame.time.Clock()
 clock.tick(1)

 def fun_1(cord1,cord2,cord3):
	pygame.draw.polygon(screen,(255,255,255),(cord1,cord2,cord3))
	pygame.display.update()
	

 def comp(c1,c2):
	m=(c1[0]+c2[0])*.5
	if c1[1]==c2[1]:
		n=c1[1]
	else:
		n=c1[1]-h
	return(m,n)
 h=h/2
 c1=comp((x1,y1),(x2,y2))
 c2=comp((x1,y1),(x3,y3))
 c3=comp((x2,y2),(x3,y3))

 fun_1(c1,c2,c3)
 clock.tick(1)
 h=h/2
 c4=comp((x1,y1),c1)
 c5=comp((x1,y1),c2)
 c6=comp(c1,c2)
 c7=comp(c1,c3)
 c8=comp((x2,y2),c3)
 c9=comp((x2,y2),c1)

 c10=comp(c2,c3)

 c11=comp(c3,(x3,y3))
 c12=comp(c2,(x3,y3))
 fun_1(c4,c5,c6)
 fun_1(c7,c8,c9)
 fun_1(c10,c11,c12)
 clock.tick(1)	

 for event in pygame.event.get():
	if event.type==QUIT:
		pygame.quit()
		sys.exit()
	pygame.display.update()
		
		
