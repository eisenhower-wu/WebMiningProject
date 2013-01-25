import bs4
import urllib ,urlparse
import string

path="/home/wyh/w/project/html/"
path1="/home/wyh/w/project/fix_html/"
ff=open("/home/wyh/w/project/url.txt")
f1=open("/home/wyh/w/project/name.txt","w")
ff1=open("/home/wyh/w/project/parse.txt","w")
cnt=1
while True:
	line=ff.readline()
	if not line:
		break
	line=line.strip("\n")
	
	urltmp=line
	url= urllib.urlopen(urltmp)
	try:
		print urltmp
	except:
		pass
	soup= bs4.BeautifulSoup(url)
	try:
		f1.write(str(cnt).encode('utf-8')+'.   '+urltmp.encode('utf-8')+'        title:'+soup.title.string.encode('utf-8')+'\n')
	except:
		pass
	parse=urlparse.urlparse(urltmp)
	try:
		ff1.write(str(cnt)+'.   '+urltmp+'\n')
		ff1.write('scheme='+parse.scheme+', netloc='+parse.netloc+', path='+parse.path+', params='+parse.params+', query='+parse.query+', fragment='+parse.fragment)
	except:
		pass
	try:
		ff1.write('\n')
	except:
		pass
	f2=open(path+str(cnt)+".html",'w')
	try:
		f2.write(soup.encode("utf-8"))
	except:
		pass
	f2.close()
	f3=open(path1+"fix_"+str(cnt)+".html","w")
	try:
		ans=soup.prettify().encode("utf-8")
	except:
		pass
	try:
		f3.write(ans)
	except:
		pass
	f3.close()
	cnt+=1

ff.close()
f1.close()
ff1.close()



