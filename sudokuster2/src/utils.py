from math import floor

def round_to_multiple(number, multiple):
    return multiple * floor(number / multiple)
