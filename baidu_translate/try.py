# 使用cURL生成的post请求
import requests

headers = {
    'authority': 'fanyi.baidu.com',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://fanyi.baidu.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://fanyi.baidu.com/translate',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': 'BAIDUID=D69D8ED032C2487D6130646A8140D288:FG=1; PSTM=1583502862; BIDUPSID=3FB5CEC450B662B26A7113BFF653E76B; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_WISE_SIDS=144367_144991_144338_140593_143922_144366_139908_142427_140367_145423_141911_144332_110085; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=J6M3lXdU00fkUwWGNGd0FwdUViMm05OFpobWNKbG56ejBRWGhobkt5TDRkVFpmRVFBQUFBJCQAAAAAAAAAAAEAAABHRPTnwO6yqsi7MTIyMTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjoDl~46A5fQ1; BDUSS_BFESS=J6M3lXdU00fkUwWGNGd0FwdUViMm05OFpobWNKbG56ejBRWGhobkt5TDRkVFpmRVFBQUFBJCQAAAAAAAAAAAEAAABHRPTnwO6yqsi7MTIyMTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjoDl~46A5fQ1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; H_PS_PSSID=32294_1450_32360_32328_31253_32046_32398_32404_31708_32504_32481; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1596673678,1596673921,1596683433,1596808304; yjs_js_security_passport=785b7109876831ff05b2c771f84e4cb7fb12a0d1_1596808441_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1596809314; __yjsv5_shitong=1.0_7_7842807c6bfb98c2460cbfe0c7f571301475_300_1596809314883_223.89.61.83_c038e8fc',
}

params = (
    ('from', 'en'),
    ('to', 'zh'),
)

data = {
  'from': 'en',
  'to': 'zh',
  'query': 'student',
  'simple_means_flag': '3',
  'sign': '767469.1005276',
  'token': '3b8f179dae36df22b8998c040cd35dc6',
  'domain': 'common'
}

response = requests.post('https://fanyi.baidu.com/v2transapi', headers=headers, params=params, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://fanyi.baidu.com/v2transapi?from=en&to=zh', headers=headers, data=data)
print(response.text)