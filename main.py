print("Hello, World!")

#the point of this is to use a headless browser and/or to requests a series of documents
#lets start with a facebook login

#IMPORTS
import requests
import time

#INIT SESSION
print(dir(requests))
c = requests.Session()
headers = {"user_agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}

def writetofile(dat, num):
	print(dat)
	f=open("out" + str(num) + ".html", "w+")
	f.write(dat.content)
	f.close()

#OPEN FACEBOOK
dat = c.get("https://www.facebook.com", headers = headers)
writetofile(dat, 1)

#LOGIN
email = r"joshuajolly3@gmail.com"
pass_ = "Minecraft01"

data = {"email":email,"pass":pass_}

dat = c.post("https://www.facebook.com/login.php?login_attempt=1&lwv=110", headers = headers, data = data)
writetofile(dat, 2)

#GET MY PAGE
time.sleep(1)
dat = c.get("https://www.facebook.com/joshua.jolly.1238", headers = headers)
writetofile(dat, 3)

#GET TARGET'S PAGE
time.sleep(1)
dat = c.get("https://www.facebook.com/juanita.sprowell", headers = headers)
writetofile(dat, 4)

#GET MESSAGES
time.sleep(1)
dat = c.get("https://www.facebook.com/messages/t/100000176732853", headers = headers)
writetofile(dat, 5)

#GET OTHER MESSAGES
user_id = 100000176732853
message_limit = 20

data = """messages[user_ids][100000176732853][offset]=0
	&messages[user_ids][100000176732853][limit]=20
	&messages[user_ids][100000176732853][timestamp]
	&client=mercury
	&__user=100008183341012&__a=1
	&__dyn=7AzkXh8OAcjxd2u6aOGeFxqewRAKGgS8zAS-C2u6oqwWhE98nwgUaqG2yaBxebkwy6UnGi7VXDG4XzErz8iGt0TyKum4UpxSLGqu58nVUkzaxbxm1iyECcBxi48hxGbwYxyq-5pZ1G6XDxx4yplzEly8myEbt5xq498lBVpEcm8ypUhKHw
	&__af=iw&__req=17&__be=-1&__pc=PHASED%3ADEFAULT&__rev=2865362
	&fb_dtsg=AQFbG2C9c977%3AAQEmJLBD7pEk&ttstamp=265817098715067579957555558658169109747666685511269107"""
dat = c.post("https://www.facebook.com/ajax/mercury/thread_info.php?dpr=1", headers = headers, data = data)
f=open("data" + str(0) + ".html", "w+")
f.write(dat.content)
f.close()
	
#GET INBOX STUFF
#success!
data = """&inbox[offset]=0
	&inbox[limit]=1000
	&inbox[filter]
	&client=mercury
	&__user=100008183341012&__a=1
	&__dyn=7AzkXh8OAcjxd2u6aOGeFxqewRAKGgS8zAS-C2u6oqwWhE98nwgUaqG2yaBxebkwy6UnGi7VXDG4XzErz8iGt0TyKum4UpxSLGqu58nVUkzaxbxm1iyECcBxi48hxGbwYxyq-5pZ1G6XDxx4yplzEly8myEbt5xq498lBVpEcm8ypUhKHw
	&__af=iw&__req=17&__be=-1&__pc=PHASED%3ADEFAULT&__rev=2865362
	&fb_dtsg=AQFbG2C9c977%3AAQEmJLBD7pEk&ttstamp=265817098715067579957555558658169109747666685511269107"""
dat = c.post("https://www.facebook.com/ajax/mercury/threadlist_info.php?dpr=1", headers = headers, data = data)
f=open("data" + str(1) + ".html", "w+")
f.write(dat.content)
f.close()
