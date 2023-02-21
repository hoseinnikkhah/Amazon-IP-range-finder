import json
from urllib.request import urlopen
url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
response = urlopen(url)
data = json.loads(response.read())
array = []
for i in data['prefixes']:
    array = [i['ip_prefix'] for i in data['prefixes']]
f_path = (r"ip.txt")
with open (f_path ,'w') as d:
       for lang in array:
        d.write("{}\n".format(lang))

for j in data['ipv6_prefixes']:
    array = [j['ipv6_prefix'] for j in data['ipv6_prefixes']]
f_path = (r"ipv6.txt")
with open (f_path ,'w') as c:
       for lang in array:
        c.write("{}\n".format(lang))

response.close()
