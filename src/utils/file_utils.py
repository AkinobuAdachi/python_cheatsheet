import string
import csv
import os
import pathlib
import shutil
import shutil
import glob

s = """\
AAA
BBB
CCC
DDD
"""


def run_script():
    print(__name__)
    print(__file__)

    # f_write()
    # f_write_with_statement()
    # f_read_all()
    # f_read_line()
    # f_read_chank()
    # f_read_seek()
    # f_write_and_read()
    # f_read_and_write()
    # read_template()
    # export_csv()
    # read_csv()
    file_operation()

# write
def f_write():
    f = open('files/test.txt', 'w')
    f.write('Test\n')
    print('My', 'name', 'is', 'Mike', file=f)
    f.close()

# with statement
def f_write_with_statement():
    with open('files/test.txt', 'w') as f:
        f.write(s)

# read
def f_read_all():
    with open('files/test.txt', 'r') as f:
        # ファイル全部を読む
        print(f.read())


# 一行づつ読む
def f_read_line():
    with open('files/test.txt', 'r') as f:
        while True:
            line = f.readline()
            print(line, end='')
            if not line:
                break


# チャンクごとに読む
def f_read_chank():
    with open('files/test.txt', 'r') as f:
        while True:
            chank = 2
            data = f.read(chank)
            print(data, end='\n')
            if not data:
                break

# seekで読み込み位置の移動
def f_read_seek():
    with open('files/test.txt', 'r') as f:
        print(f.tell())
        print(f.read(2))
        # print(f.tell())
        f.seek(2)
        print(f.tell())
        print(f.read(2))


# write and read
# 開いた時点でファイルの中身が消える
def f_write_and_read():
   with open('files/test.txt', 'w+') as f:
       f.write(s)
       # 頭に戻してから読む
       f.seek(0)
       print(f.read())


# read and write
# ファイルがないとエラーが出る
def f_read_and_write():
    with open('files/test.txt', 'r+') as f:
        text = f.read()
        print(text)
        f.seek(0)
        text += '\nEEE'
        f.write(text)


# templateにあるindex.htmlを読んで、内容を加える
def read_template():
    with open('template/index.html', 'r') as f:
        t = string.Template(f.read())
    contents = t.substitute(title='Top', contents='this is template.')
    print(contents)


# csvファイルを書き出し
def export_csv():
    with open('files/test.csv', 'w') as csv_file:
        fieldnames = ['name', 'count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'name': 'A', 'count': 1})
        writer.writerow({'name': 'B', 'count': 2})
        writer.writerow({'name': 'C', 'count': 3})
        writer.writerow({'name': 'D', 'count': 4})


def read_csv():
    with open('files/test.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['name'], row['count'])


def file_operation():
    # ファイルがあるか
    print(os.path.exists('files/test.csv')) # True
    print(os.path.exists('files')) # True
    # ファイルかどうか
    print(os.path.isfile('files/test.csv'))  # True
    print(os.path.isfile('files')) # False
    # ディレクトリかどうか
    print(os.path.isdir('files/test.csv')) # False
    print(os.path.isdir('files')) # True

    # rename
    # os.rename('files/rename_test.csv', 'files/rename_test_2.csv')
    # os.rename('files/rename_test_2.csv', 'files/rename_test.csv')

    # mkdir
    # os.mkdir('test_dir')

    # rmdir
    # os.rmdir('test_dir')

    # pathlib
    # 空のファイルを作る
    # pathlib.Path('files/empty.txt').touch()
    # os.remove('files/empty.txt')

    print(os.listdir('files'))
    # import glob
    print(glob.glob('files/*'))

    # ファイルコピー
    # import shutil
    shutil.copy('files/empty.txt', 'files/empty_copy.txt')

    # # ディレクトリとファイル生成
    # os.mkdir('files/test_dir')
    # pathlib.Path('files/test_dir/test.txt').touch()
    # shutil.copy('files/test_dir/test.txt', 'files/test_dir/test2.txt')
    # # ディレクトリごと削除
    # shutil.rmtree('files/test_dir')

    print(os.getcwd())


if __name__ == '__main__':
    run_script()
