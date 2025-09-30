from generator import Generator as gen, movement


@movement("P1_S.dat", "BODY_END_SIDE_VIEW")
def side_view():

    gen.move(196, 0)
    gen.move(0, 72)
    gen.move(-190, 0)
    gen.move(0, -16)
    gen.move(-6, 0)
    gen.move_home()


@movement("P1_T.dat", "BODY_END_TOP_VIEW")
def top_view():

    large_angle = 15.922624739
    radius = 681.666667
    height = 60

    gen.move(6, 0)
    gen.circle_around(6, radius, large_angle, 40)
    x, y = gen.position

    gen.circle_to(x, height - y, 4, 8)

    gen.circle_around(6, 60-radius, large_angle, 40)

    gen.move(-6, 0)
    gen.move_home()


@movement("P1_F.dat", "BODY_END_FRONT_VIEW")
def front_view():

    gen.move(44, 0)
    gen.circle_around(44, 28, 90, 25)
    gen.move_to(72, 32)
    gen.circle_around(44, 32, 90, 25)
    gen.move_to(0, 60)
    gen.move_home()
