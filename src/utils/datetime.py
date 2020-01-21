import datetime
import time

def run_script():
    print(__name__)
    print(__file__)

    datetime_example()
    time_example()
    # usecase_backup()

def datetime_example():
    now = datetime.datetime.now()
    # 2020-01-21 04:13:42.552337
    print(now)

    # 2020-01-21T04:13:42.552337
    print(now.isoformat())

    # 21/01/20-041342552337
    print(now.strftime('%d/%m/%y-%H%M%S%f'))

    today = datetime.date.today()
    # 2020-01-21
    print(today)

    # 2020-01-21
    print(today.isoformat())

    # 21/01/20
    print(today.strftime('%d/%m/%y'))

    t = datetime.time(hour=1, minute=10, second=5, microsecond=100)

    # 01:10:05.000100
    print(t)

    # 01:10:05.000100
    print(t.isoformat())

    # 01_10_05_000100
    print(t.strftime('%H_%M_%S_%f'))

    # 1週間前
    d = datetime.timedelta(weeks=1)
    print(now - d)

    # 日本時間
    # JSTとUTCの差分
    DIFF_JST_FROM_UTC = 9
    now = datetime.datetime.utcnow() \
          + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
    print(now)


def time_example():
    # エポック秒(UNIX時間)
    print(time.time())

    print('#####')
    time.sleep(1)
    print('1second')
    time.sleep(1)
    print('2second')


def usecase_backup():
    # 日時をファイル名に付加してバックアップを作成
    import os
    import shutil

    DIFF_JST_FROM_UTC = 9
    now = datetime.datetime.utcnow() \
          + datetime.timedelta(hours=DIFF_JST_FROM_UTC)

    file_name = 'files/test.txt'
    if os.path.exists(file_name):
        shutil.copy(file_name, "{}.{}".format(
            file_name, now.strftime('%Y_%m_%d_%H%M%S')
        ))

    with open(file_name, 'w') as f:
        f.write('test')


if __name__ == '__main__':
    run_script()