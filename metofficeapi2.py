import http.client
import json
import cx_Oracle
import datetime
import Downloadmetofficejson as dj
import settings
import os.path
from os import path
from settings import Settings
from datetime import datetime, timezone

utc_dt = datetime.now(timezone.utc)

rid=[]
id=[]
lat=[]
long=[]
location=[]
id,lat,long,location=dj.getvalues()


for y in range(0,len(id)):
    filepath=Settings().conf['filepath']
    filename=(str(utc_dt.year)+'-'+str(utc_dt.day)+'-'+str(location[y])) 
    filepath=filepath+filename+'.json'
    if path.exists(filepath):
        with open(filepath) as f:
          data = json.load(f)
        for x in range(0,25):
            if(utc_dt.strftime('%Y-%m-%dT%H:00Z')==data['features'][0]['properties']['timeSeries'][x]['time']):
                ans=data['features'][0]['properties']['timeSeries'][x]['screenTemperature']
                print('Location :'+ str(location[y]) +', Temp: '+str(int(ans))+'.0 C')
                try:
                    con2 = Settings().getcon()
                    cur2 = con2.cursor()
                    cur2.execute("update Metoffice_rac set temp="+str(int(ans))+", lastupdated=sysdate where id="+str(id[y])+"")
                    con2.commit()
                    cur2.close()
                except:
                    print('Exception occured While inserting data in Table')
                print('Data inserted into table')
                break
    else:
        dj.downloadfile()
        print('Downloading File')
        break