from screen_objects import *
import time

class Character():

    ALIVE = "ALIVE"
    DEAD = "DEAD"

    def __init__(self, world, pos, body: list, speed:int =5, dmg:int =1, hp:int =100, state=ALIVE):
        self.world = world
        self.pos = list(pos)
        self.body = body
        self.spd = speed
        self.dmg = dmg
        self.hp = hp
        self.state = state
        self.stage = self.world.get_stage()
        self.bounds = self.stage.get_bounds()

    def draw(self):
        for i in self.body:
            i.draw()

    def clear(self):
        for i in self.body:
            i.clean()

    def reset(self):
        for i in self.body:
            i.reset()

    def move(self, direction):
        if direction == 1:
            if get_inside(self.bounds, [self.pos[0]+self.spd, self.pos[1]]):
                self.pos[0] += self.spd
                for i in self.body:
                    i.set_pos((self.spd, 0))

        elif direction == -1:
            if get_inside(self.bounds, [self.pos[0]-self.spd, self.pos[1]]):
                self.pos[0] -= self.spd
                for i in self.body:
                    i.set_pos((-self.spd, 0))

        elif direction == 2:
            if get_inside(self.bounds, [self.pos[0], self.pos[1]-self.spd]):
                self.pos[1] -= self.spd
                for i in self.body:
                    i.set_pos((0, -self.spd))

        elif direction == -2:
            if get_inside(self.bounds, [self.pos[0], self.pos[1]+self.spd+35]):
                self.pos[1] += self.spd
                for i in self.body:
                    i.set_pos((0, self.spd))

    def attk(self, other):
        pass

    def kill_self(self):
        self.state = self.DEAD
        self.clear()

class Player(Character):
    COLOUR = (255, 255, 255, 255)
    CHAR = "@|^"

    def __init__(self, world, pos, spd=5, dmg=5, hp=100, scr=0, state=Character.ALIVE):
        body = Text_Img(world.get_stage(), self.COLOUR, pos, self.CHAR, 18, vert=True)
        Character.__init__(self, world, pos, [body], spd, dmg, hp, state)
        self.scr = scr

    def wep_swap(self):
        pass

    def fire(self):
        pass

    def increase_score(self):
        pass

