import requests

username = 'anmolgupta'
s = requests.get('http://codeforces.com/api/user.status?handle=' + username).text

if s.find('"status":"FAILED"') != -1:
	print('Request failed')
else:
	print('No. of problems solved by ' + username + ': ' + str(s.count('"verdict":"OK"')))

