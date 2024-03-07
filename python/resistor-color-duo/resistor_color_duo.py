from typing import List

RESISTOR_CONVERSIONS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def value(colors: List[str]):
    """
    :param colors: List[str] - the label on the resistor
    return: int - the resistance value of the resistor (in Ohms)
    """

    resistance = 0

    for color in colors[:2]:
        resistance = resistance * 10
        resistance += RESISTOR_CONVERSIONS[color]

    return resistance
