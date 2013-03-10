#!D:\python2.7\python.exe

# coding:utf-8

__version__  = '0.1'
__author__   = 'lvrenkun'

import sys,web,json,os
from   datetime    import datetime,date
from   config      import config
from   config.urls import urls
from   decimal     import Decimal
#app_root = os.path.dirname(__file__)

#sys.path.append(app_root)
#os.chdir(app_root) 

db       = config.db
render   = config.render

app = web.application(urls,globals())
if web.config.get('_session') is None:
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(app, store, initializer={'loggedin': False,'login':0,'user':'anonymous'})
    web.config._session = session
else:
    session = web.config._session
config = web.storage(
    static = '/static',
    )

web.template.Template.globals['config'] = config
web.template.Template.globals['session'] = web.config.get('_session')
web.template.Template.globals['render'] = render
    
if __name__ == '__main__':
    app.run()