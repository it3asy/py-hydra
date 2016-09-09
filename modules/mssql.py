# encoding: utf-8
# mysql login function
# author: 


def _login(_url, _user='sa', _pass=''):
	import pymssql,urlparse
	_up = urlparse.urlparse(_url)
	_netlocs = _up.netloc.split(':')
	_host = _netlocs[0]
	_port = int(_netlocs[1])
	_path = _up.path.strip('/')
	_server = '%s:%s' % (_host,_port)
	try:
		pymssql.connect(server=_server, user=_user, password=_pass, database=_path)
		return (True, '')
	except Exception as e:
		if e[0][0] == 18456:
			return (False, e[0][1])
		else:
			return (None, e[0][1])
