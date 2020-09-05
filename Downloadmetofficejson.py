# Developed by Rachit Kalra
# Developed  on 03 Feb 2020
# MetOffice Verion 2.0
#

import http.client
import json
import cx_Oracle
import datetime
import settings
from settings import Settings

conn = http.client.HTTPSConnection("api-metoffice.apiconnect.ibmcloud.com")
today = datetime.datetime.today()

if today.hour > 14:
    headers=Settings().getheader()
else:
    headers=Settings().getheader2()

id=[]
lat=[]
long=[]
location=[]


def getvalues():
    try:
        con = Settings().getcon()
        cur = con.cursor()
        #print(1)
        cur.execute("select id,latitude,longitude,location from Metoffice_rac")
        records = cur.fetchall()
        #print(2)
        for row in records:
            id.append(row[0])
            lat.append(row[1])
            long.append(row[2])
            location.append(row[3])
        cur.close()
    except:
        print('Exception occured While Reading from Table')
    return (id,lat,long,location)


def downloadfile():
    id,lat,long,location=getvalues()
    try:
        for x in range(0,len(id)):
            longitude=long[x]
            latitude=lat[x]
            conn.request("GET", "/metoffice/production/v0/forecasts/point/hourly?excludeParameterMetadata=false&includeLocationName=true&latitude="+str(latitude)+"&longitude="+str(longitude)+"", headers=headers)
            res = conn.getresponse()
            data = res.read()
            result_dic=json.loads(data)
            filename=(str(today.year)+'-'+str(today.day)+'-'+str(location[x])) 
            with open((Settings().conf['filepath']+filename+'.json'), 'w') as json_file:
                        json.dump(result_dic, json_file)
    except:
        print('Exception occured While dumping Json file location :'+str(location[x]))