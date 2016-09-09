# encoding: utf-8
# mysql login function
# author: 

def _login(_url, _user='root', _pass=''):
	import MySQLdb,urlparse
	_up = urlparse.urlparse(_url)
	_netlocs = _up.netloc.split(':')
	_host = _netlocs[0]
	_port = int(_netlocs[1])
	_path = _up.path.strip('/')
	try:
		MySQLdb.connect(host=_host, port=_port, user=_user, passwd=_pass, db=_path, connect_timeout=30)
		return (True,'')
	except Exception as e:
		if 'Access denied' in str(e):
			return (False, str(e))
		else:
			return (None, str(e))