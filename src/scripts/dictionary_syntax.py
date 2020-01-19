def run_script():
    print(__name__)
    print(__file__)
    # help
    # print(help(dict))

    basics()
    methods()

def basics():
    d = {'x': 10, 'y': 20}
    print(d)
    print(type(d))
    print(d['x'])

    d['x'] = 100
    print(d)

    d['x'] = 'abc'
    print(d)
    d[1] = 1000
    print(d)

    d = dict(a=10, b=20)
    print(d)

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


def methods():
    d = dict(a=10, b=20)
    print(d)
    # keys
    print('keys')
    print(d.keys())
    # values
    print('values')
    print(d.values())

    # get
    print('get')
    print(d.get('a'))
    print(d)

    # pop
    print('pop')
    print(d.pop('a'))
    print(d)

    # del
    print('del')
    del d['b']
    print(d)

    # update
    print('update')
    d1 = {'x': 10, 'y': 20}
    print(d1)
    d2 = {'x': 15, 'z': 30}
    print(d2)
    d1.update(d2)
    print(d1)

    # clear
    print('clear')
    d1.clear()
    print(d1)
    d1 = {'x': 10, 'y': 20}

    # in
    print('in')
    print('x' in d1)# keyを見る
    print(10 in d1.values())

    # 単純な代入
    print('単純な代入')
    d1 = d2
    print(d1)
    print(d2)
    print(id(d1))
    print(id(d2))
    d1['x'] = 30
    print(d1)
    print(d2)

    # copy
    print('copy')
    d1 = {}
    d2 = {'x': 15, 'y': 30}
    d1 = d2.copy()
    print(d1)
    print(d2)
    print(id(d1))
    print(id(d2))
    d1['x'] = 30
    print(d1)
    print(d2)