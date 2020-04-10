import random
import requests
import time

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
content="我和你"

def get_salt():
    s=str(random.randint(0,10))
    t=get_ts()
    #print("random= ",s)
    #print("ts= ",t)
    #print("salt ",t+s)
    return  t+s
    #return '15864988855634'

def get_md5(value):
    import hashlib
    m =hashlib.md5()
    m.update(value.encode("utf-8"))
    return m.hexdigest()

def get_sign():
    i=get_salt()
    e=get_content()
    s="fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
    print("s=",s," md5=",get_md5(s))
    return get_md5(s)
    return  '63ec4fac43e6d508ff508ab79a47cd11'

def get_ts():
    t = time.time()
    ts=str(int(round(t * 1000)))
    return ts
    # '1585615400595'

def get_content():
    return content


form_data={
    'i':'我和你',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': 'f0ece28f714caaf3c6cee92884b1a685',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
}

def get_headers():
    headers={
        'Cookie: OUTFOX_SEARCH_USER_ID=197877919@10.108.160.18; JSESSIONID=aaa-1EcV6hVDE9DsYSIfx; OUTFOX_SEARCH_USER_ID_NCOO=196562409'
        'Referer: http://fanyi.youdao.com/',
        'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36'
    }
    return headers

class Youdao():
    def __init__(self):
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign-self.get_sign()


if __name__ == '__main__':
    # ts=get_ts
    print(form_data)
    print(get_headers())
    response=requests.post(url,data=form_data,headers=get_headers())
    print(response.text)