import tkinter as tk
from PIL import Image,ImageTk
from time import time,sleep
from random import choice,uniform,randint
from math import sin,cos,radians
#重力变量
GRAVITY=0.5
#listof colors,can choose randomly or use as queue(FIFO
colors=['red','blue','yellow','white','green','orange','purple','seagreen','indigo','cornflowerblue']
'''
create a class for particles粒子
particles are emitted almost randomly on the sky,
forming around(组成一个圈) of circle(a star)before falling and getting removed from canvas

Attributes(属性)：
id:每个特定烟花的标识符
x，y：烟花的绽放坐标
vx,vy:烟花的绽放速度
total:一颗烟花里的星星总数
age:一颗星星会在画布上停留多久
color:自我移植
cv:画布
lifespan:星星在画布上停留的最后时间
'''
class part:#为每一个烟花绽放出来的粒子单独构建一个类的对象
  def __init__(self,cv,idx,total,explosion_speed,x=0.,y=0.,vx=0.,vy=0.,size=2.,color='red',lifespan=2,**kwargs):
    self.id=idx#每个烟花的特定标识符
    self.x=x#烟花的绽放x轴
    self.y=y#烟花的绽放x轴
    self.initial_speed=explosion_speed#初速度
    self.vx=vx#外放x轴速度
    self.vy=vy#外放y轴速度
    self.total=total#绽放的粒子数
    self.age=0#已停留时间
    self.color=color#颜色
    self.cv=cv#画布
    self.cid=self.cv.create_oval(x-size,y-size,x+size,y+size,fill=self.color)#create_oval()创建一个椭圆，参数为左上x，左上y，右下x，右下y，填满的颜色，该函数返回一个id
    self.lifespan=lifespan#应该停留时间
  def update(self,dt):#更新数据，已停留时间增加
    self.age+=dt
    #粒子膨胀
    if self.alive() and self.expand():#如果停留时间（2s）足够&&膨胀时间（1.2s）足够
      move_x=cos(radians(self.id*360/self.total))*self.initial_speed#粒子的x轴继续膨胀
      move_y=sin(radians(self.id*360/self.total))*self.initial_speed#粒子的y轴继续膨胀
      self.cv.move(self.cid, move_x, move_y)#根据id把画布上的粒子移动x和y个距离
      self.vx=move_x/(float(dt)*1000)
    #以自由落体坠落
    elif self.alive():#如果只是停留时间足够，说明膨胀到最大了，应该准备下坠
      move_x=cos(radians(self.id*360/self.total))#x轴继续膨胀
      self.cv.move(self.cid,self.vx+move_x,self.vy+GRAVITY*dt)#而y轴按照重力因素做落体运动，但实际上这个重力是v而不是a
      self.vy+=GRAVITY*dt#更新一下y轴

    elif self.cid is not None:#如果粒子的生命周期已过，就将其移除
      cv.delete(self.cid)#删除该粒子对象
      self.cid=None
  #定义膨胀效果的时间帧
  def expand(self):
    return self.age<=1.2#膨胀时间小于1.2s
  #检查粒子是否仍在生命周期内
  def alive(self):#已停留时间是不是比应该停留时间短
    return self.age<=self.lifespan
'''
烟花模拟回路：
递归调用来在画布上重复发出新的烟火
通过每个“部件”对象内部的更新协议，每次调用时都要在画布上创建并绘制列表（星列表，每个星列表成员都是粒子列表）来重复地在画布上发出新的焰火
'''
#生成新的一轮爆炸
def simulate(cv):
  t=time()#time()函数返回自1970年后经过的浮点秒数，精确到小数点后6位
  explode_points=[]#爆炸点列表--烟花列表
  wait_time=randint(10,100)#随机生成一个int n,10<=n<=100
  numb_explode=randint(6,10)#爆炸的个数是6~10
  #为所有模拟烟花绽放的全部例子创建一列列表
  for point in range(numb_explode):#遍历爆炸的个数
    objects=[]#这是每个点的爆炸粒子列表
    x_cordi=randint(50,550)#每个点的爆炸x轴
    y_cordi=randint(50,150)#爆炸y轴
    speed=uniform(0.5,1.5)#随机生成一个float speed，0.5<=speed<1.5
    size=uniform(0.5,3)#随机生成一个float size,0.5<=size<3
    color=choice(colors)#choice（）是python内置函数，随机返回元组，列表，或字符串的一个成员
    explosion_speed=uniform(0.2,1)#爆炸的绽放速度也要随机出来
    total_particles=randint(10,50)#爆炸出来的粒子数半径也随机
    for i in range(1,total_particles):#同一个烟花爆炸出来的粒子的大小，速度，坐标都是相同的
      r = part(cv, idx=i, total=total_particles, explosion_speed=explosion_speed, x=x_cordi, y=y_cordi,
        vx=speed, vy=speed, color=color, size=size, lifespan=uniform(0.6, 1.75))#把上述参数带入，但他们每个粒子的生存时间是自己独立的
      objects.append(r)#添加进粒子列表里
    explode_points.append(objects)#把该粒子列表添加进烟花列表里

  total_time=.0#先把时间置0
  #在1.8秒时间帧内保持更新
  while total_time<1.8:
    sleep(0.01)#让画面暂停0.01s
    tnew=time()#刷新时间
    t,dt=tnew,tnew-t#时间等于新时间，与上次时间间隔为tnew-t
    for point in explode_points:#遍历烟花列表
      for item in point:#遍历烟花里的粒子列表
        item.update(dt)#更新时间
    cv.update()#刷新页面
    total_time+=dt#为上面的while循环增加时间
  root.after(wait_time,simulate,cv)#将组件置于其他组件之后，就是放在最顶层，覆盖下面的，这里递归第哦啊用了自己，形成新的一轮爆炸
def close(*ignore):
  #打开模拟循环并关闭窗口
  global root
  root.quit()

if __name__=="__main__":
  root=tk.Tk()
  cv=tk.Canvas(root,height=600,width=700)#绘制一个画布
  #绘制一个黑色背景
  #cv.create_rectangle(0,0,600,600,fill="black")
  #use a nice background image
  image=Image.open("D:\\workplace\\code\\github\\python_auto_office\\未公开\\用excel画图\\111.jpg")
  photo=ImageTk.PhotoImage(image)
  cv.create_image(0,0,image=photo,anchor='nw')#在画板上绘制一张图片
  cv.pack()#把cv添加进去
  root.protocol("WM_DELETE_WINDOW",close)
  #在0.1s后才开始调用stimulate()
  root.after(100,simulate,cv)#调用stimulate生成一轮烟花绽放效果
  root.mainloop()#执行root，生成窗口
#让我更加明白了python的一切皆对象