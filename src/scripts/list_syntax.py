def run_script():
    print(__name__)
    print(__file__)
    # help
    # print(help(list))

    basics()
    methods()


def basics():
    l = ['11', '12', '13', '14', '15']

    print(l)
    print('l[0] = ' + l[0])
    print('l[1] = ' + l[1])
    print('l[-1] = ' + l[-1])
    print('l[0:2] = ' + str(l[0:2]))
    print('l[:2] = ' + str(l[:2]))
    print('l[2:5] = ' + str(l[2:5]))
    print('l[2:] = ' + str(l[2:]))
    print('l[:] = ' + str(l[:]))
    print('len(l) = ' + str(len(l)))
    print('type(l) = ' + str(type(l)))
    word = 'abcde'
    print('word = ' + word)
    print('list(word) = ' + str(list(word)))

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('l = ' + str(l))
    print('l[::2] = ' + str(l[::2]))
    print('l[1::2] = ' + str(l[1::2]))
    print('l[::-1] = ' + str(l[::-1]))

    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    l = [a, n]
    print('l = ' + str(l))
    print('l[0] = ' + str(l[0]))
    print('l[0][1] = ' + str(l[0][1]))

    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print('l = ' + str(l))

    l[0] = 'X'
    print('l[0] = "X"')
    print('l = ' + str(l))

    l[2:5] = ['C', 'D', 'E']
    print("l[2:5] = ['C', 'D', 'E']")
    print('l = ' + str(l))

    l[2:5] = []
    print("l[2:5] = []")
    print('l = ' + str(l))

    l[:] = []
    print("l[:] = []")
    print('l = ' + str(l))

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
    l = [i for i in t]

    print(l)

    l = [i for i in t if i % 2 == 0]

    print(l)


def methods():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('l = ' + str(l))

    # append
    l.append(100)
    print('l.append(100)')
    print('l = ' + str(l))

    # insert
    l.insert(0, 200)
    print('l.insert(0, 200)')
    print('l = ' + str(l))

    # pop
    print('l.pop() = ' + str(l.pop()))
    print('l = ' + str(l))

    print('l.pop(0) = ' + str(l.pop(0)))
    print('l = ' + str(l))

    # del
    del l[0]
    print('del l[0]')
    print('l = ' + str(l))
    print('del l とするとl自体が削除される')

    # remiove
    l.remove(5)
    print('l.remove(5)')
    print('l = ' + str(l))

    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9]
    print('a = ' + str(a))
    print('b = ' + str(b))
    a += b
    print('a += b')
    print('a = ' + str(a))

    # extends
    c = [1, 2, 3, 4, 5]
    d = [6, 7, 8, 9]
    print('c = ' + str(c))
    print('d = ' + str(d))
    c.extend(d)
    print('c.extend(d)')
    print('c = ' + str(c))

    # index
    l = [1, 2, 3, 4, 5, 1, 2, 3]
    print('l = ' + str(l))
    print('l.index(3) = '+ str(l.index(3)))
    print('l.index(3, 3) = ' + str(l.index(3, 3)))

    # count
    l = [1, 2, 3, 4, 5, 1, 2, 3]
    print('l = ' + str(l))
    print('l.count(3) = ' + str(l.count(3)))

    # in
    l = [1, 2, 3, 4, 5, 1, 2, 3]
    print('l = ' + str(l))
    print('5 in l = {}'.format(5 in l))
    print('7 in l = {}'.format(7 in l))

    # sort(元のリストが更新される)
    l = [1, 2, 3, 4, 5, 1, 2, 3]
    print('l = ' + str(l))
    l.sort()
    print('l.sort()')
    print('l = ' + str(l))
    l.sort(reverse=True)
    print('l.sort(reverse=True)')
    print('l = ' + str(l))

    # reverse(元のリストが更新される)
    l = [1, 2, 3, 4, 5, 1, 2, 3]
    print('l = ' + str(l))
    l.reverse()
    print('l = ' + str(l))

    s = 'My name is Mike'
    print('s = ' + s)
    print('s.split(' ') = {}'.format(s.split(' ')))

    #copy
    # copy不使用
    l1 = [1, 2, 3, 4, 5]
    l2 = l1
    print('l1= ' + str(l1))
    print('l2= ' + str(l2))
    print('id(l1) = {}'.format(id(l1)))
    print('id(l2) = {}'.format(id(l2)))
    l1[0] = 100
    print('l1[0] = 100')
    print('l1= ' + str(l1))
    print('l2= ' + str(l2))

    # copy使用
    l1 = [1, 2, 3, 4, 5]
    l2 = l1.copy()
    # 以下でも同様の動作
    # l2 = l1[:]
    print('l1= ' + str(l1))
    print('l2= ' + str(l2))
    print('id(l1) = {}'.format(id(l1)))
    print('id(l2) = {}'.format(id(l2)))
    l1[0] = 100
    print('l1[0] = 100')
    print('l1= ' + str(l1))
    print('l2= ' + str(l2))


if __name__ == '__main__':
    run_script()