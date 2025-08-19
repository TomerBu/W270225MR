def draw_square(size):
    if not isinstance(size, int):
        raise TypeError("Size must be an integer")
    if size <= 0:
        raise ValueError("Size must be a positive integer")

    # do the logic:
    for _ in range(size):
        print(size * "⬛️")


# test edge cases:
draw_square(11.1)
draw_square("ff")
draw_square(0)
draw_square(-3)