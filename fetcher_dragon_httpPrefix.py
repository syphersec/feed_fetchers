import requests
import re
from pymemcache.client import Client

# User defined variables
feedaddr = 'http://www.dragonresearchgroup.org/insight/http-report.txt'
feedID = 'dragonhttp'
mkey = 'fetcher_dragon_httpPrefix:feeddata'
killchain = 'Reconnaissance'

# No user modifications needed below.
client = Client(('localhost', 11211))
result = client.get(mkey)

if isinstance(result, str):
	splitlines = result.split('\n')
else:
	r = requests.get(feedaddr)
	client.set(mkey, r.content, expire=7200)
	splitlines = r.content.split('\n')

print('ipv4prefix,feedID,killchain,description')

for x in splitlines:
	x = x.strip()
	if re.search('^#', x): continue
	if len(x) == 0: continue
	shortx = x[49:]
	shortx = shortx[:19]
	shortx = shortx.strip()
	print("%s,%s,%s" % (shortx, feedID, killchain, 'HTTP Probes'))
	
