from bs4 import BeautifulSoup
import requests
import Agent
import re
import time
import random





def post_list():
	title1= ''
	url = "https://www.fl.ru/projects/"
	shortname = 'fl.ru'
	req = requests.get(url, headers = {
	'User-Agent': Agent.user_agent()})
	soup = BeautifulSoup(req.text , 'lxml')
	lenta = soup.find('div', class_='b-page__lenta' )
	post = lenta.find('div', class_='b-post b-post_padbot_15 b-post_margbot_20 b-post_bordbot_eee b-post_relative')


#---------------------title-href---------------------
	postlink = post.find('a')	#находим тег с заголовком
	title = postlink.text	#присваиваем ему имя title
	href = postlink['href']	#ссылка
#---------------------title-href---------------------


#---------------------price---------------------
	js = []
	script = post.findAll('script')
	for tag in script:
		js.append(tag)
	pattern = re.compile("> (\d.*?)</div>")
	price = re.findall(pattern, str(js[0]).replace('&nbsp;', ''))
	price = (str(price).replace('[\'',''))
	price = price.replace('\']','')
	if price == '':
		price = 'Договорная'
#---------------------price---------------------


#---------------------text---------------------
	pattern2 = re.compile("txt \"> (.*?)</div>")
	text = re.findall(pattern2,str(js[1]))
	text = (str(text).replace('[\'',''))
	text = text.replace('\']','')
	text = text.replace('&quot','')
	text = text.replace('&nbsp','')
	text = text.replace('&#150;',':')
#---------------------text---------------------
	a=random.randint(11,21)
	
	mess = title+'\n'+'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n'+text+'\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n'+price+' • '+shortname+'\n'+'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n'+'https://fl.ru'+href
	
	return mess
	
if __name__ == '__main__':
	post_list()

		
	

