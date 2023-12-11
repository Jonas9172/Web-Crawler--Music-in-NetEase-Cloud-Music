import requests
import json

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'referer': 'https://music.163.com/'
    }

data = {
    'params': '2hwSx/aDVhhrpmzBRmo0aTzKNH7q0VQuEZIV2HIKthOo4VQi5K5UuXkE0L9eBcAAZMddto3WdA1bipvCAmvrrz/9jTORANOlojKTK0QIn/9bJR9j7hlntpGiMnaPtkhK9qxk7FKrDvMu+Fc5yghEfg==',
    'encSecKey': '1da8dc388a6216d2827c23f02a1cbb0491717646fb2f0fcbdb133d15f0295bf594d7de0c46ab7945a525c4f687080c8d2a09b4d75267dc0f113320b3ce1dd5b99f45ac0b518546fdaca26b013fcbb4d999bbc9e915c7e583d9411b0cdf6d041978f75fb86b9b5f642ff2b1fb93702cbb7f6d7aed11aa49dfd4284165bcecd4d8'
    }

target_url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="

res = requests.post(target_url, headers=headers, data=data)

data_json = json.loads(res.text)

mp3_url = data_json['data'][0]['url']

mp3_content = requests.get(url=mp3_url).content

with open('163music.m4a', 'wb') as file:
    file.write(mp3_content)