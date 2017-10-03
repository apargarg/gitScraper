import requests
from bs4 import BeautifulSoup as bs
import os


base_url='https://www.github.com/'

while True:
	os.system('clear')
	user=raw_input('name of user')
# user='pratyush1687'
	print '''choose the option no:
		1.repositories
		2.stars
		3.Followers
		4.following
		press any other key for exit:P
	''' 
	a=input()

	#if tab chosen ==following
	if a==4:
		tab='?tab=following' #implement other tabs
		url=base_url+user+tab
		soup=bs(requests.get(url).text,'html.parser')
		FollowReqlist=soup.findAll('a',{'class':'d-inline-block'})
		print 'github id of ppl followed by enter user are:'
		for i in FollowReqlist:
			print 'id:',i.attrs['href'][1:],',name:',i.find('span').text
		a=raw_input()
	elif a==1:
		tab='?tab=repositories' #implement other tabs
		url=base_url+user+tab
		soup=bs(requests.get(url).text,'html.parser')
		RepoList=soup.findAll('div',{'class':'d-inline-block'})
		print "repositories of the entered user are:"
		for repo in RepoList:
			try:
				str1=repo.find('a').attrs['href']
				try:
					str2=repo.find('span').text.strip()
					print str1,str2,'\n'
				except:
					print str1+'\n'
			except Exception as e:
				continue
		a=raw_input()

	elif a==2:
		tab='?tab=stars'
		url=base_url+user+tab
		soup=bs(requests.get(url).text,'html.parser')
		StarList=soup.findAll('div',{'class':'d-inline-block'})
		print 'the repositories starred by user are :'
		for i in StarList:
			str1=i.find('a').attrs['href']
			if str1[0]=='/':
				print 'https://github.com'+str1
		a=raw_input()
	
	elif a==3:
		tab='?tab=followers' #implement other tabs
		url=base_url+user+tab
		soup=bs(requests.get(url).text,'html.parser')
		FollowReqlist=soup.findAll('a',{'class':'d-inline-block'})
		print 'github id of ppl following the user are:'
		for i in FollowReqlist:
			print 'id:',i.attrs['href'][1:],',name:',i.find('span').text
		a=raw_input()
	
	else:
		print 'please enter a valid choice'
		break
