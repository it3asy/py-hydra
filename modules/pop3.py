# encoding: utf-8
# pop3 login function
# author: 

def _login(_url, _user='', _pass=''):
	import poplib,urlparse
	_up = urlparse.urlparse(_url)
	_netlocs = _up.netloc.split(':')
	_host = _netlocs[0]
	_port = int(_netlocs[1])
	_path = _up.path
	try:
		Mailbox = poplib.POP3(_host, _port)
		Mailbox.user(_user) 
		Mailbox.pass_(_pass)
		Mailbox.quit()
		return (True,'')
	except poplib.error_proto,e:
		return (False,str(e))
	except Exception as e:
		return (None,str(e))