import urllib
import json
from encoder import Encoder
base_url="https://fanyi.baidu.com/sug"
data = {
    'kw':'spider'
}
headers = {
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0'
}
encoder=Encoder()
new_data = encoder.encode(data)
request = urllib.request.Request(base_url,new_data.encode(),headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(type(content))
#此时content为json类型
obj = json.loads(content)
print (obj)


