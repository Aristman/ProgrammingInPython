from math import sqrt
import pygame
import random


class Vec2d:
    """Vectors class"""

    def __init__(self, coordinate):
        self.x = coordinate[0]
        self.y = coordinate[1]

    def __str__(self):
        return ':'.join(map(str, self.int_pair())) + ' '

    def __add__(self, other):
        return Vec2d((self.x + other.x, self.y + other.y))

    __radd__ = __add__

    def __sub__(self, other):
        return Vec2d((self.x - other.x, self.y - other.y))

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2d((self.x * other, self.y * other))

    def len(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def int_pair(self):
        return int(self.x), int(self.y)


class Polyline:
    """Polyline class"""

    def __init__(self, display):
        self._display = display
        self.points = []
        self.speeds = []
        self.line_speed = 0

    def add_point(self, point):
        """Adding a new point to the base at a random speed"""
        self.points.append(Vec2d(point))
        self.speeds.append(Vec2d((random.random() * 2, random.random() * 2)))

    def del_point(self):
        """Removing a point from a line"""
        if len(self.points) > 0:
            self.points.pop()
            self.speeds.pop()

    def clear(self):
        """Reset and clear data"""
        self.points.clear()
        self.speeds.clear()

    def set_points(self):
        """function of recalculation of coordinates of control points"""
        for p in range(len(self.points)):
            self.points[p] += self.speeds[p]
            if self.points[p].x > self._display.get_width() or self.points[p].x < 0:
                self.speeds[p].x *= -1
            if self.points[p].y > self._display.get_height() or self.points[p].y < 0:
                self.speeds[p].y *= -1

    def draw_points(self):
        """function of drawing points on the screen"""
        color = (255, 255, 255)
        for p in self.points:
            pygame.draw.circle(self._display, color,
                               (p.int_pair()), 3)

    def draw_line(self, width, color, points=None):
        """Poly line draw function"""
        points = points or self.points
        if len(points) >= 3:
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(self._display, color,
                                 points[p_n].int_pair(),
                                 points[p_n + 1].int_pair(), width)


class Knot(Polyline):
    """Smoothed line descendant class"""

    def __init__(self, display, steps):
        super().__init__(display)
        self.steps = steps
        self.line_points = []

    def clear(self):
        super().clear()
        self.line_points.clear()

    def add_point(self, point):
        super().add_point(point)
        self.get_knot()

    def del_point(self):
        super().del_point()
        self.get_knot()

    def set_points(self):
        super().set_points()
        self.get_knot()

    def draw_line(self, width, color, points=None):
        """Line drawing function"""
        points = points or self.line_points
        if len(self.points) >= 3:
            self.get_knot()
            super().draw_line(width, color, points)

    def get_knot(self):
        """Function for calculating additional line points"""
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)
            res.extend(self._get_points(ptn, self.steps))
        self.line_points = res

    def _get_points(self, base_points, count):
        """Function forming a list of smooth line vectors"""
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self._get_point(base_points, i * alpha))
        return res

    def _get_point(self, points, alpha, deg=None):
        """Recursive function when calculating additional points"""
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + self._get_point(points, alpha, deg - 1) * (1 - alpha)


class GameHelp:
    """Help window class"""

    def __init__(self, display, help_menu: dict):
        self.display = display
        self._width = display.get_width()
        self._height = display.get_height()
        self.help_menu = help_menu
        self.isshow = False

    def show_help_window(self):
        self.display.fill((60, 60, 60))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        pygame.draw.lines(self.display, (255, 50, 50, 255), True, [
            (0, 0),
            (self._width, 0),
            (self._width, self._height),
            (0, self._height)
        ], 5)
        for i, it in enumerate(self.help_menu):
            gameDisplay.blit(font1.render(
                str(it), True, (128, 128, 255)), (100, 100 + 30 * i))
            gameDisplay.blit(font2.render(
                str(self.help_menu[it]), True, (128, 128, 255)), (400, 100 + 30 * i))


help_menu = {
    "F1": "Show Help",
    "R": "Restart",
    "P": "Pause/Play",
    "Num+": "More points",
    "Num-": "Less points",
    "Mouse Left button": "Add point",
    "Mouse Right button": "Remove point",
    "Del": "Delete last line",
    "Insert": "Insert new line",
    "": "",
    "Current points": 5,
    "Current line": 0
}

if __name__ == '__main__':
    pygame.init()
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("MyScreenSaver")
    gameDisplay.fill((0, 0, 0))

    working = True
    pause = True
    line = [Knot(gameDisplay, 5), ]  # List of polyline objects
    help_win = GameHelp(gameDisplay, help_menu)
    index_line = 0
    show_help = False

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    index_line = 0
                    line = [Knot(gameDisplay, 5), ]
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS and type(line[index_line]) is Knot:
                    line[index_line].steps += 1
                    help_win.help_menu["Current points"] = line[index_line].steps
                if event.key == pygame.K_F1:
                    help_win.isshow = not help_win.isshow
                if event.key == pygame.K_KP_MINUS and type(line[index_line]) is Knot:
                    line[index_line].steps -= 1 if line[index_line].steps > 1 else 0
                    help_win.help_menu["Current points"] = line[index_line].steps
                if event.key == pygame.K_INSERT:
                    line.append(Knot(gameDisplay, 5))
                    index_line += 1
                    help_win.help_menu["Current line"] = index_line
                    help_win.help_menu["Current points"] = 5
                if event.key == pygame.K_DELETE and len(line) > 1:
                    line.pop()
                    index_line -= 1
                    help_win.help_menu["Current line"] = index_line
                    help_win.help_menu["Current points"] = line[index_line].steps
                if event.key == pygame.K_w:
                    line[index_line].line_speed += 1
                if event.key == pygame.K_s:
                    line[index_line].line_speed -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    line[index_line].add_point(event.pos)
                elif event.button == pygame.BUTTON_RIGHT:
                    line[index_line].del_point()

        gameDisplay.fill((0, 0, 0))
        for lin in line:
            if not pause:
                lin.set_points()
            lin.draw_points()
            hue = (hue + 1) % 360
            color.hsla = (hue, 100, 50, 100)
            lin.draw_line(5, color)
        if help_win.isshow:
            help_win.show_help_window()
        pygame.display.flip()
    pygame.display.quit()
    pygame.quit()
    exit(0)
