import re
"""
https://docs.python.org/ja/3/library/re.html
match()  文字列の先頭で正規表現とマッチするか調べる
search()　文字列を操作して、正規表現がどこにマッチするか調べる
findall()　正規表現にマッチする部分文字列を全て探し出しリストとして返す
finditr()　重複しないマッチオブジェクトのイテレータを返す
"""
AWS_ID_1 = 'arn:aws:cloudformation:us-east-2:123456789012:stack/mystack' \
      '-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786'

AWS_ID_2 = 'arn:aws:cloudformation:us-east-1:769876452978:stack/mystack' \
      '-mynestedstack-lakjhsdlfkjha/987345bn9er-b969-11e0-a185-98y3959yhjbi'

RE_STACK_ID = re.compile(r"""
                arn:aws:cloudformation:
                (?P<region>[\w-]+):             # region
                (?P<account_id>[\d]+)           # account_id
                :stack/
                (?P<stack_name>[\w-]+/[\w-]+)   # stack_name
                """, re.VERBOSE)

def run_script():
    match()
    # search()
    # find_all()
    # find_iter()
    # check_aws_id()
    # re_sprit()
    # re_sub()
    # to_hex()


def match():
    # (ドット) デフォルトのモードでは改行以外の任意の文字にマッチします。
    # DOTALL フラグが指定されていれば改行も含む全ての文字にマッチします。
    # m = re.match('a.c', 'abc')

    # 直前の正規表現を 0 回か 1 回繰り返したものにマッチさせる結果の正規表現にします。
    # 例えば ab? は 'a' あるいは 'ab' にマッチします
    # m = re.match('ab?', 'abb')

    # 直前の正規表現を 0 回以上、できるだけ多く繰り返したものにマッチさせる結果の正規表現にします。
    # 例えば ab* は 'a'、'ab'、または 'a' に任意個数の 'b' を続けたものにマッチします。
    # m = re.match('ab*', 'abb')

    # 直前の正規表現を 0 回以上、できるだけ多く繰り返したものにマッチさせる結果の正規表現にします。
    # 例えば ab* は 'a'、'ab'、または 'a' に任意個数の 'b' を続けたものにマッチします。
    # m = re.match('ab+', 'abbb')

    # 直前の正規表現をちょうど m 回繰り返したものにマッチさせるよう指定します。
    # それより少ないマッチでは正規表現全体がマッチしません。
    # 例えば、 a{6} は 6 個ちょうどの 'a' 文字にマッチしますが、 5 個ではマッチしません。
    # m = re.match('a{6}', 'aaaaaa')

    # 直前の正規表現を m 回から n 回、できるだけ多く繰り返したものにマッチさせる結果の正規表現にします。
    # 例えば、a{3,5} は、3 個から 5 個の 'a' 文字にマッチします。
    # m を省略すると下限は 0 に指定され、n を省略すると上限は無限に指定されます。
    # 例として、 a{4,}b は 'aaaab' や、1,000 個の 'a' 文字に 'b' が続いたものにマッチしますが、
    # 'aaab' にはマッチしません。コンマは省略できません、
    # 省略すると修飾子が上で述べた形式と混同されてしまうからです。
    # m = re.match('a{2,4}', 'aaaaaa')

    # []文字の集合を指定するのに使います。集合の中では:
    # 文字を個別に指定できます。 [amk] は 'a' 、 'm' または 'k' にマッチします。
    # m = re.match('[a-c]', 'a')
    # m = re.match('[a-zA-Z]', 'J')
    # m = re.match('[a-zA-Z0-9]', '5')
    # m = re.match('[a-zA-Z0-9_]', '_')
    # m = re.match('\w', '_') #　[a-zA-Z0-9_]と同じ
    # m = re.match('[^a-zA-Z0-9_]', '@')# [a-zA-Z0-9_]と以外
    # m = re.match('\W', '@')  # [a-zA-Z0-9_]と同じ
    # m = re.match('[0-9]', '5')
    # m = re.match('\d', '5')
    # m = re.match('[^0-9]', 'a')
    # m = re.match('\D', 'a') # [^0-9]と同じ
    # m = re.match('a|b', 'a')
    # m = re.match('(abc)', 'abcabc')
    # m = re.match('(abc)+', 'abcabcacb')
    # m = re.match('\s', ' ') # スペース
    # m = re.match('\S', '1')  # スペース以外
    # *, ?, + など正規表現で使用する文字列はエスケープが必要
    m =re.match('\+', '+')
    print(m)
    print(m.group())

    s = '<html><head><title>Title</title></head></html>'

    print(re.match('<.*>', s)) # Greedy
    print(re.match('<.*?>', s))

def search():
    # m =re.search('a.c', 'test aac test abc')
    # m = re.search('^abc', 'abc test aac test ab') # 先頭をチェックする場合
    m = re.search('abc$', 'test aac test abc')  # 末尾をチェックする場合

    print(m)
    print(m.span())
    print(m.group())

def find_all():
    m = re.findall('a.c', 'test aac test abc')
    print(m)

def find_iter():
    m = re.finditer('a.c', 'test aac test abc')
    print(m)
    # for w in m:
    #     print(w.group())
    print([w.group() for w in m])


def check_aws_id():
    # m = re.match(r'arn:aws:cloudformation:(?P<region>[\w-]+):'
    #              r'(?P<account_id>[\d]+):stack/(?P<stack_name>[\w-]+/[\w-]+)',
    #              AWS_ID_2)

    for id in [AWS_ID_1, AWS_ID_2]:
        m = RE_STACK_ID.match(id)
        if m:
            print('go next')
            print(m)
            print(m.group())
            print('region : {}'.format(m.group('region')))
            print('account_id : {}'.format(m.group('account_id')))
            print('stack_name : {}'.format(m.group('stack_name')))
        else:
            raise Exception('Error!')

def re_sprit():
    s = 'My name is ... Mike'
    print(s.split(sep=' '))

    p = re.compile(r'\W+')
    print(p.split(s))

def re_sub():
    p = re.compile('(blue|white|red)')
    print(p.sub('color', 'blue socks and red shoes')) # blue, white,
    # red を colorに置換
    print(p.sub('color', 'blue socks and red shoes', count=1)) # 1つ目だけ置換
    print(p.subn('color', 'blue socks and red shoes')) # 置換した数をタプルに追加

##########

def hexrepl(match):
    value = int(match.group())
    return hex(value)

def to_hex():
    p = re.compile(r'\d')
    print(p.sub(hexrepl, '2345 23452 34 test test2'))

##########


if __name__ == '__main__':
    run_script()
