def run_script():
    print(__name__)
    print(__file__)
    # help
    # print(help(tuple))

    basics()
    methods()

def basics():
    t = (1, 2, 3, 1, 2)
    print(t)
    print(type(t))
    print(t[1])
    # print(t[0]=5) エラー
    print(t[2:5])
    print(t)

    t = ([1, 2, 3], [4, 5, 6])
    print(t)
    print(t[0][0])
    t[0][0] = 2
    print(t)

    t = 1,  # ,がつくとアプルになる
    print(t)
    print(type(t))

    t = (1)
    print(t)
    print(type(t))

    # アンパッキング(展開)
    num_tuple = (10, 20)
    print(num_tuple)
    x, y = num_tuple
    print(x, y)
    min, max = 0, 100
    print(min, max)

    #入れ替えなどに使える
    a, b = 1, 2
    print(a, b)
    a, b = b, a
    print(a, b)

def methods():
    t = (1, 2, 3, 1, 2)
    print(t)
    print(type(t))
    print(t.index(2))
    print(t.index(2, 2))
    print(t.count(2))


if __name__ == '__main__':
    run_script()