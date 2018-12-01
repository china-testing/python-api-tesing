#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 技术支持：https://www.jianshu.com/u/69f40328d4f0 
# 技术支持 https://china-testing.github.io/
# https://github.com/china-testing/python-api-tesing/blob/master/practices/pygame_house.py
# 项目实战讨论QQ群630011153 144081101
# CreateDate: 2018-12-01
import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))

#used http://colorpicker.com/ to find RGB colors

def draw_tree(x,y):
	#tree trunk (50 wide and 100 tall)
	pygame.draw.rect(screen,(117,90,0),(x,y-100,50,100))
	#leaves are a circle
	pygame.draw.circle(screen,(27,117,0),(x+25,y-120),50)

def draw_house(x,y):
	#pink house
	pygame.draw.rect(screen,(255,171,244),(x,y-180,200,180))
	#brown door
	pygame.draw.rect(screen,(89,71,0),(x+80,y-60,40,60))
	#yellow door knob
	pygame.draw.circle(screen,(255,204,0),(x+112,y-30),4)
	#triangle roof
	pygame.draw.polygon(screen, (125,125,125), ( (x,y-180),(x+100,y-250),(x+200,y-180) ) )
	draw_window(x+20,y-90)
	draw_window(x+130,y-90)

def draw_window(x,y):
	#glass
	pygame.draw.rect(screen,(207,229,255),(x,y-50,50,50))
	#frame
	pygame.draw.rect(screen,(0,0,0),(x,y-50,50,50),5)
	pygame.draw.rect(screen,(0,0,0),(x+23,y-50,5,50))
	pygame.draw.rect(screen,(0,0,0),(x,y-27,50,5))

#this function is able to draw clouds of different sizes
def draw_cloud(x,y,size):
	#put int() around any multiplications by decimals to get rid of this warning:
	#DeprecationWarning: integer argument expected, got float
	pygame.draw.circle(screen,(255,255,255),(x,y),int(size*.5))
	pygame.draw.circle(screen,(255,255,255),(int(x+size*.5),y),int(size*.6))
	pygame.draw.circle(screen,(255,255,255),(x+size,int(y-size*.1)),int(size*.4))


#green ground
pygame.draw.rect(screen,(0,160,3),(0,400,640,80))
#light blue sky
pygame.draw.rect(screen,(135,255,255),(0,0,640,400))

draw_tree(60,400) #x and y location are the bottom left of tree trunk
draw_tree(550,400)

draw_house(225,400)

draw_cloud(60,120,80)
draw_cloud(200,50,40)
draw_cloud(450,100,120)


pygame.display.flip()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
pygame.quit()