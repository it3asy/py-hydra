		elif resp.status_code == 200:
			if 'Tomcat Web Application Manager' in resp.content:
				return (True, '')
			else:
				return (None, '')
		else:
			return (None, '')
	except Exception as e:
		return (None, str(e))