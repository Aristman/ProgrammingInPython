"""
Первая программа по графическому интерфейсу. Использует сторонний модуль graphics.py
"""

import graphics as gr


def main():
    window = gr.GraphWin('Первая графика', 600, 600)
    draw_image(window)
    window.getMouse()


def draw_image(window):
    house_x, house_y = window.width // 2, window.height // 2
    house_wigth = window.width // 3
    house_height = house_wigth * 4 // 3

    draw_background(window)
    draw_house(window, house_x, house_y, house_wigth, house_height)


def draw_background(window, color_earth='green', color_scy='cyan'):
    earth = gr.Rectangle(gr.Point(0, window.height // 2),
                         gr.Point(window.width - 1, window.height - 1))
    earth.setFill(color_earth)
    earth.draw(window)
    scy = gr.Rectangle(gr.Point(0, 0),
                       gr.Point(window.width - 1, window.height // 2))
    scy.setFill(color_scy)
    scy.draw(window)


def draw_house_walls(window, x, y, widht, height):
    walls = gr.Rectangle(gr.Point(x - widht // 2, y),
                         gr.Point(x + widht // 2, y + height))
    walls.setFill('brown')
    walls.draw(window)


def draw_house_foundation(window, x, y, width, height):
    pass


def draw_house_roof(window, x, y, width, height):
    pass


def draw_house(window, x, y, width, height):
    foundation_height = height // 8
    walls_height = height // 2
    walls_widht = 7 * width // 8
    roof_height = height - walls_height - foundation_height
    draw_house_foundation(window, x, y, width, foundation_height)
    draw_house_walls(window, x, y - foundation_height, walls_widht, walls_height)
    draw_house_roof(window, x, y - foundation_height - walls_height, width, roof_height)


if __name__ == '__main__':
    main()
