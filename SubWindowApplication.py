import Plane
import pyglet
import os
class GameBoard(Plane.Plane):
    """docstring for MapViewer."""

    def __init__(self, x,y,w,h):
        super(GameBoard, self).__init__(x,y,w,h)
        #load map MapSelector
        #then load map
        #make is so that any change of mapslector will change map
        self.currentMap = "temp.png"
        self.map = Map("temp.png")
        self.map.rescale(w,h)
        self.map.setPosition(x,y)
        self.addSubject(self.map)
        self.addSubject(MapSelector(0,0,150,200))


    def update(self):
        if self.currentMap != self.subjects[1].getSelectedMap():
            self.currentMap = self.subjects[1].getSelectedMap()
            self.changeMap()

    def changeMap(self):
        for i in range(len(self.subjects)):
            if self.subjects[i]==self.map:
                self.map = Map(self.currentMap)
                self.map.rescale(self.w,self.h)
                self.subjects[i] = self.map
                break;


class MapSelector(Plane.Plane):
    def __init__(self, x,y,w,h):
        super(MapSelector, self).__init__(x,y,w,h)
        self.highlightedMaps = []
        self.selectedMap = "temp.png"
        self.importMaps()
        self.sideLength = 60
        self.borderSize = 10

        self.formatButtons()

    def importMaps(self,location= "Images/Maps/"):
        for file in os.listdir(location):
            if not file.endswith(".txt"):

                mapButton = MapImageButton(location + file,0,0)
                self.highlightedMaps.append(0)
                self.addSubject(mapButton)
                print(len(self.subjects))

    def getSelectedMap(self):
        return self.selectedMap
    def formatButtons(self):
        xmax = int((self.w)/(self.sideLength + 5))
        ystep = self.y + self.h - 5
        xstep = self.x + 5
        for i in range(len(self.subjects)):
            print(i,xmax)
            if(i%xmax == 0):
                print(i%xmax)
                ystep += -self.sideLength - 5
                xstep = self.x + 10
                self.subjects[i].rescale(self.sideLength,self.sideLength)
                self.subjects[i].setPosition(xstep,ystep)
            else:
                xstep += self.sideLength + 5
                self.subjects[i].rescale(self.sideLength,self.sideLength)
                self.subjects[i].setPosition(xstep,ystep)


    def onAction(self,a=(0,0)):
        for i in range(len(self.subjects)):
            if self.subjects[i].isPressed(a):

                self.selectedMap = self.subjects[i].map_source
                self.invertSelection(i)
                break;


    def invertSelection(self, i):
        self.subjects[i].invertBorder()
        a = self.highlightedMaps[i]
        if a is 0:
            self.highlightedMaps[i] = 1
        else:
            self.highlightedMaps[i] = 0

    def isPressed(self,a):
        self.onAction(a)


class Map(Plane.GraphicObject):
    def __init__(self,location):
        super(Map, self).__init__(0,0,0,0)
        image = pyglet.resource.image(location)
        self.map = pyglet.sprite.Sprite(image,x=0,y=0)

    def rescale(self,winx,winy):
        scaley = winy / self.map.height
        scalex = winx / self.map.width
        self.map.update(scale_x=scalex,scale_y=scaley)

    def setPosition(self,x,y):
        self.map.update(x=x,y=y)
        self.x = x
        self.y = y

    def draw(self):
        self.map.draw()
    def isPressed(self,a):
        pass

class MapImageButton(Plane.Button):
    def __init__(self,location,x,y):
        self.map_source = location
        image = pyglet.resource.image(location)
        self.image = pyglet.sprite.Sprite(image,x=0,y=0)
        self.w = self.image.width
        self.h = self.image.height
        self.rgb=(0,0,0)
        self.border = 2

    def rescale(self,x,y):
        scaley = x / self.image.height
        scalex = y / self.image.width
        self.image.update(scale_x=scalex,scale_y=scaley)
        self.w = self.image.width
        self.h = self.image.height
        print(self.image.width,self.image.height)
    def setBorderColor(self,R,G,B):
        self.rgb = (R,G,B)

    def invertBorder(self):
        if self.rgb[0] == 0:

            dr = 255
            dg = 255
            db = 255
        else:
            dr = 0
            dg = 0
            db = 0
        self.setBorderColor(dr,dg,db)

    def setPosition(self,x,y):
        self.image.update(x=x,y=y)
        self.x = x
        self.y = y

    def setBorderSize(self,s):
        self.border = s

    def draw(self):
        x = self.x
        y = self.y
        h = self.h
        w = self.w
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,[0, 1, 2, 0, 2, 3],('v2i', (x-self.border, y-self.border,x+w+self.border, y-self.border,x+w+self.border, y+h+self.border,x-self.border, y+h+self.border)),('c3B', ( self.rgb[0],self.rgb[1],self.rgb[2],self.rgb[0],self.rgb[1],self.rgb[2],self.rgb[0],self.rgb[1],self.rgb[2],self.rgb[0],self.rgb[1],self.rgb[2])))
        self.image.draw()
