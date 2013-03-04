#!D:\python2.7\python.exe
# coding:utf-8
import web,os

#数据库连接配置
#openshift数据库
#db = web.database(host='127.5.120.129',dbn='mysql',db='hy',user='admin',pw='NBNlVY1ZFEha')
db = web.database(host='127.0.0.1',dbn='mysql',db='news',user='root',pw='admin')
#render 配置
root = os.path.dirname(__file__)
render = web.template.render(os.path.join(root,'..','templates/'))

config = web.storage(
	static = '/static'
	)

web.template.Template.globals['render'] = render
web.template.Template.globals['config'] = config




