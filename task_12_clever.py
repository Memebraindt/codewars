from itertools import product

BUTTONS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')


def get_pins(observed):
    return ["".join(p) for p in product(*(BUTTONS[int(d)] for d in observed))]
