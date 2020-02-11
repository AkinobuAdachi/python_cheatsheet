import json
import os

def run_script():
    j = {
        "employee":
            [
                {"id": 111, "name": "Mike"},
                {"id": 222, "name": "Nancy"}
            ]
    }

    print(j)
    print('**********************')
    a =json.dumps(j)
    print(a)
    print('**********************')
    print(json.loads(a))


    if not os.path.exists('files/test.json'):
        import pathlib
        pathlib.Path('files/test.json').touch()

    # ファイル書き込み
    with open('files/test.json', 'w') as f:
        json.dump(j, f)

    print('**********************')
    # ファイル読み込み
    with open('files/test.json', 'r') as f:
        print(json.load(f))


if __name__ == '__main__':
    run_script()