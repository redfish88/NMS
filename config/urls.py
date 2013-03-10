#!D:\python2.7\python.exe
# coding:utf-8

pre_fix = 'controllers.controllers.'

urls = (
	'/'	,					pre_fix + 'Index',
	'/register',			pre_fix + 'register',
	'/sign',				pre_fix + 'Sign',
	'/post',				pre_fix + 'post',
	'/new',					pre_fix + 'New',
	'/view/(\d+)',			pre_fix + 'View',
	'/edit/(\d+)',			pre_fix + 'Edit',
	'/logout',				pre_fix + 'Logout',
	'/vote_post',			pre_fix + 'Vote',
	'/mypost',				pre_fix + 'Mypost',
	)
