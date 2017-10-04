import requests
from bs4 import BeautifulSoup as bs
import os


base_url='https://www.github.com/'
def following(base_url):
	pageNo=1
	print 'loading...'
	FollowReqlist=[0]
	ansArr=[]
	while len(FollowReqlist)>0:
		tab='?page='+str(pageNo)+'&tab=following' #implement other tabs
		url=base_url+user+tab
		getResult=requests.get(url)
		soup=bs(getResult.text,'html.parser')
		FollowReqlist=soup.findAll('a',{'class':'d-inline-block'})
		# print len(FollowReqlist)
		for i in FollowReqlist:
			ansArr.append('id: '+i.attrs['href'][1:]+',\tname: '+i.find('span').text)
		pageNo+=1
	os.system('clear')
	print 'github id of ppl followed by enter user are:'
	for i in ansArr:
		print str(ansArr.index(i)+1)+'.',i
	a=raw_input()



def repo(base_url):
	pageNo=1
	print 'loading...'
	Repolist=[0]
	ansArr=[]
	while len(Repolist)>0:
		tab='?page='+str(pageNo)+'&tab=repositories' #implement other tabs
		url=base_url+user+tab
		soup=bs(requests.get(url).text,'html.parser')
		if soup.find('div',{'class':'blankslate'}):
			# print 'breaking'
			break
		RepoList=soup.findAll('div',{'class':'d-inline-block'})
		for repo in RepoList:
			try:
				str1=repo.find('a').attrs['href']
				ansArr.append('Repo name :\t'+str1)
				# try:
				# 	str2=repo.find('span').text.strip()
				# 	ansArr.append(str1+' '+str2+' \n')
				# except:
				# 	ansArr.append(str1+'\n')
			except Exception as e:
				continue
		pageNo+=1

	os.system('clear')
	print "repositories of the entered user are:"
	for i in ansArr:
		print str(ansArr.index(i)+1)+'.',i
	a=raw_input()

def stars(base_url):
	pageNo=1
	print 'loading...'
	StarList=[0]
	ansArr=[]
	while len(StarList)>0:
		tab='?page='+str(pageNo)+'&tab=stars'
		url=base_url+user+tab
		soup=bs(requests.get(url).text,'html.parser')
		if soup.find('div',{'class':'blankslate'}):
			print 'breaking'
			break
		StarList=soup.findAll('div',{'class':'d-inline-block'})
		for i in StarList:
			str1=i.find('a').attrs['href']
			if str1[0]=='/':
				ansArr.append('https://github.com'+str1)
		pageNo+=1
	os.system('clear')
	print 'the repositories starred by user are :'
	for i in ansArr:
		print str(ansArr.index(i)+1)+'.',i
	a=raw_input()

def followers(base_url):
	pageNo=1
	print 'loading...'
	FollowReqlist=[0]
	ansArr=[]
	while len(FollowReqlist)>0:
		tab='?page='+str(pageNo)+'&tab=followers' 
		url=base_url+user+tab
		soup=bs(requests.get(url).text,'html.parser')
		FollowReqlist=soup.findAll('a',{'class':'d-inline-block'})
		for i in FollowReqlist:
			ansArr.append('id: '+i.attrs['href'][1:]+',\tname: '+i.find('span').text)
		pageNo+=1
	os.system('clear')
	print 'github id of ppl following the user are:'
	for i in ansArr:
		print str(ansArr.index(i)+1)+'.',i	
	a=raw_input()

while True:
	user=raw_input('name of user(leave blank to exit): ') 
	if user=='':
		break
	while True:
		os.system('clear')

	# user='pratyush1687'
		print '''choose the option no:
			1.repositories
			2.stars
			3.Followers
			4.following
			press any other key to reenter user:P
		''' 
		a=raw_input()

		#if tab chosen ==e following
		if a=='4':
			following(base_url)
		elif a=='1':
			repo(base_url)
		elif a=='2':
			stars(base_url)
		elif a=='3':
			followers(base_url)	
		else:
			print 'please enter a valid choice'
			break
	