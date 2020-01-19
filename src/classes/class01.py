class Person(object):
    # コンストラクタ
    def __init__(self, age=1, name=None):
        self.name = name
        self.age = age
        print('this is constructor')
        if self.name is not None:
            print('I am {}.'.format(self.name))

    def __str__(self):
        return 'Person class'

    @ staticmethod
    def say_something():
        print('hello')

    def drive(self):
        try:
            if self.age >= 18:
                print('drive')
            else:
                raise Exception('no Drive')
        except Exception as err:
            print(err)

    # デストラクタ
    def __del__(self):
        print('good bye!')


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    @ staticmethod
    def ride(person):
        person.drive();


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 password=''):
        super().__init__(model)
        # _変数名 Protected クラス外からもアクセスできてしまう
        # __変数名　Private
        self.__enable_auto_run = enable_auto_run
        self.password = password

    # getter
    @property
    def enable_auto_run(self):
        return self.__enable_auto_run

    # setter
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        # パスワードで書き換え条件をつける
        try:
            if self.password == '123':
                self.__enable_auto_run = is_enable
            else:
                raise ValueError
        except ValueError:
            print('Err : password is not match')

    # オーバーライド
    def run(self):
        print('super fast')

    @ staticmethod
    def auto_run():
        print('auto run')


def run_script():
    print(__name__)
    print(__file__)

    # execute
    car = Car()
    car.run()
    adalt = Person(30)
    print(adalt.__str__())
    baby = Person(1)
    car.ride(adalt)
    car.ride(baby)

    print('***********')
    toyota_car = ToyotaCar('Lexus')
    print(toyota_car.model)
    toyota_car.run()

    print('***********')
    tesla_car = TeslaCar('Model X', password='13')
    print(tesla_car.model)
    tesla_car.enable_auto_run = True
    print('enable_auto_run: {}'.format(tesla_car.enable_auto_run))
    tesla_car.auto_run()
    tesla_car.run()


if __name__ == '__main__':
    run_script()
