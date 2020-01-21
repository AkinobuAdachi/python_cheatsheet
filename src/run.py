import sys

from scripts import *
# from scripts import basics
# from scripts import string_syntax
# from scripts import list_syntax
# from scripts import tupule_syntax
# from scripts import dictionary_syntax
# from scripts import set_syntax
# from scripts import input_if
# from scripts import condition
# from scripts import loop
# from scripts import function
# from scripts import namespace
# from scripts import exception
# from scripts import importTest

# import same_dir


# コメントは上に書く

from classes import class01
from utils import file_utils
from utils import datetime
from utils import configparser


def main():
    '''
    # python組み込み関数
    https://docs.python.org/ja/3.7/library/functions.html
    # Python 標準ライブラリ
    https://docs.python.org/ja/3.7/library/index.html
    # PyPi
    https://pypi.org/
    '''
    print(sys.argv)
    # print(sys.path)
    # basics.run_script()

    # scripts
    # string_syntax.run_script()
    # list_syntax.run_script()
    # tupule_syntax.run_script()
    # dictionary_syntax.run_script()
    # set_syntax.run_script()
    # input_if.run_script()
    # condition.run_script()
    # loop.run_script()
    # function.run_script()
    # namespace.run_script()
    # exception.run_script()
    # importTest.run_script()
    # built_in_function.run_script()

    # classes
    # person_01 = class01.Person()
    # person_01.say_something()
    # del person_01
    #
    # class01.run_script()

    # utils
    # file_utils.run_script()
    # datetime.run_script()
    configparser.run_script()

if __name__ == '__main__':
    main()
