def run_script():
    print(__name__)
    print(__file__)

    def say_something(word):
        print(word)

    say_something('hi')
    func = say_something
    func('hello')

    # *****************************
    def add(a, b):
        return a + b

    print(add(3, 5))

    # *****************************
    def add_num(a: int , b: int) -> int:
        return a + b

    # エラー出ない
    print(add_num('a', 'b'))

    # *****************************
    # # キーワード引数
    def menu(entree, drink, dessert):
        print('entree :', entree)
        print('drink :', drink)
        print('dessert :', dessert)

    # 並び順は関係なくなる
    menu(drink='beer', dessert='ice', entree='beef')

    # *****************************
    # デフォルト引数
    def menu_def(entree='beef', drink="beer", dessert='ice'):
        print('entree :', entree)
        print('drink :', drink)
        print('dessert :', dessert)

    # 渡してない引数はデフォルト引数が使用される
    menu_def(drink='wine')

    ###############################
    # デフォルト引数注意
    # デフォルト引数に空のリストやディクショナリーを設定しない
    # 同じアドレスが繰り返し使用されるので、バグになる
    def menu_def2(x, l=None):
        if l is None:
            l = []
        l.append(x)
        return l

    print(str(menu_def2(100, [1, 2, 3])))

    # *****************************
    # # 位置引数のタプル化
    # *をつけるとタプルを展開する
    def sample_func(*args):
        print(args)
        print(type(args))
        for arg in args:
            print(arg)

    sample_func('good','bad')

    # *****************************
    # キーワード引数の辞書化
    # **をつけると辞書を展開する
    def menu_kwargs(**kwargs):
        """
        キーワード引数の辞書化
        :param kwargs:
        :return:
        """
        print(kwargs)
        print(type(kwargs))
        for k, v in kwargs.items():
            print(k,':', v)

    menu_kwargs(entree='checken', drink='coffee')


    d = {
        'entree': 'fish',
        'drink': 'wine',
        'dessert': 'ice'
    }

    menu_kwargs(**d)

    # doc, help
    print(menu_kwargs.__doc__)
    print(help(menu_kwargs()))

    # *****************************
    # 関数内に関数定義
    def outer(a, b):

        def add(c, d):
            return c + d

        return add(a, b)

    print(outer(3, 4))

    # *****************************
    # クロージャ closure
    def circle_area_func(pi):
        def circle_area(radius):
            return pi * radius ** 2
        return circle_area

    # この時点では実行されない
    f = circle_area_func(3.14)

    print('******')

    # ここで実行
    print(f(10))

    # *****************************
    # デコレータ decorator
    def add_start_end(func):
        def wrapper(*args, **kwargs):
            print('start')
            result = func(*args, **kwargs)
            print('end')
            return result

        return wrapper

    def showFuncInfo(func):
        def wrapper(*args, **kwargs):
            print('func:', func.__name__)
            print('args:', args)
            print('kwargs:', kwargs)
            result = func(*args, **kwargs)
            print(result)
            return result

        return wrapper

    @add_start_end
    @showFuncInfo
    def add_num(a, b):
        return a + b

    print(add_num(1, 2))

    # 以下と同じ
    # f = add_start_end(showFuncInfo(add_num))
    # print(f(1, 2))

    # *****************************
    # ラムダ lambda
    # func =　lambda 引数 : 戻り値 　
    l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

    # ***********************************************
    # def sample_func(word):
    #     return word.capitalize()
    #
    # def change_words(words, func=sample_func):
    #     for word in words:
    #         print(func(word))
    # ***********************************************

    # 　上記同様の事を、lambdaでかくと
    # ***********************************************
    # def change_words(words, func=lambda word: word.capitalize()):
    #     for word in words:
    #         print(func(word))
    #
    # change_words(l)
    # ***********************************************

    def change_words(words, func):
        for word in words:
            print(func(word))

    change_words(l, lambda word: word.capitalize())
    change_words(l, lambda word: word.lower())



if __name__ == '__main__':
    run_script()