#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	#return HttpResponse(u"欢迎来到SJ.Lee的避风港!")
	stringWelcome = "欢迎来到SJ.Lee的避风港@!"
	strMenu = ["主页","关于我","生活日记","工作心得","留言簿"]
	strMenu2 = {u"主页":u"/home",u"关于我":u"/aboutMe",u"生活日记":u"/lifeDiary"
		,u"工作心得":u"/aboutWork",u"留言簿":u"/guestbook"}
	strContract = {'TelPhone':u'18952367310','EMail':u'SJ.Lee@outlook.com'}
	return render(request,'home.html'
		,{'strWelcome':stringWelcome,'strMenu':strMenu,'strContract':strContract,'strMenu2':strMenu2})

def aboutMe(request):
	stringWelcome = "欢迎来到SJ.Lee的避风港@!"
	strMenu = ["主页","关于我","生活日记","工作心得","留言簿"]
	strMenu2 = {u"主页":u"/home",u"关于我":u"/aboutMe",u"生活日记":u"/lifeDiary",u"工作心得":u"/aboutWork",u"留言簿":u"/guestbook"}
	strContract = {'TelPhone':u'18952367310','EMail':u'SJ.Lee@outlook.com'}
	return render(request,'aboutme.html'
		,{'strWelcome':stringWelcome,'strMenu':strMenu,'strContract':strContract,'strMenu2':strMenu2})

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a)+int(b)
	return HttpResponse(str(c))

def add2(request,a,b):
	c = int(a)+int(b)
	return HttpResponse(str(c))