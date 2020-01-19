class UppercaseError(Exception):
    '''
    自作エラークラス
    '''
    pass

def run_script():
    '''
    https://docs.python.org/3/library/exceptions.html#exception-hierarchy
    :return:
    '''
    print(__name__)
    print(__file__)

    l = [1, 2, 3]
    i = 3

    # print(l[i])
    # del l
    try:
        print(l[i])
        # print(l + ())
    except IndexError as err:
        print('IndexError: {}'.format(err))
        # raise IndexError
    except NameError as err:
        print('NameError: {}'.format(err))
    except Exception as err:
        print('Exception: {}'.format(err))
    else:
        # tryの中が成功した時のみ
        print('success')
    finally:
        # キャッチできないエラーがあっても必ず実行される
        print('end')

    # 自作のエラーを発生させる
    def originalErrcheck():
        words = ['APPLE', 'orange', 'banana']
        for word in words:
            if word.isupper():
                raise  UppercaseError(word)

    try:
        originalErrcheck()
    except UppercaseError as err:
        print(err, 'is uppercase', UppercaseError.__doc__)


if __name__ == '__main__':
    run_script()