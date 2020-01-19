import builtins


def run_script():
    '''
    https://docs.python.org/ja/3.7/library/functions.html
    '''
    print(__name__)
    print(__file__)

    # builtins.print(builtins.globals())
    # print(builtins.locals())

    exam_A = {
        'A': 100,
        'B': 85,
        'C': 95
    }
    print(exam_A.keys())
    print(exam_A.values())
    print(exam_A.get('A'))

    print(sorted(exam_A, key=exam_A.get, reverse=True))


if __name__ == '__main__':
    run_script()