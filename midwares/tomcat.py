# encoding: utf-8
# author: 

def _login(_url, _user='weblogic', _pass='weblogic'):
	import requests,base64
	url = _url + '/manager/html'
	auth = base64.b64encode('%s:%s' % (_user,_pass))
	header = {'Authorization': 'Basic %s' % auth}
	try:
		resp = requests.get(url=url, headers=header, timeout=10)
		if resp.status_code == 401:
			return (False,'')
		elif resp.status_code == 200:
			if 'Tomcat Web Application Manager' in resp.content:
				return (True, '')
			else:
				return (None, '')
		else:
			return (None, '')
	except Exception as e:
		return (None, str(e))