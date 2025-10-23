import urllib.request
url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
request = urllib.request.Request()
#1.urlopen返回的类型为 http.client.HTTPResponse
print(type(response))
#2.
content = response.read()
print(type(content))
#3.
#4.
#5.
#6.
