from generator import Generator as gen, movement


@movement("P2_S.dat", "BODY_CENTER_SIDE_VIEW")
def side_view():

    gen.move(136, 0)
    gen.move(0, 56)
    gen.move(-136, 0)
    gen.move_home()


@movement("P2_T.dat", "BODY_CENTER_TOP_VIEW")
def top_view():

    gen.move(136, 0)
    gen.move(0, 60)
    gen.move(-136, 0)
    gen.move_home()


@movement("P2_F.dat", "BODY_CENTER_FRONT_VIEW")
def front_view():

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
    gen.move_home()
