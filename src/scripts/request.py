"""
REST

HTTPメソッド　クライアントが行いたい処理をサーバーに伝える

GET    データの参照
POST   データの新規登録
PUT    データの更新
DELETE データの削除
"""
import urllib
import json

payload = {'key1': 'value1', 'key2': 'value2'}

def run_script():
    get()
    # post()
    # put()
    # delete()

def get():
    url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
    print(url)
    with urllib.request.urlopen(url) as f:
        resp = f.read()
        print('***********response***********')
        print(type(resp))
        print(resp)
        print('***********decode***********')
        decoded_resp = resp.decode('utf-8')
        print(type(decoded_resp))
        print(decoded_resp)
        print('***********json.loads***********')
        d = json.loads(decoded_resp)
        print(type(d))
        print(d)

def post():
    p = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request('http://httpbin.org/post', data=p,
                                 method='POST')
    with urllib.request.urlopen(req) as f:
        print(json.loads(f.read().decode('utf-8')))

def put():
    p = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request('http://httpbin.org/put', data=p,
                                 method='PUT')
    with urllib.request.urlopen(req) as f:
        print(json.loads(f.read().decode('utf-8')))

def delete():
    p = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request('http://httpbin.org/delete', data=p,
                                 method='DELETE')
    with urllib.request.urlopen(req) as f:
        print(json.loads(f.read().decode('utf-8')))


if __name__ == '__main__':
    run_script()