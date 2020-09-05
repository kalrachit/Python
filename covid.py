from selenium import webdriver
from selenium.webdriver.common.keys import Keys	 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, datetime
import re
import pyodbc
import socket
import requests
import gc 
import mails,os
import getpass
from selenium import webdriver
#driver = webdriver.Chrome()
requests.adapters.DEFAULT_RETRIES = 2
server	= str(socket.gethostname()+' ('+getpass.getuser()+')')
print(server)

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=;DATABASE=;UID=;PWD=')
statenodata=['CG']
#state=['WB']
state=['AP','AR','AS','BR','GA','GJ','HR','HP','JK','JH','KA','KL','MP','MH','MN','ML','MZ','NL','OR','PB','RJ','SK','TN','TR','UK','UP','WB','TN','TR','AN','CH','DH','DD','DL','LD','PY']
def joinstr(list, x):
	sum=''
	for y in range(x,len(list)):
		print(list[y])
		sum=sum+str(list[y])+' '
	return sum

def joinstr2(list, x):
	sum=''
	for y in range(0,len(list)):
		if y > x:
			continue
		print(list[y])
		sum=sum+str(list[y])+' '
	return sum

def convtolist(dtable):
	if type(dtable) == list:
		lst1 = []
		try:
			for d in dtable:
				print(d.text)
				lst1.append(format(d.text))
			if str(lst1)[1] == "\'":
				st1 = str(lst1).replace("['", "")
				st1 = str(st1).replace("']", "")
				lst2 = str(st1).split('\\n')
				lst3 = [ ' '.join(x) for x in zip(lst2[0::2], lst2[1::2]) ]
				return lst3
			elif str(lst1)[1] == '\"':
				st1 = str(lst1).replace('["', "")
				st1 = str(st1).replace('"]', "")
				lst2 = str(st1).split('\\n')
				lst3 = [ ' '.join(x) for x in zip(lst2[0::2], lst2[1::2]) ]
				return lst3
		except Exception as e:
			print('Oops! There are some error ('+str(e)+') in this process. Please retry after some time')
	else:
		print("Not a list passed")
		
		
def restartScript() :

	print('')
	try:
		driver = webdriver.Chrome(executable_path=r'C:\Chromedriver\chromedriver.exe')
		# you need chrome driver match your chrome version and provide path in the above path.
		#driver.maximize_window()
		print(state)
		for x in state:
			statename=''
			if str(x)==str('AP'): statename ='Andhra Pradesh'
			if str(x)==str('AR'): statename ='Arunachal Pradesh'
			if str(x)==str('AS'): statename ='Assam'
			if str(x)==str('BR'): statename ='Bihar'
			if str(x)==str('CG'): statename ='Chhattisgarh'
			if str(x)==str('GA'): statename ='Goa'
			if str(x)==str('GJ'): statename ='Gujarat'
			if str(x)==str('HR'): statename ='Haryana'
			if str(x)==str('HP'): statename ='Himachal Pradesh'
			if str(x)==str('JK'): statename ='Jammu and Kashmir'
			if str(x)==str('JH'): statename ='Jharkhand'
			if str(x)==str('KA'): statename ='Karnataka'
			if str(x)==str('KL'): statename ='Kerala'
			if str(x)==str('MP'): statename ='Madhya Pradesh'
			if str(x)==str('MH'): statename ='Maharashtra'
			if str(x)==str('MN'): statename ='Manipur'
			if str(x)==str('ML'): statename ='Meghalaya'
			if str(x)==str('MZ'): statename ='Mizoram'
			if str(x)==str('NL'): statename ='Nagaland'
			if str(x)==str('OR'): statename ='Orissa'
			if str(x)==str('PB'): statename ='Punjab'
			if str(x)==str('RJ'): statename ='Rajasthan'
			if str(x)==str('SK'): statename ='Sikkim'
			if str(x)==str('TN'): statename ='Tamil Nadu'
			if str(x)==str('TR'): statename ='Tripura'
			if str(x)==str('UK'): statename ='Uttarakhand'
			if str(x)==str('UP'): statename ='Uttar Pradesh'
			if str(x)==str('WB'): statename ='West Bengal'
			if str(x)==str('TN'): statename ='Tamil Nadu'
			if str(x)==str('TR'): statename ='Tripura'
			if str(x)==str('AN'): statename ='Andaman and Nicobar Islands'
			if str(x)==str('CH'): statename ='Chandigarh'
			if str(x)==str('DH'): statename ='Dadra and Nagar Haveli'
			if str(x)==str('DD'): statename ='Daman and Diu'
			if str(x)==str('DL'): statename ='Delhi'
			if str(x)==str('LD'): statename ='Lakshadweep'
			if str(x)==str('PY'): statename ='Pondicherry'
			url = "https://www.covid19india.org/state/"+str(x)
			print(url)
			
			driver.get(url)
			time.sleep(3)
			try:
				driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[2]/div[1]/div[2]/button").click()
			except:
				print('Button not available')
				time.sleep(3)
				try:
					driver.find_element_by_xpath("//*[@id='root']/div/div[3]/div[2]/div[1]/div[2]/button").click()
				except:
					print('Button not available in 2nd try')
                    #//*[@id="root"]/div/div[3]/div[2]/div[1]/div[1]/div[1]/div
                    #//*[@id="root"]/div/div[3]/div[2]/div[1]/div[1]/div[1]/div
			confirmedcase = driver.find_elements_by_xpath("//*[@id='root']/div/div[3]/div[2]/div[1]/div[1]/div[1]/div")########## path	  ##########
			if confirmedcase:
				print(confirmedcase)
				countrytable = convtolist(confirmedcase)
				time.sleep(3) 
			else:
				continue
			#Actions action = new Actions(driver);
			#confirmedcase = driver.find_elements_by_xpath("//*[@id='root']/div/div[3]/div[2]/div[1]/div[1]/div")########## path	  ##########
			cursor = conn.cursor()
			for x in countrytable:
				if '↑' in str(x):
					continue
				name=x.split(' ')
				
				if (str(name[1]).replace('-','').replace('.','').strip()).isalpha() and ((str(name[0]).replace('-','').replace('.','').strip()).isalpha() == False):
					distname=joinstr(name, 1)
					print(distname)
					sql="insert into corona_cases(country,state,district,datefor,cases,source,updatedat,updatedby)values('India','"+statename+"','"+distname.strip()+"',getdate(),'"+str(name[0]).replace(',','').strip()+"','"+str(url)+"',getdate(),'auto')"
				else:
					distname=joinstr2(name, (len(name)-2))
					print(distname)
					sql="insert into corona_cases(country,state,district,datefor,cases,source,updatedat,updatedby)values('India','"+statename+"','"+distname.replace(',','').strip()+"',getdate(),'"+str(name[(len(name)-1)]).replace(',','').strip()+"','"+str(url)+"',getdate(),'auto')"
				print(sql)
				cursor.execute(sql)
				conn.commit()
				
			
	except pyodbc.Error as ex:
		driver.close()

def main() :
	restartScript()

if __name__ == "__main__" :
	main()