from screen_objects import Stage

class World:
    def __init__(self, display, clock):
        self._disp = display
        self._clk = clock
        self._play_area = Stage(self._disp, (0, 0), (500, 300), (40, 40, 40, 255))
        self._utility_area = Stage(self._disp, (0, 300), (500, 200), (0, 0, 0, 0))

    def update_world(self):
        self._play_area.update()
        self._utility_area.update()

        self._disp.update()

        self._play_area.clear()
        self._utility_area.clear()

    def update_world_persist(self):
        self._play_area.update()
        self._utility_area.update()
        self._disp.update()

    def get_stage(self):
        return self._play_area

    def get_utility_screen(self):
        return self._utility_area

    def get_clock(self):
        return self._clk