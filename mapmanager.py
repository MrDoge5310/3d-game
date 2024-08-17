class Mapmanager:
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.color = (0.2, 0.2, 0.4, 1)
        self.land = None
        self.startNew()

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self, position):
        block = loader.loadModel(self.model)
        block.setTexture(loader.loadTexture(self.texture))
        block.setPos(position)
        block.setColor(self.color)
        block.reparentTo(self.land)

    def loadLend(self, filename):
        with open(filename, 'r') as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z) + 1):
                        if z0 > 0:
                            self.color = (1, 0, 0, 1)
                        else:
                            self.color = (0.2, 0.2, 0.4, 1)
                        self.addBlock((x, y, z0))
                    x += 1
                y += 1

