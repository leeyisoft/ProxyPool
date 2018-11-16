import requests
from proxypool.db import RedisClient

conn = RedisClient()

def set_proxy(proxy):
    result = conn.add(proxy)
    print(proxy)
    print('录入成功' if result else '录入失败')

# transfer int to ip
def long2ip(long):
    floor_list=[]
    yushu=long
    for i in reversed(range(4)):   #3,2,1,0
        res=divmod(yushu,256**i)
        floor_list.append(str(res[0]))
        yushu=res[1]
    return '.'.join(floor_list)

url = ''
response = requests.get(url)
li = response.text.split('\r\n')
for proxy in li:
    (ip,port)=proxy.split(':')
    proxy = '%s:%s' % (long2ip(int(ip)), port)
    print(proxy)
    set_proxy(proxy)
