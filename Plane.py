import pyglet
from enum import Enum
class Format(Enum):
    MENU_X = 0
    MENU_Y = 1
    GRID   = 2
    SHELF  = 3

class GraphicObject:
    def __init__(self,x,y,w,h):
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)
    def setPosition(self,x,y):
        self.x = int(x)
        self.y = int(y)
    def setScale(self,w,h):
        self.w = int(w)
        self.h = int(h)

class Plane(GraphicObject):
    """docstring for Plane."""

    def __init__(self, x,y,w,h, FORMAT = None):
        super(Plane, self).__init__(x,y,w,h)
        self.subjects = []
        self.FORMAT = FORMAT
        self.addSubject(Button(100,100,100,100))
        self.addSubject(Button(100,100,100,100))
        self.addSubject(Button(100,100,100,100))
        self.addSubject(Button(100,100,100,100))


    def draw(self):
        x = self.x
        y = self.y
        h = self.h
        w = self.w
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,[0, 1, 2, 0, 2, 3],('v2i', (x, y,x+w, y,x+w, y+h,x, y+h)),('c3B', ( 167,167,167,167,167,167,167,167,167,167,167,167)))
        self.drawSubjects()

    def drawSubjects(self):
        for i in range(len(self.subjects)):
            self.subjects[i].draw()
    def addSubject(self, object):
        if self.FORMAT == Format.MENU_X:
            object.setPosition(self.w/50 + (self.x + self.w/10 + self.w/100) * len(self.subjects), self.y + self.h/10)
            object.setScale(self.w/10, self.h*(1-0.2))

        self.subjects.append(object)


class Button(GraphicObject):
    """docstring for Button."""

    def __init__(self, x,y,w,h):
        super(Button, self).__init__(x,y,w,h)
    def draw(self):
        x = self.x
        y = self.y
        h = self.h
        w = self.w
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
        [0, 1, 2, 0, 2, 3],
        ('v2i', (x, y,
                 x+w, y,
                 x+w, y+h,
                 x, y+h)),
         ('c3B', ( 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255))
                 )
