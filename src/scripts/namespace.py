value = 'foo'


def run_script():
    '''
    document text
    :return:
    '''
    print(__name__)
    print(__file__)

    # グローバル変数にアクセス
    # print(value)

    # # 同名の変数を作成が作成されてしまう
    # value = 'bar'
    # print('local : '  + value)
    global value
    value = 'biz'
    # print(value)
    # print('global:', globals())
    print('local : ', locals())
    print(run_script.__name__)
    print(run_script.__doc__)


if __name__ == '__main__':
    run_script()