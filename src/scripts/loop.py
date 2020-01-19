def run_script():
    print(__name__)
    print(__file__)

    while_syntax()
    for_syntax()
    iter_syntax()
    generator_syntax()
    range_syntax()
    enumerate_syntax()
    zip_syntax()

def while_syntax():
    count = 0

    while count < 5:
        print(count)
        count += 1
    else:
        # breakで抜けた時は来ない
        print('done')

    count = 0
    while True:
        if count >= 5:
            break
        # 2をスキップ
        if count == 2:
            count +=1
            continue
        print(count)
        count += 1
    else:
        # breakで抜けた時は来ない
        print('done')


def for_syntax():
    list = ['a', 'b', 'c', 'd', 'e']

    for i in list:
        print(i)
    else:
        print('finish')

    for s in 'qwerty':
        print(s)
    else:
        print('finish')

    # dictionary for loop
    d = {'x': 100, 'y': 200}
    for k in d:
        print(k)

    print(d.items())

    for key, value in d.items():
        print(key, ':', value)

    # リスト内包表記
    print('************************')
    t = (1, 2, 3, 4, 5, 6)
    l = []

    # 内包表記を使用しない場合
    for i in t:
        if i % 2 == 0:
            l.append(i)

    print(l)

    # 内包表記を使用した場合
    print('************************')
    l = [i for i in t]

    print(l)

    l = [i for i in t if i % 2 == 0]

    print(l)

    # 辞書内包表記
    week = ['mon', 'tue', 'wed']
    food = ['coffee', 'milk', 'water']

    d = {}

    # 内包表記を使用しない場合
    for k, v in zip(week, food):
        d[k] = v
    print(d)

    # 内包表記を使用した場合
    d = {k: v for x, y in zip(week, food)}
    print(d)

    # 集合内包表記
    s = set()

    # 内包表記を使用しない場合
    for i in range(10):
        s.add(i)

    print(s)

    # 内包表記を使用した場合
    s = {i for i in range(10)}
    print(s)


def iter_syntax():
    # print(help(iter))
    list = ['z', 'x', 'c', 'v', 'b']
    iter_list = iter(list)
    print(next(iter_list))
    print(next(iter_list))
    print(next(iter_list))
    print(next(iter_list))
    print(next(iter_list))

def generator_syntax():
    # def counter(num):
    #     for i in range(num):
    #         yield i

    # 上記を内包表記にすると
    def counter(size):
        return (i for i in range(size))

    def daysGene():
        yield 'Mon'
        yield 'Tue'
        yield 'Wed'
        yield 'Thu'
        yield 'Fri'
        yield 'Sat'
        yield 'Sun'

    # for g in daysGene():
    #     print(g)
    g = daysGene()
    c = counter(7)
    print(next(g))
    print(next(c))
    print('#######')
    print(next(g))
    print(next(c))
    print('#######')
    print(next(g))
    print(next(c))
    print('#######')
    print(next(g))
    print(next(c))
    print('#######')
    print(next(g))
    print(next(c))
    print('#######')
    print(next(g))
    print(next(c))
    print('#######')
    print(next(g))
    print(next(c))



def range_syntax():
    # print(help(range))
    for i in range(1, 10, 2):
        print(i)

    # 使ってない変数は_にする
    for _ in range(10):
        print('hello')

    for i in range(10):
        print(f'{i} hello')


def enumerate_syntax():
    # print(help(enumerate))
    for i, fruit in enumerate(['apple', 'banana', 'orange']):
        print(i, fruit)


def zip_syntax():
    days = ['Mon', 'Tue', 'Wed']
    fruits = ['apple', 'banana', 'orange']
    drinks = ['coffee', 'tea', 'beer']

    for day, fruit, drink in zip(days, fruits, drinks):
        print(day, fruit, drink)




if __name__ == '__main__':
    run_script()