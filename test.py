import requests

'''
r = requests.get("http://0.0.0.0:9090/api/v2/identity")
print r.json()['returncode']
print len(r.json()['data'])

payload = {"name":"testin"}
r = requests.post("http://0.0.0.0:9090/api/v2/identity", params=payload)
print r.json()['returncode']
print r.json()


payload = {"name":"testin"}
r = requests.put("http://0.0.0.0:9090/api/v2/identity", params=payload)
print r.json()['returncode']
#print r.json()
print len(r.json()['data'])
'''
'''
print "CREATE SEARCH"
payload = {"distant": True, "search_string": "ASDASDASD"}
r = requests.post("http://0.0.0.0:9090/api/v2/filesearch/create_search", params=payload)
print r.json()['returncode']
print r.json()
r.json()['data']



print "\nGET SEARCH"
r = requests.get("http://0.0.0.0:9090/api/v2/filesearch")
print r.json()['returncode']
print r.json()
print len(r.json()['data'])


print "\nOWN ID"
r = requests.get("http://0.0.0.0:9090/api/v2/identity/own")
print r.json()['returncode']
print r.json()


print "\nCREATE ID"
payload = {"name":"testin"}
r = requests.post("http://0.0.0.0:9090/api/v2/identity", params=payload)
print r.json()['returncode']
print r.json()

r = requests.post("http://0.0.0.0:9090/api/v2/identity?name=testin")
print r.json()['returncode']
print r.json()

payload = {"name":"testin"}
r = requests.put("http://0.0.0.0:9090/api/v2/identity", params=payload)
print r.json()['returncode']
print len(r.json())
'''

print "\nFORUM"
print "own groups"
fid = 0
fname = ""
r = requests.put("http://0.0.0.0:9090/api/v2/forums")
for f in r.json()['data']:
	if f['own']:
		print f
		fid = f['id']
		fname = f['name']
print fid

print "\n messages in " + fname + "("+fid+")"
r = requests.put("http://0.0.0.0:9090/api/v2/forums/"+fid)
print r.json()['data']



