import Plane


class TopBarMenu(Plane.Plane):
    """docstring for TopBarMenu."""

    def __init__(self,windowWidth, windowHeight):
        s = 20
        x = 0
        y = windowHeight - windowHeight/s
        w = windowWidth
        h = windowHeight/s
        print(w)
        super(TopBarMenu, self).__init__(x,y, w , h , FORMAT = Plane.Format.MENU_X)

        self.addSubject(Plane.Button(100,100,100,100))
        self.addSubject(Plane.Button(100,100,100,100))
        self.addSubject(Plane.Button(100,100,100,100))
        self.addSubject(Plane.Button(100,100,100,100))
