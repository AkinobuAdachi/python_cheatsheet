def run_script():
    print(__name__)
    print(__file__)

    # print(help(None))
    basecs()
    nullCheke()
    is_or_equal()

def basecs():
    print(True & True)
    print(True | False)
    print(True and True)
    print(True or False)

    a = 1
    b = 2

    if not a == b:
        print('not a == b')

    y = [1, 2, 3]
    x = 1
    if x in y:
        print('in')

    if 1000 not in y:
        print('not in')

    a = 1
    b = 2

    if not a == b:
        print('not a == b')

    # better
    if a != b:
        print('a != b')

    isOk = False
    if not isOk:
        print('isOk is False')

    isFoo = True
    isFoo = 1
    isFoo = -1
    isFoo = 0 # False
    isFoo = '' # False
    isFoo = 'bar'
    isFoo = [1, 2]
    isFoo = []  # False
    if isFoo:
        print('isFoo has value')
    else:
        print("isFoo doesn't have value")

def nullCheke():
    is_enpty = None
    print(is_enpty)

    if is_enpty is None:
        print('is_enpty is None')

    if is_enpty is not None:
        print('is_enpty is not None')

def is_or_equal():
    print(1 == True) # True
    print(1 is True) # False


if __name__ == '__main__':
    run_script()