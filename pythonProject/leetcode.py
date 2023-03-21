import math

def addDigits(num: int) -> int:
    if num == 1:
        return True
    x = math.log(num, 2) %2

    if x == 0:
        return True
    return False

if (16 & 15):
    print(False)