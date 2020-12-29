# -*- coding: utf-8 -*-
# @Time : 2020/10/9 2:25
# @公众号 :Python自动化办公社区
# @File : 贪吃蛇代码.py
# @Software: PyCharm
# @Description:关注公众号，后台回复 “0816”，加入Python学习交流群（长期有效）


#1、首先打开terminal
#2、输入：pip install pygame，回车
#3、右键，选择run

import random
import pygame
import sys
from pygame.locals import *

windows_width=800 #游戏窗口的大小，原点在左上角
windows_height=600

cell_size=20  #snake 的大小，需被窗口长宽整除

#一些颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
gray = (230, 230, 230)
dark_gray = (40, 40, 40)
DARKGreen = (0, 155, 0)
Green = (0, 255, 0)
Red = (255, 0, 0)
blue = (0, 0, 255)
dark_blue =(0,0, 139)

BG_COLOR = (184,224,217)

#贪吃蛇的地图尺寸
map_width = int(windows_width / cell_size)
map_height = int(windows_height / cell_size)

#蛇的移动速度
snake_speed=5

#方向定义
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

#主函数
def main_game():
  pygame.init() #初始化gygame
  screen=pygame.display.set_mode((windows_width,windows_height))
  pygame.display.set_caption("Snake GO")
  snake_speed_clock = pygame.time.Clock() # 创建Pygame时钟对象
  screen.fill(white)

  while True:
    run_game(screen,snake_speed_clock) #游戏主体
    gameover(screen)        #游戏结束


def run_game(screen,snake_speed_clock):
  #初始化蛇的位置，方向，食物的位置
  start_x=random.randint(3,map_width-8)
  start_y=random.randint(3,map_width-8)
  snake_coords=[{'x':start_x,'y':start_y},{'x':start_x-1,'y':start_y},{'x':start_x-2,'y':start_y}]#初始化snake，也可以用列表的的列表
  direction = RIGHT
  food=get_random_location()

  #循环
  while True:
    for event in pygame.event.get(): #键盘事件监听
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN: #按键事件
        if (event.key==K_LEFT or event.key==K_a) and direction!=RIGHT:
          direction=LEFT
        elif (event.key==K_RIGHT or event.key==K_d) and direction!=LEFT:
          direction=RIGHT
        elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
          direction = UP
        elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
          direction = DOWN
        elif event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()

    snake_move(direction,snake_coords) #根据方向，移动蛇

    alive=snake_is_alive(snake_coords)  #判断蛇的死活
    if not alive:            #如果挂了，则终止循环，跳出run_game函数，执行gameover
      break
    snake_eat_foods(snake_coords,food)  #没挂，则看看迟到食物了吗
    screen.fill(BG_COLOR)        #游戏背景刷新

    #下面draw，是把蛇食物等画出来
    draw_snake(screen, snake_coords)
    draw_food(screen,food)
    draw_score(screen, len(snake_coords) - 3)
    # draw_grid(screen)
    pygame.display.flip()

    #控制执行次数
    snake_speed_clock.tick(snake_speed) # 控制fps


#根据移动方向，更新蛇头坐标
def snake_move(directtion,snake_coords):
  if directtion==UP:
    newHead={'x':snake_coords[0]['x'],'y':snake_coords[0]['y']-1}
  elif directtion==DOWN:
    newHead = {'x': snake_coords[0]['x'], 'y': snake_coords[0]['y'] + 1}
  elif directtion==LEFT:
    newHead = {'x': snake_coords[0]['x']-1, 'y': snake_coords[0]['y'] }
  elif directtion == RIGHT:
    newHead = {'x': snake_coords[0]['x']+1, 'y': snake_coords[0]['y']}
  snake_coords.insert(0,newHead)

def snake_is_alive(snake_coords): #碰壁或者碰到自身就是死了
  alive=True
  if snake_coords[0]['x'] == -1 or snake_coords[0]['x'] == map_width or snake_coords[0]['y'] == -1 or \
  snake_coords[0]['y'] == map_height:
    alive=False
  for snake_body in snake_coords[1:]:
    if snake_coords[0]['x']==snake_body['x'] and snake_coords[0]['y']==snake_body['y']:
      alive=False
  return alive

#坐标重合，表示吃到食物了，否则就没有，则移动，把
def snake_eat_foods(snake_coords,food):
  if snake_coords[0]['x']==food['x'] and snake_coords[0]['y']==food['y']:
    food['x']=random.randint(0, map_width-1)
    food['y']=random.randint(0, map_height-1)
  else:
    del snake_coords[-1]

def get_random_location(): #食物的坐标随机生成
  return {'x':random.randint(0,map_width-1),'y':random.randint(0,map_height-1)}

def draw_snake(screen, snake_coords):
  for coord in snake_coords:
    x=coord['x']*cell_size
    y=coord['y']*cell_size
    segmentRect=pygame.Rect(x,y,cell_size,cell_size)
    pygame.draw.rect(screen,dark_blue,segmentRect)

def draw_food(screen,food):
  x=food['x']*cell_size
  y=food['y']*cell_size

  foodRect=pygame.Rect(x,y,cell_size,cell_size)
  pygame.draw.rect(screen,Red,foodRect)

def draw_grid(screen):
  for x in range(0,windows_width,cell_size):
    pygame.draw.line(screen,gray,(x,0),(x,windows_height))
  for y in range(0,windows_height,cell_size):
    pygame.draw.line(screen,gray,(0,y),(windows_width,y))
def draw_score(screen, score):
  font = pygame.font.SysFont(None, 40)
  score_str = "{:,}".format(score)
  score_image=font.render('Score: '+score_str,True,Green,gray)
  score_rect=score_image.get_rect()

  score_rect.topleft=(windows_width-200,10)
  screen.blit(score_image, score_rect)

def gameover(screen):
  font=pygame.font.SysFont(None, 40)
  tips=font.render('Press Q or ESC to quit; Press anykey to continue',True, (65, 105, 225))
  screen.blit(tips,(80, 300))
  pygame.display.update()
  while True:
    for event in pygame.event.get():
      if event.type==QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == KEYDOWN:
        if event.key == K_ESCAPE or event.key == K_q: # 终止程序
          pygame.quit()
          sys.exit() # 终止程序
        else:
          return # 结束此函数, 重新开始游戏

if __name__=='__main__':
  main_game()