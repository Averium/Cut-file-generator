from generator import Generator as gen, movement


@movement("P3_S.dat", "DECK_WINDOW_SIDE_VIEW")
def side_view():

    gen.move(124, 0)
    gen.move(0, 16)
    gen.move(-124, 0)
    gen.move(0, -16)


@movement("P3_T.dat", "DECK_WINDOW_TOP_VIEW")
def top_view():

    # begin from bottom-left corner
    gen.move(0, 30)
    gen.move(6, 0)

    # inner shape
    gen.move(0, -18)
    gen.circle(6, -6, 6, 6)
    gen.move(100, 0)
    gen.circle(6, 6, 6, 6)
    gen.move(0, 36)
    gen.circle(-6, 6, 6, 6)
    gen.move(-100, 0)
    gen.circle(-6, -6, 6, 6)
    gen.move(0, -18)

    # cut around
    gen.move(-6, 0)
    gen.move(0, 30)
    gen.move(124, 0)
    gen.move(0, -60)
    gen.move_home()

@movement("P3_F.dat", "DECK_WINDOW_SIDE_VIEW")
def front_view():

    gen.move(60, 0)
    gen.move(0, 16)
    gen.move(-60, 0)
    gen.move(0, -16)