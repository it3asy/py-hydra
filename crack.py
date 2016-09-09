#coding: utf-8

import optparse
import urlparse
import Queue
import threading
import sys,os,inspect

ROOT_DIR = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())))
DICT_DIR = ROOT_DIR + '/dict/'
sys.path.append(ROOT_DIR+'/modules')


class BruteModel(object):
	def __init__(self, target_url, options):
		self.target_url = target_url
		self.options = options
		self.cracked = []
		self.error = ''
		self.scheme = urlparse.urlparse(self.target_url).scheme
		try:
			self._login_ex = getattr(__import__(self.scheme), '_login')
		except:
			self.error = "load module %s error" % self.scheme

	def _debug(self, s, level):
		if level <= self.options._debug_level:
			x = 32 + level
			print '\033[0;%s;40m' % x + '  ' * (level-1) + '- %s' % s + '\033[0m'

	def _brute_force(self):
		_users = list()
		_passes = list()
		if not self.options._login == None:
			_users.append(self.options._login)
		else:
			file = DICT_DIR + self.options._login_dict
			with open(file) as f:
				for line in f:
					i = line.strip()
					if i:
						_users.append(i)
		if not self.options._pass == None:
			_passes.append(self.options._pass)
		else:
			file = DICT_DIR + self.options._pass_dict
			with open(file) as f:
				for line in f:
					i = line.strip()
					if i:
						_passes.append(i)

		for u in _users:
			for p in _passes:
				_user = u
				_pass = p
				_pass = _pass.replace('%user%', _user)
				_pass = _pass.replace('%null%', '')

				r = self._login(_user=_user,_pass=_pass)
				self._debug('%s/%s, %s' % (_user,_pass, r[0]), 2)
	
				if r[0] == True:
					self.cracked.append((_user,_pass))
					break

				self._debug('%s' % r[1], 3)

			if self.cracked:
				if self.options._greedy == None:
					break

	def _login(self, _user, _pass):
		return self._login_ex(self.target_url, _user, _pass)

	def _check(self):
		r = self._login(_user='invalid',_pass='invalid')
		if r[0] == None:
			return False
		elif r[0] == False:
			return True
		elif r[0] == True: # 匿名访问,以后处理.
			return True
		else:
			return False


	def _run(self):
		self._debug('cracking %s' % self.target_url, 0)
		if self.error != "":
			self._debug(self.error, 1)
		elif self._check():
			self._brute_force()
		else:
			self._debug('remote service invalid or not brutable',1)


def bruteforce(url,options):
	bm = BruteModel(url, options)
	bm._run()
	return bm.cracked


if __name__ == '__main__':
	parser = optparse.OptionParser('usage: %prog [options] service_url')
	parser.add_option('-t', metavar = 'THREAD NUMS', dest='_threads_num', default=1, type='int', help='Number of threads. default=1')
	parser.add_option('-l', metavar='LOGIN', dest='_login', default=None, type='string', help='login with LOGIN name')
	parser.add_option('-p', metavar='PASS', dest='_pass', default=None, type='string', help='try password PASS')
	parser.add_option('-L', metavar='FILE', dest='_login_dict', default='common_user', type='string', help='load several logins from FILE')
	parser.add_option('-P', metavar='FILE', dest='_pass_dict', default='common_pass', type='string', help='load several passwords from FILE')
	parser.add_option('--greedy', dest='_greedy', action="store_true", help='defalt False')
	parser.add_option('--debug', metavar='DEBUG', dest='_debug_level', default=1, type='int', help='debug info level, default 1')
	(options, args) = parser.parse_args()

	if len(args) < 1:
		parser.print_help()
		sys.exit(0)

	url = args[0]
	print bruteforce(url,options)

