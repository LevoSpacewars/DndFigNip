import pyglet
from pyglet.window import mouse
import Plane
import Ui
from Plane import Format
window = pyglet.window.Window()

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')


image = pyglet.resource.image('Images/Maps/OIP.jpg')
print(window.width)
topmenu = Ui.TopBarMenu(window.width,window.height)
plane = Plane.Plane(0,100,window.width,window.height/10,FORMAT = Format.MENU_X)
class test():

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        print("pressed")
        topmenu.onAction(a=(x,y))

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)
    label.draw()
    plane.draw()
    topmenu.draw()

pyglet.app.run()
