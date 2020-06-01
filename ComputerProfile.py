import Plane
from SubWindowApplication import Map, GameBoard
import pyglet

## TODO: add control click for selection on the map modifiers.
# TODO: add controlable tocken characters.

class ClientEngine(object):
    """docstring for ClientEngine."""

    def __init__(self, arg):
        super(ClientEngine, self).__init__()
        self.arg = arg


class HostEngine(object):
    """docstring for HostEngine."""

    def __init__(self):
        super(HostEngine, self).__init__()

        self.window = pyglet.window.Window()

        self.defineEvents()
        self.board = GameBoard(0,0,self.window.width,self.window.height)
        pyglet.app.run()

    def test(self):
        print("test")

    def draw(self):
        self.window.clear()
        self.board.update()
        self.board.draw()


    def defineEvents(self):

        @self.window.event
        def on_mouse_press(x, y, button, modifiers):
            self.board.onAction((x,y))

        @self.window.event
        def on_draw():
            self.draw()







engine = HostEngine()
