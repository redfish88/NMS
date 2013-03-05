#! D:/python2.7/python.exe
# coding:utf-8


import web,json,os
from   datetime    import datetime,date
from   config  	   import config
from   decimal 	   import Decimal

db 	     = config.db
render   = config.render

class register(object):
	"""docstring for register"""
	def POST(self):
		pass
	def GET(self):
		return render.register()


