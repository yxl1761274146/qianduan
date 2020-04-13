import random
import requests
import time

#url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
#content="我和你"

class Youdao():
    def __init__(self,content):
        self.content=content
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts = self.get_ts()
        self.salt = self.get_salt()
        self.sign = self.get_sign()


    def get_salt(self):
        s=str(random.randint(0,10))
        t=self.ts
        #print("random= ",s)
        #print("ts= ",t)
        #print("salt= ",t+s)
        return  t+s
        #return '15865238351685'

    def get_md5(self,value):
        import hashlib
        m =hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        i=self.salt
        e=self.content
        s="fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        #print("s=",s," md5=",get_md5(s))
        return self.get_md5(s)
        #return  '3193a8a41b35c7008754488154d2c1aa'

    def get_ts(self):
        t = time.time()
        ts=str(int(round(t * 1000)))
        print("ts=",ts)
        return ts
        # '1586523835168'

    #def get_content(self):
    #   return content

    def yield_form_data(self):
        form_data={
            'i': self.content(),
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': 'f0ece28f714caaf3c6cee92884b1a685',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        return form_data

    def get_headers(self):
        headers={
            'Cookie':'OUTFOX_SEARCH_USER_ID=197877919@10.108.160.18; JSESSIONID=aaa-1EcV6hVDE9DsYSIfx; OUTFOX_SEARCH_USER_ID_NCOO=196562409'
            'Referer: http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36'
        }
        return headers

    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        return response.text

if __name__ == '__main__':
    # ts=get_ts()
    #print(form_data)
    #print(get_headers())
    youdao=Youdao('我们')
    print(youdao.fanyi())