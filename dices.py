#Turning Dice combination into points
def dice_points(a, b, c):
    if a == b and a == c:
        return 1000
    if a == 1:
        a = 100
    elif a == 5:
        a = 50
    else:
        a = 0
    if b == 1:
        b = 100
    elif b == 5:
        b = 50
    else:
        b = 0
    if c == 1:
        c = 100
    elif c == 5:
        c = 50
    else:
        c = 0
    return a + b + c

#Calling Dice sides
def dice_side(x):
    if x == 1:
        one()
    elif x == 2:
        two()
    elif x == 3:
        three()
    elif x == 4:
        four()
    elif x == 5:
        five()
    else:
        six()


def one():
    print(' -------')
    print('|       |')
    print('|   *   |')
    print('|       |')
    print(' -------')

def two():
    print(' -------')
    print('| *     |')
    print('|       |')
    print('|     * |')
    print(' -------')

def three():
    print(' -------')
    print('| *     |')
    print('|   *   |')
    print('|     * |')
    print(' -------')

def four():
    print(' -------')
    print('| *   * |')
    print('|       |')
    print('| *   * |')
    print(' -------')

def five():
    print(' -------')
    print('| *   * |')
    print('|   *   |')
    print('| *   * |')
    print(' -------')

def six():
    print(' -------')
    print('| *   * |')
    print('| *   * |')
    print('| *   * |')
    print(' -------')
