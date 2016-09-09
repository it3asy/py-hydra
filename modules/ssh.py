# encoding: utf-8
# ssh login function
# author: 

def _login(_url, _user='', _pass=''):
	import paramiko, urlparse
	_up = urlparse.urlparse(_url)
	_netlocs = _up.netloc.split(':')
	_host = _netlocs[0]
	_port = int(_netlocs[1])
	_path = _up.path
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(_host,_port,_user,_pass)
		return (True,'')
	except paramiko.ssh_exception.AuthenticationException,e:
		return (False,str(e))
	except Exception as e:
		return (None,str(e))