class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.model = loader.loadModel('smiley')
        self.model.setColor(1, 0.5, 0)
        self.model.setScale(1)
        self.model.setPos(pos)
        self.model.reparentTo(render)
        self.cameraBind()
        self.cameraOn = True
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.model)
        pos = self.model.getPos()
        base.camera.setPos(-pos[0], -pos[1], -pos[2])
        self.cameraOn = True

    def cameraUp(self):
        base.enableMouse()
        pos = self.model.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        self.cameraOn = False

    def accept_events(self):
        base.accept('c', self.change_view)

    def change_view(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()
