import math,turtle,time
from pynput import keyboard,mouse
'''
def vector_xy(v1=[1,1,0]):
    return math.atan(v1[1]/v1[0])
def vector_xz(v1=[1,0,1]):
    return math.atan(v1[3]/v1[0])
'''

def vector_xy(v1,v2):
    x1=v1[0]
    y1=v1[1]
    x2=v2[0]
    y2=v2[1]
    s1=x1*x2+y1*y2
    s2=(x1**2+y1**2)**0.5*(x2**2+y2**2)**0.5



    s3=math.acos(s1/s2)


    if (y1/x1<y2/x2 ):
        s3=0-s3


    return s3

def vector_xz(v1,v2):
    x1=v1[0]
    y1=v1[2]
    x2=v2[0]
    y2=v2[2]
    s1=x1*x2+y1*y2
    s2=(x1**2+y1**2)**0.5*(x2**2+y2**2)**0.5

    s3 = math.acos(s1 / s2)

    if (y1 / x1 <y2 / x2):
        s3 = 0 - s3
    global logs

    return s3






class camera():
    def __init__(self,position=[0,0,0],vision_deg=math.pi/3):
        self.position=position
        self.vision_deg=vision_deg
        self.vision_vector=(1,0,0)#[cos z-xy*cos x-y,cos z-x*sin x-y,sin z-xy]
    def turn_xyzcamera(self,xyz_package):
        self.vec_ob=[]
        self.xyz_grouplens=0
        for tri in xyz_package:#get triangle list
            t_tri=[]
            self.xyz_grouplens+=1
            for xyz in tri:#get xyz
                temp=[]

                for i in range(3):#get x,y,z

                    temp.append(xyz[i]-self.position[i]+0.000001)
                t_tri.append(temp)
            self.vec_ob.append(t_tri)

    def return_xyz_grouplens(self):
        return self.xyz_grouplens

    def turn_camera_vision_xyz(self,groupnum):
        t_temp=[]
        for i in range(3):


            tris_temp = []
            t1=self.vec_ob[groupnum][i]
            d1=(vector_xy(self.vec_ob[groupnum][i],self.vision_vector))
            d2 = (vector_xz(self.vec_ob[groupnum][i], self.vision_vector))

            tris_temp.append(d1)
            tris_temp.append(d2)
            t_temp.append(tris_temp)
        return t_temp



class drawing:
    def __init__(self):
        turtle.tracer(False)

    def update(self):
        turtle.setup()
        turtle.clear()
    def triangle(self,lists,color):



        turtle.penup()
        turtle.pencolor(color)

        turtle.goto(lists[0][0] * 400, lists[0][1] * 400)
        turtle.pendown()
        for i in range(1,3):
            turtle.goto(lists[i][0]*400,lists[i][1]*400)
        turtle.goto(lists[0][0] * 400, lists[0][1] * 400)

        if logs:
            print(lists)











c1=camera()
vec=[[[7,2,9],[5,1,7],[11,0,7]],[[7,2,9],[5,8,2],[11,0,7]],[[7,2,9],[5,8,2],[5,1,7]]]

logs=False

def press(key):
    global logs
    try :
        if key.char=='s':
            c1.position[0] -= c1.vision_vector[0] * 0.5
            c1.position[1] -= c1.vision_vector[1] * 0.5
            c1.position[2] -= c1.vision_vector[2] * 0.5
        if key.char=='w':
            c1.position[0]+=c1.vision_vector[0]*0.5
            c1.position[1] += c1.vision_vector[1] * 0.5
            c1.position[2] += c1.vision_vector[2] * 0.5
        if key.char=='d':
            c1.position[1]+=0.5
        if key.char=='a':
            c1.position[1]-=0.5
    except:
        if key==keyboard.Key.space:
            c1.position[2]+=0.5
        if key==keyboard.Key.shift:
            c1.position[2]-=0.5
        if key==keyboard.Key.f3:
            logs=True






def mouse_move(x,y):
    x1=(x-990)/400*math.pi
    y1=-(y-540)/400*math.pi
    c1.vision_vector=[math.cos(y1)*math.cos(x1),math.cos(y1)*math.sin(x1),math.sin(y1)]



m1=mouse.Controller()
m1.position=[990,540]
m=mouse.Listener(on_move=mouse_move)
l=keyboard.Listener(on_press=press)

l.start()
m.start()


d=drawing()
while True:
    c1.turn_xyzcamera(vec)
    d.update()

    d.triangle(c1.turn_camera_vision_xyz(0),'red')
    d.triangle(c1.turn_camera_vision_xyz(1),'blue')
    d.triangle(c1.turn_camera_vision_xyz(2),'gray')
    #print(c1.position)






