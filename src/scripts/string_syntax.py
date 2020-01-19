def run_script():
    print(__name__)
    print(__file__)

    basecs()
    methods()
    assignment()

def basecs():
    # エスケープ
    print('I don\'t know')
    # 改行
    print('Hello.\nHow are you.')
    # raw string(windowsのpathとか)
    print(r'C:\number\name')
    print("""\
line1
line2
line3\
    """)
    print('Hi.' * 3)
    prefix = 'dev'
    print(prefix + str.title('python'))
    print('aaaaaa'
          'bbbbbb')
    word = 'python'
    print('word = '+ word)
    print('word[0] = ' + word[0])
    print('word[1] = ' + word[1])
    print('word[-1] = ' + word[-1])
    # スライス
    print('word[0:2] = ' + word[0:2])
    print('word[:2] = ' + word[:2])
    print('word[2:5] = ' + word[2:5])
    print('word[2:] = ' + word[2:])
    # print('word[100] = ' + word[100])
    # print(word[0] = 'j')
    word = 'j' + word[1:]
    print(word)
    # len()
    print('len(word) = ' + str(len(word)))

def methods():
    s = 'My name is Mike. Hi Mike.'
    print('s = ' + s)
    # startswith
    print('s.startswith(\'My\') = ' + str(s.startswith('My')))
    # find
    print("s.find('Mike') = " + str(s.find('Mike')))
    # rfind
    print("s.rfind('Mike') = " + str(s.rfind('Mike')))
    # count
    print("s.count('Mike') = " + str(s.count('Mike')))
    # capitalize
    print('s.capitalize() = ' + s.capitalize())
    # title
    print('s.title() = ' + s.title())
    # upper
    print('s.upper() = ' + s.upper())
    # lower
    print('s.lower() = ' + s.lower())
    # replace
    print("s.replace('Mike', 'Nancy') = " + s.replace('Mike', 'Nancy'))
    # join
    l = ['My', 'name', 'is', 'Mike']
    print('l = {}'.format(l))
    print("' '.join(l) = {}".format(' '.join(l)))

def assignment():
    print('a is {} {} {}'.format(1, 2, 3))
    print('a is {2} {1} {0}'.format(1, 2, 3))
    print('My name is {name} {family}. 私の名前は{family} {name}です。\
          '.format(name='Akinobu', family='Adachi' ))

    # f-string
    print('***** f-string *****')
    x, y, z = 1, 2, 3
    print(f'a is {x}, {y}, {z}')
    name = 'Akinobu'
    family = 'Adachi'
    print(f'My name is {name} {family}. 私の名前は{family} {name}です。')

if __name__ == '__main__':
    run_script()