# encoding: utf-8
# author: 

def _login(_url, _user='root', _pass=''):
	import requests
	url = _url.strip('/') + '/index.php'
	
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 5.2; rv:49.0) Gecko/20100101 Firefox/49.0',
		'Content-Type': 'application/x-www-form-urlencoded'
	}
	_payload = 'pma_username=%s&pma_password=%s' % (_user, _pass)
	try:
		resp = requests.post(url=url, headers=header, data=_payload, timeout=20)
		if 'pma_username' in resp.content:
			return (False, '')
		elif 'main.php?token=' in resp.content:
			return (True, '')
		elif 'db_structure.php?' in resp.content:
			return (True, '')
		else:
			return (None, '')
	except Exception as e:
		return (None, str(e))
