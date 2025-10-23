import urllib.request
def getbaidu():
    url = 'http://www.baidu.com'
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    return content
content = getbaidu()
print(content)

