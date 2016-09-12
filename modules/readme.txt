模板:
--------
def _login(_url, _user='', _pass=''):
	"""
	_url = 服务名://主机:端口/路径，示例:
		mysql://127.0.0.1:3306/mysql
		ssh://127.0.0.1:22
	"""
	if 登录成功:
		return (True,'')
	elif 帐号密码错误 as e:
		return (False, str(e))
	else 其它错误异常 as e:
		return (None, str(e))


注意：
--------
1) 单线程工具，不能阻塞!!!
  - 比如MySQLdb的connect函数不设置timeout时，如果远程主机不返回结果，登录函数将阻塞。
