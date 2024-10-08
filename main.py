from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        base.camLens.setFov(90)
        x,y = self.land.loadLend('land.txt')
        self.hero = Hero((x // 2, y // 2, 3), self.land)


game = Game()
game.run()
