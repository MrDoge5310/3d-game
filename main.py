from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        base.camLens.setFov(90)
        self.land.loadLend('land3.txt')


game = Game()
game.run()
