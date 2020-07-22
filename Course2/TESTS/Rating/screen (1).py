#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """возвращает сумму двух векторов"""
        if isinstance(other, Vec2d):
            return Vec2d(self.x + other.x, self.y + other.y)
        elif hasattr(other, "__getitem__"):
            return Vec2d(self.x + other[0], self.y + other[1])
        else:
            return Vec2d(self.x + other, self.y + other)

    def __sub__(self, other):
        """"возвращает разность двух векторов"""
        return Vec2d(self.x - other.x, self.y - other.y)
    
    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        return Vec2d(self.x * k, self.y * k)

    def len(self):
        """возвращает длину вектора"""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def int_pair(self):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return int(self.x), int(self.y)

class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def add_points(self,point, speed):
        self.points.append(point)
        self.speeds.append(speed)


    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p].__add__(self.speeds[p])
            if self.points[p].int_pair()[0] > SCREEN_DIM[0] or self.points[p].int_pair()[0] < 0:
                self.speeds[p] = (- self.speeds[p][0], self.speeds[p][1])
            if self.points[p].int_pair()[1] > SCREEN_DIM[1] or self.points[p].int_pair()[1] < 0:
                self.speeds[p] = (self.speeds[p][0], -self.speeds[p][1]) 
    
    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        
        for p in self.points:
            pygame.draw.circle(gameDisplay, color,
                                (int(p.int_pair()[0]), int(p.int_pair()[1])), width)

class Knot(Polyline):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def add_points(self, point, speed):
        super().add_points(point,speed)
        self.get_knot()

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append(self.points[i].__add__(self.points[i + 1]).__mul__(0.5))
            ptn.append(self.points[i + 1])   
            ptn.append((self.points[i+1].__add__(self.points[i + 2])).__mul__(0.5))
            res.extend(self.get_points(ptn))
        return res
    
    def get_points(self, base_points):
        alpha = 1 / self.count
        res = []
        for i in range(self.count):
            res.append(self.get_point(base_points, i * alpha))
        return res
    
    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg]*alpha + self.get_point(points, alpha, deg - 1) * (1 - alpha)


    def draw_lines(self, points, style="line", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(points)- 1): 
                pygame.draw.line(gameDisplay, color,
                                    (int(points[p_n].int_pair()[0]), int(points[p_n].int_pair()[1])),
                                    (int(points[p_n + 1].int_pair()[0]), int(points[p_n + 1].int_pair()[1])), width)




def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))

# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    points = []
    speeds = []
    show_help = False
    pause = True
    polyline = Polyline()
    knot = Knot(steps)
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
                    polyline = Polyline()
                    knot = Knot(steps)
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                polyline.add_points(Vec2d(event.pos[0],event.pos[1]), (random.random() * 2, random.random() * 2))
                knot.add_points(Vec2d(event.pos[0],event.pos[1]), (random.random() * 2, random.random() * 2))
        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)  
        polyline.draw_points()  
        knot.draw_lines(knot.get_knot(), "line", 3, color)
        if not pause:
            polyline.set_points()
            knot.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
