class Mapmanager:
    def __init__(self):
        self.model = 'box'
        # self.texture = 'box'
        self.color = (0.2, 0.2, 0.35, 1)
        self.land = None
        self.startNew()
        self.addBlock((0, 0, 0))

    def startNew(self):
        self.land = render.attachNewNode("Land")

    def addBlock(self, position):
        block = loader.loadModel(self.model)
        # block.setTexture(loader.loadTexture(self.texture))
        block.setPos(position)
        block.setColor(self.color)
        block.reparentTo(self.land)
