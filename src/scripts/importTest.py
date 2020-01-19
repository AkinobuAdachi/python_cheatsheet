try:
    import test
except ImportError as err:
    # print(err)
    from dir2 import test

def run_script():
    print(__name__)
    print(__file__)


    test.test_func()
    print(test.__file__)


if __name__ == '__main__':
    run_script()