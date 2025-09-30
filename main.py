from generator import Generator as gen


def nose_cone_top():

    gen.begin("S1.txt", "ORR ELEM FELULROL")

    large_angle = 15.922624739
    radius = 681.666667
    height = 60

    gen.move(6, 0)
    gen.circle_around(6, radius, large_angle, 40)
    x, y = gen.position

    gen.circle_to(x, height - y, 4, 8)

    gen.circle_around(6, 60-radius, large_angle, 40)

    gen.move(-6, 0)
    gen.move_to(0, 0)

    gen.end()
    gen.plot()


def nose_cone_back():

    gen.begin("S2.txt", "ORR ELEM HATULROL JOBBRA DONTVE")

    gen.move(44, 0)
    gen.circle_around(44, 28, 90, 25)
    gen.move_to(72, 32)
    gen.circle_around(44, 32, 90, 25)
    gen.move_to(0, 60)
    gen.move_to(0, 0)
    gen.end()
    gen.plot()


def body_side():

    gen.begin("S3.txt", "TEST ELEM OLDALROL")

    gen.move(120, 0)
    gen.move(0, 56)
    gen.move(-120, 0)
    gen.move_to(0, 0)

    gen.end()
    gen.plot()


def body_back():

    gen.begin("S4.txt", "TEST ELEM HATULROL JOBBRA DONTVE")

    gen.move(28, 0)
    gen.circle(28, 28, 28, 25)
    gen.move(0, 4)
    gen.circle(-28, 28, 28, 25)
    gen.move(-28, 0)
    gen.move(0, -6)
    gen.move(28, 0)
    gen.circle(22, -22, 22, 20, -1)
    gen.move(0, -4)
    gen.circle(-22, -22, 22, 20, -1)
    gen.move(-28, 0)
    gen.move(0, -6)
    
    gen.end()
    gen.plot()


if __name__ == "__main__":
    nose_cone_top()
    nose_cone_back()
    body_side()
    body_back()
