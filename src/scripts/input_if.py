def run_script():
    print(__name__)
    print(__file__)
    print(help(input))

    basics()


def basics():
    num = input('>>>')
    num = int(num)
    if num > 0:
        print('positive')
    elif num == 0:
        print('zero')
    else:
        print('negative')


if __name__ == '__main__':
    run_script()