import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, x):
        self.x = x

    def __add__(self, y):
        return Vec2d((self.x[0] + y.x[0], self.x[1] + y.x[1]))

    def __sub__(self, y):
        return Vec2d((self.x[0] - y.x[0], self.x[1] - y.x[1]))

    def __mul__(self, k):
        return Vec2d((self.x[0] * k, self.x[1] * k))

    def __len__(self):
        return math.sqrt(self.x[0] ** 2 + self.x[1] ** 2)

    def int_pair(self):
        return tuple((self.x[0], self.x[1]))


class Polyline:
    def __init__(self):
        self.points = []
        self.speed = []

    def add_point(self, x, speed):
        self.points.append(Vec2d(x))
        self.speed.append(Vec2d(speed))

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speed[p]
            if self.points[p].x[0] > SCREEN_DIM[0] or self.points[p].x[0] < 0:
                self.speed[p].x = (- self.speed[p].x[0], self.speed[p].x[1])
            if self.points[p].x[1] > SCREEN_DIM[1] or self.points[p].x[1] < 0:
                self.speed[p].x = (self.speed[p].x[0], -self.speed[p].x[1])

    def draw(self, pygame, gameDisplay, width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        for p in self.points:
            pygame.draw.circle(gameDisplay, color,
                               (int(p.x[0]), int(p.x[1])), width)


class Knot(Polyline):
    def __init__(self, count):
        super().__init__()
        self.points_for_line = []
        self.count = count

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return (points[deg] * alpha) + (self.get_point(points, alpha, deg - 1) * (1 - alpha))

    def get_points(self, base_points):
        alpha = 1 / self.count
        res = []
        for i in range(self.count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)

            res.extend(self.get_points(ptn))
        return res

    def add_point(self, x, speed):
        super().add_point(x, speed)
        self.points_for_line = self.get_knot()

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        super().set_points()
        self.points_for_line = self.get_knot()

    def draw(self, pygame, gameDisplay, width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        super().draw(pygame, gameDisplay)

        for p_n in range(-1, len(self.points_for_line) - 1):
            pygame.draw.line(gameDisplay, color,
                             (int(self.points_for_line[p_n].x[0]), int(self.points_for_line[p_n].x[1])),
                             (int(self.points_for_line[p_n + 1].x[0]), int(self.points_for_line[p_n + 1].x[1])), width)


def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")
    steps = 35
    working = True
    points = Knot(steps)
    pause = True
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
                    points = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.add_point(event.pos, (random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)

        points.draw(pygame, gameDisplay, 3, color)

        if not pause:
            points.set_points()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)


if __name__ == "__main__":
    main()
