from generator import Generator as gen, movement


@movement("P4_S.dat", "DECK_CENTER_SIDE_VIEW")
def side_view():

    gen.move(228, 0)
    gen.move(0, 16)
    gen.move(-228, 0)
    gen.move(0, -16)


@movement("P4_T.dat", "DECK_CENTER_TOP_VIEW")
def top_view():

    gen.move(228, 0)
    gen.move(0, 124)
    gen.move(-228, 0)
    gen.move(0, -124)


@movement("P4_F.dat", "DECK_CENTER_FRONT_VIEW")
def front_view():

    gen.move(124, 0)
    gen.move(0, 16)
    gen.move(-124, 0)
    gen.move(0, -16)