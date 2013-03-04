#!D:\python2.7\python.exe

# coding:utf-8

__version__  = '0.1'
__author__   = 'lvrenkun'

import sys,web,json,os
from   datetime    import datetime,date
from   config  	   import config
from   config.urls import urls
from   decimal 	   import Decimal
app_root = os.path.dirname(__file__)

sys.path.append(app_root)
os.chdir(app_root) 

db 	     = config.db
render   = config.render


if __name__ == '__main__':
	app = web.application(urls,globals())
	app.run()