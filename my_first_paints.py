# подключение библиотеки под синонимом gr
import graphics as gr

window = gr.GraphWin("My First Paint With Python", 400, 400)


def two_rectangle_blocks_for_background():
    """ Рисуем прямоугольник, у которого диагональ —
    отрезок с концами в точках (0, 0) и (400, 200) """
    first_rectangle_block = gr.Rectangle(gr.Point(0, 0), gr.Point(400, 200))
    first_rectangle_block.setFill('blue')
    first_rectangle_block.draw(window)

    """ Создание прямоугольника, у которого диагональ —
    отрезок с концами в точках (400, 200) и (400, 400) """
    second_rectangle_block = gr.Rectangle(gr.Point(400, 200), gr.Point(400, 400))
    second_rectangle_block.setFill('gray')
    second_rectangle_block.draw(window)


def sun():
    """ Рисуем солнце (круг) с радиусом 10 и координатами центра (50, 50) """
    circle_of_sun = gr.Circle(gr.Point(330, 60), 30)
    circle_of_sun.setFill('yellow')
    circle_of_sun.draw(window)


def clouds(x, y, size):
    """ Рисуем облака.

    Наивным решением будет написать сто почти одинаковых функций с измененными цифрами, но если мы вдруг внезапно захотим
    во всех этих обьектах убрать какой-либо примитив — нам придется залезть в каждую такую функцию и изменить соответствующие строчки.
    Такой подход нежизнеспособен.

    Рациональным выходом из подобной ситуации будет являться использование функций с параметрами. В физике положение обьекта
    мы задавали с помощью координат, почему бы такой подход не распространить и на графические обьекты? """
    circle_of_cloud = gr.Circle(gr.Point(x, y), size)
    circle_of_cloud.setFill('white')
    circle_of_cloud.setOutline('black')
    circle_of_cloud.draw(window)


def house():
    """ Рисуем дом (базу дома и крышу) """
    big_square_of_house = gr.Rectangle(gr.Point(120, 140), gr.Point(250, 280))
    big_square_of_house.setFill('dark gray')
    big_square_of_house.draw(window)

    roof_of_house = gr.Polygon(gr.Point(185, 70), gr.Point(120,140), gr.Point(250,140))
    roof_of_house.setFill('dark red')
    roof_of_house.draw(window)


def windows_of_house(a, b, c, d):
    """ Рисуем окна в доме """
    window_square_of_house = gr.Rectangle(gr.Point(a, b), gr.Point(c, d))
    window_square_of_house.setFill('yellow')
    window_square_of_house.setOutline('black')
    window_square_of_house.draw(window)


def fir_tree():
    """ Рисуем елку """
    bole_of_fir_tree = gr.Rectangle(gr.Point(320, 300), gr.Point(330, 330))
    bole_of_fir_tree.setFill('brown')
    bole_of_fir_tree.setOutline('black')
    bole_of_fir_tree.draw(window)

    first_stage_of_fir_tree = gr.Polygon(gr.Point(295, 300), gr.Point(315, 280), gr.Point(335, 280), gr.Point(355, 300))
    first_stage_of_fir_tree.setFill('green')
    first_stage_of_fir_tree.draw(window)

    second_stage_of_fir_tree = gr.Polygon(gr.Point(305, 280), gr.Point(320, 260), gr.Point(330, 260), gr.Point(345, 280))
    second_stage_of_fir_tree.setFill('green')
    second_stage_of_fir_tree.draw(window)

    third_stage_of_fir_tree = gr.Polygon(gr.Point(315, 260), gr.Point(325, 230), gr.Point(335, 260))
    third_stage_of_fir_tree.setFill('green')
    third_stage_of_fir_tree.draw(window)


#  Вызываем функции
def draw_angry_lecturer():
    two_rectangle_blocks_for_background()
    sun()
    clouds(70, 50, 20)
    clouds(90, 50, 20)
    clouds(60, 70, 20)
    clouds(80, 70, 20)
    clouds(100, 70, 20)
    house()
    windows_of_house(165, 170, 185, 190)
    windows_of_house(185, 170, 205, 190)
    windows_of_house(185, 190, 205, 210)
    windows_of_house(165, 190, 185, 210)
    fir_tree()


draw_angry_lecturer()


#  Ожидание нажатия кнопки мыши по окну.
window.getMouse()


#  После того как мы выполнили все нужные операции, окно следует закрыть.
window.close()