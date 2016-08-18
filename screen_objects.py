'''

'''
import pygame
import pygame.freetype
import pygame.gfxdraw
import pygame.math

class Stage:
    def __init__(self, disp, pos, size, col):
        self.disp = disp
        self.disp_surf = self.disp.get_surface()
        self.pos = pos
        self.size = size
        self.col = col
        self.surf = pygame.Surface(self.size)
        self.surf.fill(self.col)
        self.update()

    def get_surf(self):
        return self.surf

    def get_bounds(self):
        return [[0, 0], [0, self.size[1]], list(self.size), [self.size[0], 0]]

    def update(self):
        self.disp_surf.blit(self.surf, self.pos)

    def clear(self):
        self.surf.fill(self.col)
        self.disp_surf.blit(self.surf, self.pos)

class Img:
    def __init__(self, stage, col, pos):
        self.stage = stage
        self.col = list(col)
        self.pos = list(pos)

    def draw(self):
        pass

    def clean(self):
        self.col[3] = 0

    def reset(self):
        self.col[3] = 255

    def set_pos(self, new_pos):
        pass

    def rotate(self, angle):
        pass

class Text_Img(Img):
    pygame.freetype.init()
    FONT = pygame.freetype.Font("resources/FreeMono.ttf")
    FONT.antialiased = False

    def __init__(self, stage, col, pos, text, size, padx=0, pady=0, vert=False):
        Img.__init__(self, stage, col, pos)
        self.text = text
        self.size = size
        self.padx = padx
        self.pady = pady
        self.vert = vert
        self.FONT.vertical = self.vert

    def draw(self):
        self.FONT.render_to(self.stage.get_surf(), [self.pos[0]+self.padx, self.pos[1]+self.pady],
                            self.text, self.col, size=self.size)

    def set_size(self, size):
        self.size = size

    def set_pos(self, new_pos):
        self.pos[0] += new_pos[0]
        self.pos[1] += new_pos[1]

class Line_Img(Img):
    def __init__(self, stage, col, pos, pointlst):
        Img.__init__(self, stage, col, pos)
        self.pointlst = pointlst
        self.points = move_pts(self.pos, self.pointlst)

    def draw(self):
        pygame.gfxdraw.polygon(self.stage.get_surf(), self.points, self.col)

    def set_pos(self, new_pos):
        self.points = move_pts(new_pos, self.points)

def rotate_pts(pivot, pt_list, angle):
    new_pt_list = []
    for pt in pt_list:
        new_pt_list.append(pygame.math.Vector2((pt[0] - pivot[0], pt[1] - pivot[1])).rotate(angle))

    for i in range(len(new_pt_list)):
        pt_list[i] = [round(x) for x in list(new_pt_list[i])]
        pt_list[i][0] += pivot[0]
        pt_list[i][1] += pivot[1]

def move_pts(pos, points):
    x = points[:]
    for pt in x:
        pt[0] += pos[0]
        pt[1] += pos[1]

    return x

def get_inside(bounds, point):
    def _lst_less(lst1, lst2):
        if lst2[0] < lst1[0]:
            return True

        elif lst2[1] < lst1[1]:
            return True

        return False

    s = []
    for pt in bounds:
        if _lst_less(pt, point):
            s.append(1)
        else:
            s.append(0)

    if s == [0, 1, 1, 1]:
        return True
    return False

