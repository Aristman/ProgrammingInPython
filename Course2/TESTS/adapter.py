class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid: list):
        map_lights = []
        map_obstacles = []
        self.adaptee.set_dim((len(grid[0]), len(grid)))
        for col in range(len(grid)):
            for row in range(len(grid[col])):
                if grid[col][row] == 1:
                    map_lights.append((row, col))
                elif grid[col][row] == -1:
                    map_obstacles.append((row, col))
        self.adaptee.set_lights(map_lights)
        self.adaptee.set_obstacles(map_obstacles)
        return self.adaptee.generate_lights()
