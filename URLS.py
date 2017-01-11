class Base:
	url = None
	uid = None
	pwd = None

class google(Base):
	url = 'https://www.google.com/'

class office365(Base):
	url = 'https://login.microsoftonline.com/'
	
class hotmail(Base):
	url = 'https://www.hotmail.com/'

class aws(Base):
	url =  'https://aws.amazon.com/'

class amazon(Base):
	url =  'https://www.amazon.com/'

class github(Base):
	url = 'https://github.com/login'

class youtube(Base):
	url =  'https://www.youtube.com/'
