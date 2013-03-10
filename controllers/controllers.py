#! D:/python2.7/python.exe
# coding:utf-8

import hashlib
import web,json,os
from   datetime    import datetime,date
from   config  	   import config
from   decimal 	   import Decimal

db 	     = config.db
render   = config.render
session  = web.config.get('_session')

def get_by_id(tb,id):
	result	= db.select(tb,where='id=$id',vars=locals())
	if not result:
		return False
	return result[0]


class register(object):
	"""docstring for register"""
	def POST(self):
		tb = 'user'
		user = web.input()
		username = user.username
		passwd 	 = user.password
		result = db.select(tb,where='username=$username',vars=locals())

		if not result:
			db.insert(tb,username=username,passwd=hashlib.md5(passwd).hexdigest(),createtime=datetime.now())
			session.loggedin = True
			session.user 	 = username
			return web.seeother('/')
		return render.error("该账号已被注册",'/register')
	def GET(self):
		return render.register()

#index
class Index(object):
	def POST(self):
		pass
	def GET(self):
		news_list = db.select('news_post',where='status=1',order='post_time desc')
		return render.index(news_list)


#登录
class Sign(object):
	"""docstring for sign"""
	def POST(self):
		tb = 'user'
		user = web.input()
		username = user.username
		passwd 	 = user.password
		pw = hashlib.md5(passwd).hexdigest()
		check = db.query('select * from user where username=$username and passwd=$pw',vars=locals())
		if not check:
			return render.signin('用户名或密码错误',username)
		else:
			session.loggedin = True
			session.user 	 = username
			return web.seeother('/')
		
	def GET(self):
		return render.signin('','')

class New(object):

	def POST(self):
		if not session.loggedin:
			return render.signin('','')
		news = web.input()
		username = session.user
		news_id = db.insert('news_post',title=news.title,author=username,content=news.content,type=news.type,status=news.status,post_time=datetime.now())
		raise web.seeother('/view/%d' % news_id)
	def GET(self):
		if not session.loggedin:
			return render.signin('','')
		else:
			return render.new()
class View(object):
	def GET(self,id):
		print id
	 	entry = get_by_id('news_post',id)
	 	return render.view(entry)
	def POST(self,id):
		pass
class Edit(object):
	def GET(self,id):
		entry = get_by_id('news_post',id)
		if not session.loggedin:
			return render.signin('','')
		elif session.user != entry.author:
			return render.error("您登陆已超时或没有权限编辑该文!")
		else:
			return render.edit(entry)
	def POST(self,id):
		update_entry = web.input()
		entry = get_by_id('news_post',id)
		if not session.loggedin:
			return render.signin('','')
		elif session.user != entry.author:
			return render.error("您登陆已超时或没有权限编辑该文!")
		else:
			db.update('news_post',where='id=$id',title=update_entry.title,\
					 content=update_entry.content,\
					 type=update_entry.type,\
					 status=update_entry.status,\
					 post_time=datetime.now(),\
					 update_time=datetime.now(),vars=locals())
			raise web.seeother("/view/%d" % int(id))	

class Logout(object):
	def POST(self):
		pass
	def GET(self):
		session.kill()
		raise web.seeother('/')
class Vote(object):
	"""docstring for Vote"""
	def GET(self):
		entry = web.input()
		post_id = entry.post_id 
		print post_id
		vote =  db.select('vote',where='news_id=$post_id',vars=locals()).list()
		web.header('Content-Type','application/json')
		return json.dumps(vote)
	def POST(self):
		new_vote = web.input()
		vote_list =  db.select('vote',where='news_id=$new_vote.post_id',vars=locals())
		if not vote_list:
			if new_vote.type == 'top':
				db.insert('vote',news_id=new_vote.post_id,top=1)
			else:
				db.insert('vote',news_id=new_vote.post_id,stamp=1)
		else:
			vote = vote_list[0]
			if new_vote.type == 'top':
				db.update('vote',where='news_id=$new_vote.post_id',top=vote.top+1,vars=locals())
			else:
				db.update('vote',where='news_id=$new_vote.post_id',stamp=vote.stamp+1,vars=locals())
		web.header('Content-Type','application/plain')
		return "success"
				
class Mypost(object):
	"""docstring for Mypost"""
	def GET(self):
		if session.loggedin:
			username = session.user
			news_list = db.select('news_post',where='status=1 and author=$username',order='post_time desc',vars=locals())
			return render.index(news_list)
		else:
			raise web.seeother("/")
			
	def POST(self):
		pass
		

