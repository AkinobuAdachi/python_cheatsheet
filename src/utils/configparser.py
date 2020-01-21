"""
[DEFAULT]
debug = False

[web_server]
host = 127.0.0.1
port = 80

[db_server]
host = 127.0.0.1
port = 3306
"""
import configparser

def run_script():
    print(__name__)
    print(__file__)

    # write_config()
    read_config()

def write_config():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'debug': True
    }
    config['web_server'] = {
        'host': '127.0.0.1',
        'port': 80
    }
    config['db_server'] = {
        'host': '127.0.0.1',
        'port': 3306
    }

    with open('config.ini', 'w') as config_file:
        config.write(config_file)

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    print(config['DEFAULT'])
    print(config['DEFAULT']['debug'])

    print(config['web_server'])
    print(config['web_server']['host'])
    print(config['web_server']['port'])

    print(config['db_server'])
    print(config['db_server']['host'])
    print(config['db_server']['port'])


if __name__ == '__main__':
    run_script()
