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
        base.camera.setPos(-0, 0, 1)
        self.cameraOn = True

    def cameraUp(self):
        base.enableMouse()
        pos = self.model.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        self.cameraOn = False

    def accept_events(self):
        base.accept('c', self.change_view)
        base.accept('arrow_left', self.turn_left)
        base.accept('arrow_left'+'-repeat', self.turn_left)

        base.accept('arrow_right', self.turn_right)
        base.accept('arrow_right'+'-repeat', self.turn_right)

        base.accept('w', self.forward)
        base.accept('w' + '-repeat', self.forward)

        base.accept('s', self.backward)
        base.accept('s' + '-repeat', self.backward)

        base.accept('a', self.left)
        base.accept('a' + '-repeat', self.left)

        base.accept('d', self.right)
        base.accept('d' + '-repeat', self.right)

    def turn_right(self):
        a = self.model.getH()
        a -= 5
        self.model.setH(a % 360)

    def check_dir(self, angle):
        if 0 <= angle <= 20:
            return 0, -1
        elif 20 < angle <= 65:
            return 1, -1
        elif 65 < angle <= 110:
            return 1, 0
        elif 110 < angle <= 155:
            return 1, 1
        elif 155 < angle <= 200:
            return 0, 1
        elif 200 < angle <= 245:
            return -1, 1
        elif 245 < angle <= 290:
            return -1, 0
        elif 290 < angle <= 335:
            return -1, -1
        else:
            return 0, -1

    def look_at(self, angle):
        from_x = round(self.model.getX())
        from_y = round(self.model.getY())
        from_z = round(self.model.getZ())

        dx, dy = self.check_dir(angle)

        return from_x + dx, from_y + dy, from_z

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.model.setPos(pos)

    def forward(self):
        angle = (self.model.getH()) % 360
        self.try_move(angle)

    def backward(self):
        angle = (self.model.getH() + 180) % 360
        self.try_move(angle)

    def left(self):
        angle = (self.model.getH() + 90) % 360
        self.try_move(angle)

    def right(self):
        angle = (self.model.getH() - 90) % 360
        self.try_move(angle)

    def turn_left(self):
        a = self.model.getH()
        a += 5
        self.model.setH(a % 360)

    def change_view(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.model.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.model.setPos(pos)
