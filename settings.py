# Developed by Rachit Kalra
# Developed  on 03 Feb 2020
# MetOffice Verion 2.0
#

import cx_Oracle
import datetime
from collections import OrderedDict

class Settings :
    conf = {
        'connection' : {
            'server' : '',
            'port' : ,
            'SID' : '',
            'username' : '',
            'password' : '',
        },
        'filepath' : r'C:\\Python\\data\\MetOffice\\',
		#this path needs to be present
    }
    headers = {
    'x-ibm-client-id': "",
    'x-ibm-client-secret': "",
    'accept': "application/json"
    }
	# this is api id and key from met office offical webite i got two for testing please make your own
    headers2 = {
    'x-ibm-client-id': "",
    'x-ibm-client-secret': "",
    'accept': "application/json"
    }
    def getcon(self):
        dsn_tns = cx_Oracle.makedsn(self.conf['connection']['server'], self.conf['connection']['port'], self.conf['connection']['SID'])
        conn = cx_Oracle.connect(self.conf['connection']['username'], self.conf['connection']['password'], dsn_tns)
        return conn
    
    def getnum(self):
        return self.conf['num']
        
    def getheader(self):
        return self.headers
    
    def getheader2(self):
        return self.headers2