# encoding: utf-8
# ftp login function
# author: 

def _login(_url, _user='root', _pass=''):
	import urlparse,ftplib
	_up = urlparse.urlparse(_url)
	_netlocs = _up.netloc.split(':')
	_host = _netlocs[0]
	_port = int(_netlocs[1])
	_path = _up.path.strip('/')
	ftp=ftplib.FTP() 
	try:
		ftp.connect(_host,_port)
	except Exception as e:
		return (None, str(e))
	try:
		ftp.login(_user,_pass)
		return (True, '')
	except ftplib.error_perm as e:
		return (False, str(e))
	except Exception as e:
		return (None, str(e))