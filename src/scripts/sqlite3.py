import sqlite3
import os


def run_script():
    if (os.path.exists('db') & os.path.isdir('db')) == False:
        os.mkdir('db')

    # if os.path.exists('db/test_sqlite.db') == False:
    # connection = sqlite3.connect('db/test_sqlite.db')
    connection = sqlite3.connect(':memory:')

    cursor = connection.cursor()

    cursor.execute(
        'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
    connection.commit()

    cursor.execute(
        'INSERT INTO persons(name) values("Mike")'
    )
    cursor.execute(
        'INSERT INTO persons(name) values("Nancy")'
    )
    cursor.execute(
        'INSERT INTO persons(name) values("Jun")'
    )

    # cursor.execute('UPDATE persons set name="Michel" where name="Mike"')

    # cursor.execute('DELETE from persons where id > 1')
    connection.commit()



    cursor.execute('SELECT * from persons')
    print(cursor.fetchall())

    cursor.close()
    connection.close()


if __name__ == '__main__':
    run_script()