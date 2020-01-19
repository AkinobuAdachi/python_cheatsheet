def run_script():
    print(__name__)
    print(__file__)

    values()
    printSyntax()
    number()

def values():
    '''
    #変数
    '''
    num: int = 1 #型は書けるが、型を固定するわけではない
    print('value: {}, type: {}'.format(num, type(num)))
    num = str(num)
    print('value: {}, type: {}'.format(num, type(num)))

    name = 'mike'
    print('value: {}, type: {}'.format(name, type(name)))

    isOK = True
    print('value: {}, type: {}'.format(isOK, type(isOK)))

def printSyntax():
    '''
    #print
    '''
    print('1', 'name', 'email', sep=", ", end='.\n')
    print('2', 'name', 'email', sep=", ")

def number():
    '''
    数値計算
    '''
    print('  =', )

    print('17 / 3  =', 17 / 3)
    print('17 // 3  =', 17 // 3)
    print('17 % 3  =', 17 % 3)

    #べき乗
    print('5 * 5 * 5 * 5 * 5  =', 5 * 5 * 5 * 5 * 5)
    print('5 ** 5 =', 5 ** 5)

    #丸め
    print('round(3.141592, 2) = ', round(3.141592, 2))

    #math
    import math
    # print(help(math))
    print('math.sqrt(25) = ', math.sqrt(25))
    print('math.log2(10) = ', math.log2(10))


if __name__ == '__main__':
    run_script()

