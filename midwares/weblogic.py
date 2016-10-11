# encoding: utf-8
# author: 

def _login(_url, _user='weblogic', _pass='weblogic'):
	import requests
	url = _url + '/console/j_security_check'
	data = {"j_username":_user, "j_password":_pass}
	try:
		print data
		resp = requests.post(url=url, data=data, timeout=10)
		print resp.url
		if resp.url.endswith('LoginForm.jsp'):
			return (False, '')
		elif 'console.portal' in resp.url:
			return (True, '')
		else:
			return (None, '')
	except Exception as e:
		return (None, str(e))
