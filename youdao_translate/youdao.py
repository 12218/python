import execjs
import hashlib
import requests

class translate:
    def __init__(self):
        super().__init__()
        self.r_js = '''
            function get_code() {
                r = "" + (new Date).getTime();
                return r;
            }
        '''
        self.i_js = '''
            function get_code(r) {
                i = r + parseInt(10 * Math.random(), 10);
                return i;
            }
        '''
        self.lts = ''
        self.salt = ''
        self.sign = ''
        self.bv = ''

    def product_code(self, word):
        resp_r = execjs.compile(self.r_js)
        r = resp_r.call('get_code') # 获取js代码里面r的值,即请求提交数据里面lts的值

        resp_i = execjs.compile(self.i_js)
        i = resp_i.call('get_code', r) # 获取js代码里面i的值,即请求提交数据里面salt的值

        print(r, i)

        string = "fanyideskweb" + word + str(i) + "]BjuETDhU)zqSxf-=B#7m"
        m = hashlib.md5()
        m.update(string.encode('utf-8')) # 使用md5码加密,获取请求提交数据里面sign的值

        print(m.hexdigest())

        t_string = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
        t = hashlib.md5()
        t.update(t_string.encode('utf-8')) # 使用md5码加密,获取js代码里面t的值;即请求提交数据里面bv的值

        print(t.hexdigest())

        # return r, i, m.hexdigest(), t.hexdigest()
        self.lts = r
        self.salt = i
        self.sign = m.hexdigest()
        self.bv = t.hexdigest()

    def get_dict(self, word):
        cookies = {
            'OUTFOX_SEARCH_USER_ID': '102171286@182.116.195.120',
            '_ntes_nnid': '6f128fc005892dceb127064b19c37b4c,1584184329500',
            'OUTFOX_SEARCH_USER_ID_NCOO': '413571387.0777992',
            'UM_distinctid': '171796b3b2d827-0f16dcba377a4e-f313f6d-1fa400-171796b3b2e831',
            'JSESSIONID': 'aaaFQ8dY4x4ED6gK9Ptpx',
            'DICT_UGC': 'be3af0da19b5c5e6aa4e17bd8d90b28a|',
            # '___rl__test__cookies': '1596984913055',
        }

        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

        params = (
            ('smartresult', ['dict', 'rule']),
        )

        data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': self.salt,
        'sign': self.sign,
        'lts': self.lts,
        'bv': self.bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
        }

        response = requests.post('http://fanyi.youdao.com/translate_o', headers=headers, params=params, cookies=cookies, data=data, verify=False)
        print(response.json())

        return response.json()

if __name__ == "__main__":
    dictionary = translate()
    word = input('Word: ')
    dictionary.product_code(word)
    dictionary.get_dict(word)