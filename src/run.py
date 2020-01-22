import sys
from optparse import OptionParser

from flask import Flask
from flask import render_template
from flask import request
import sqlite3



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

from tests import doc_test_example


# Flask routing
app = Flask(__name__)


@app.route('/')
def top_page():
    return 'this is top page.'


@app.route('/next')
def next_page():
    return 'this is next page.'


@app.route('/<query_param>')
def user(query_param):
    return 'query_param : {}'.format(query_param)


# @app.route('/index')
# def index():
#     return render_template('index_template.html', title='index',
#                            contents='this is template')

@app.route('/index')
@app.route('/index/<username>')
def greeting(username=None):
    return render_template('index_template.html', title='index',
                           contents='this is template', username=username)


@app.route('/method/post', methods=['POST', 'PUT', 'DELETE'])
def show_post():
    return str(request.values)

def main():
    '''
    # python組み込み関数
    https://docs.python.org/ja/3.7/library/functions.html
    # Python 標準ライブラリ
    https://docs.python.org/ja/3.7/library/index.html
    # PyPi
    https://pypi.org/
    # Flask
    https://a2c.bitbucket.io/flask/
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
    # configparser.run_script()

    # test
    c = doc_test_example.Cal()
    print(c.add_num_and_double(1, 1))

    # Flask (terminal で python run.py しないとダメ。なんでだろ。)
    # app.debug = True
    # app.run(host='0.0.0.0', port='5000')


if __name__ == '__main__':
    main()
