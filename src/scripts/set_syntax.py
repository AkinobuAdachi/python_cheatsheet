def run_script():
    print(__name__)
    print(__file__)
    # help
    # print(help(set))

    basics()
    methods()


def basics():
    a = {1, 2, 2, 3, 4, 4, 4, 5, 5, 6}
    print(type(a))
    print('a : {}'.format(a))
    b = {2, 2, 4, 6, 7}
    print('b : {}'.format(b))
    print('a - b = {}'.format(a - b))
    print('b - a = {}'.format(b - a))
    print('a & b = {}'.format(a & b))# 論理積
    # a + b ではない
    print('a | b = {}'.format(a | b))# 論理和
    print('a ^ b = {}'.format(a ^ b))# 排他的論理和

    # 集合内包表記
    s = set()

    # 内包表記を使用しない場合
    for i in range(10):
        s.add(i)

    print(s)

    # 内包表記を使用した場合
    s = {i for i in range(10)}
    print(s)



def methods():
    a = {1, 2, 2, 3, 4, 4, 4, 5, 5, 6}
    # add
    a.add(8)
    print(a)
    # remove
    a.remove(8)
    print(a)
    # clear
    a.clear()
    print(a)

    f = ['apple', 'banana', 'banana', 'orange']
    kind = set(f)
    print(kind)
