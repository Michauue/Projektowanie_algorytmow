from ctypes import pointer
import glfw
from OpenGL.GL import *
from numpy import ones,vstack
from numpy.linalg import lstsq


def cross_point(line1,line2):
    x1=line1[0]
    y1=line1[1]
    x2=line1[2]
    y2=line1[3]
    
    x3=line2[0]
    y3=line2[1]
    x4=line2[2]
    y4=line2[3]
    
    k1=(y2-y1)*1.0/(x2-x1)
    b1=y1*1.0-x1*k1*1.0
    if (x4-x3)==0:
        k2=None
        b2=0
    else:
        k2=(y4-y3)*1.0/(x4-x3)
        b2=y3*1.0-x3*k2*1.0
    if k2==None:
        x=x3
    else:
        x=(b2-b1)*1.0/(k1-k2)
    y=k1*x*1.0+b1*1.0
    if x>x1 and x>x2:
        return None
    elif x<x1 and x<x2:
        return None
    elif x<x3 and x<x4:
        return None
    elif x>x3 and x>x4:
        return None
    elif y>y1 and y>y2:
        return None
    elif y<y1 and y<y2:
        return None
    elif y<y3 and y<y4:
        return None
    elif y>y3 and y>y4:
        return None
    else:     
        return [round(x,2),round(y,2)]


def calcStraight(points):
    for i in range(len(points)):
        x_coords, y_coords = zip(*points[i])
        print(x_coords)
        A = vstack([x_coords,ones(len(x_coords))]).T
        a, b = lstsq(A, y_coords)[0]
        straight_tab.append([a,b])

def side(cordinates,line1,straight_tab):
    x=cordinates[0]
    y=cordinates[1]

    i=straight_tab[0]
    j=straight_tab[1]

    x1=line1[0]
    y1=line1[1]
    x2=line1[2]
    y2=line1[3]

    print(cordinates, line1, straight_tab)

    if x1<x2:
        if i * x + j < y:
            return False
        else:
            return True
    elif x1>x2:
        if i * x + j > y:
            return False
        else:
            return True
    elif x1 == x2:
        if y1 < y2:
            if x > x1:
                return True
            else:
                return False
        elif y1 > y2:
            if x < x1:
                return True
            else:
                return False


def pointPosition(cordinates,vertices_tab):
    calcStraight(points)
    for i in range(len(vertices_tab)):
        temp_var = side(cordinates,vertices_tab[i],straight_tab[i])
        print(temp_var)

vertices_tab = []

count = int(input('Ile odcinków chcesz dodać? '))

for z in range(count):
    print("Podaj współrzędne odcinka ", z+1 , ": ")
    vertices_tab.append([])
    for x in range(2):
        if x == 0:
            temp = 'początkowego'
        else:
            temp = 'końcowego'
        print("Podaj współrzędne punktu ", temp , ": ")
        vertices_tab[z].append(float(input()))
        vertices_tab[z].append(float(input()))

print(vertices_tab)

# vertices_tab = [[0.5, 0.4, -0.8, -0.5],
#                 [-0.1, 0.9, 0.6, 0.0],
#                 [0.2, -0.8, -0.74, -0.13],
#                 [0.25, -0.9, 0.0, 0.9]]
# count = len(vertices_tab)
temp = []
points = []
straight_tab = []
cordinates = [-0.35, 0.15]

for i in range(count):
    for j in range(count):
        if vertices_tab[i] == vertices_tab[j]:
            break
        point = cross_point(vertices_tab[i], vertices_tab[j])
        if point != None:
            temp.append(point)


for i in range(len(vertices_tab)):
    points.append([(vertices_tab[i][0], vertices_tab[i][1]), (vertices_tab[i][2], vertices_tab[i][3])])

print(points)
calcStraight(points)
print(straight_tab)
pointPosition(cordinates, vertices_tab)

if not glfw.init():
    raise Exception("glfw can not be initialized!")


window = glfw.create_window(1280, 720, "My OpenGL window", None, None)


if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")


glfw.set_window_pos(window, 50, 50)
glfw.make_context_current(window)

glClearColor(1.0, 1.0, 1.0, 1.0)

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    glLoadIdentity()
    glLineWidth(2.0)

    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(-1, 0)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(1, 0)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(0, 1)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(0, -1)
    glEnd()

    glBegin(GL_POINTS)
    glColor3f(0.5, 0.5, 0.5)
    glVertex2f(cordinates[0],cordinates[1])
    glEnd()

    glLineWidth(5.0)
    for z in range(count):
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0)    #początek zielony
        glVertex2f(vertices_tab[z][0], vertices_tab[z][1])
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(vertices_tab[z][2], vertices_tab[z][3])
        glEnd()

    glPointSize(10)
    for z in range(len(temp)):
        glBegin(GL_POINTS)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(temp[z][0], temp[z][1])
        glEnd()

    glfw.swap_buffers(window)


glfw.terminate()