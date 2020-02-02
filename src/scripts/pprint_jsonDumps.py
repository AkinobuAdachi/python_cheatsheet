import json
import pprint
from urllib.request import urlopen

def run_script():
    with urlopen('https://pypi.python.org/pypi/Twisted/json') as responce:
        http_info = responce.info()
        print(responce.info()['Content-Type'])
        # responce.info().get_content_charset()が取れない
        # raw_data = responce.read().decode(responce.info().get_content_charset())
        raw_data = responce.read().decode('utf-8')

    project_info = json.loads(raw_data)
    # pprint.pprint(project_info, width=50)
    print(json.dumps(project_info, indent=4))



if __name__ == '__main__':
    run_script()