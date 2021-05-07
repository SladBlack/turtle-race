import turtle
import random


width_size = 500
height_size = 500
turtle.screensize(width_size, height_size)
turtle_count = 8
color_dict = {'red': 'Красный',
              'brown': 'Коричневый',
              'yellow': 'Желтый',
              'blue': 'Синий',
              'green': 'Зеленый',
              'black': 'Черный',
              'purple': 'Фиолетовый',
              'pink': 'Розовый',
              }


class Racer(object):
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.setposition(x=position[0], y=position[1])

    def move(self):
        """Движение черепахи"""
        r = random.randint(1, 15)
        self.turt.pendown()
        self.turt.forward(r)

    def get_xcor(self):
        """Узнать координату х"""
        return self.turt.xcor()


def start_game():
    turtle.clearscreen()
    tList = list()
    start_y = 300
    start_x = -250

    for i in range(turtle_count):
        start_y -= height_size / turtle_count
        tList.append(Racer(list(color_dict.keys())[i], [start_x, start_y]))

    finish = 250
    maxDis = -250
    winners = []

    while maxDis < finish:
        for t in tList:
            t.move()
            x_cor = t.get_xcor()
            if x_cor >= maxDis:
                maxDis = t.get_xcor()
            if x_cor >= finish:
                winners.append(t.color)

    print('Список победителей:')
    for winner in winners:
        print(color_dict[winner])


if __name__ == '__main__':
    while True:
        print('--------------------------------------')
        start_game()
        input('Чтобы начать игру заново нажми <Enter>')
