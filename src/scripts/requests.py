import requests

payload = {'key1': 'value1', 'key2': 'value2'}

def run_script():
    get()
    # post()
    # put()
    # delete()

def get():
    r = requests.get('http://httpbin.org/get', params=payload, timeout=1)
    print(r.status_code)
    print(r.text)
    print(r.json())


def post():
    r = requests.post('http://httpbin.org/post', data=payload)
    print(r.status_code)
    print(r.text)
    print(r.json())


def put():
    r = requests.put('http://httpbin.org/put', data=payload)
    print(r.status_code)
    print(r.text)
    print(r.json())


def delete():
    r = requests.delete('http://httpbin.org/delete', data=payload)
    print(r.status_code)
    print(r.text)
    print(r.json())




if __name__ == '__main__':
    run_script()