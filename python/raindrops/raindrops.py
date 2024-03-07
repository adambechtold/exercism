from typing import NamedTuple

Conversion = NamedTuple("Conversion", [('divisor', int), ('text', str)])

def convert(number: int):

    """
    :param number: int - the number to convert into a string
    return: string - the string conversion of the number
    """

    conversion_map = [
        Conversion(3, "Pling"),
        Conversion(5, "Plang"),
        Conversion(7, "Plong")
    ]

    result = ""

    for conversion in conversion_map:
        if number % conversion.divisor == 0:
            result += conversion.text

    if result == '':
        return str(number)
    
    return result
