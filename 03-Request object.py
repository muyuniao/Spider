import urllib.request

from Tools.scripts.generate_opcode_h import header

url = "http://www.google.com.hk/search?q=%E8%8E%B1%E6%98%82%E7%BA%B3%E5%A4%9A"
headers = {"user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
urllib.request.urlretrieve(url,'page.html')

