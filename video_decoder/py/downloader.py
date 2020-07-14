import requests

# 错误代码
'''
申请错误 100
'''

'''url = 'https://cdn.yangju.vip/kc/api.php?url='
film = 'https://www.iqiyi.com/v_19rqpjhlz0.html'

html = requests.get(url + film)
print(html.json())

print(html.json()['url'])
m3u8_url = html.json()['url']

print('https://www.m3u8play.com/?play=' + m3u8_url)
# webbrowser.open('https://www.m3u8play.com/?play=' + m3u8_url)'''

class download:
    def __init__(self, error, film_url):
        super().__init__()
        self.error = error
        self.film_url = film_url # 从外部传入的url(电影url)
        self.m3u8_url = ''
        self.url_1 = 'https://cdn.yangju.vip/kc/api.php?url=' # 线路一url
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    def Down_1(self):
        try:
            html = requests.get(self.url_1 + self.film_url, headers = self.headers)
            self.m3u8_url = html.json()['url']
            print(self.m3u8_url)
            # return m3u8_url
        except:
            self.error = '100'
            print('Error Code is 100')

if __name__ == "__main__":
    film = download('0', 'https://www.iqiyi.com/v_19rqpjhlz0.html')
    film.Down_1()
    print(film.m3u8_url)