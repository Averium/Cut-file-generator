from generator import Generator as gen, movement


@movement("P5_S.dat", "DECK_END_SIDE_VIEW")
def side_view():

    gen.move(228, 0)
    gen.move(0, 16)
    gen.move(-228, 0)
    gen.move(0, -16)


@movement("P5_T.dat", "DECK_END_TOP_VIEW")
def top_view():

    gen.move(228, 0)
    gen.move(0, 12)
    gen.move(-228, 0)
    gen.move(0, -12)


@movement("P5_F.dat", "DECK_END_FRONT_VIEW")
def front_view():

    gen.move(12, 0)
    gen.move(0, 16)
    gen.move(-12, 0)
    gen.move(0, -16)