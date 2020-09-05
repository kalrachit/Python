import http.client
import json
import cx_Oracle
import datetime
conn = http.client.HTTPSConnection("api-metoffice.apiconnect.ibmcloud.com")

today = datetime.datetime.today()

id=[]
lat=[]
long=[]
location=[]

server = '' # enter your oracle local host 
port =   # port id
SID = '' # sid
dsn_tns = cx_Oracle.makedsn(server, port, SID)

if today.hour > 14:
    headers = {
    'x-ibm-client-id': "",
    'x-ibm-client-secret': "",
    'accept': "application/json"
    }
	# this is api id and key from met office offical webite i got two for testing please make your own
else:
    headers = {
    'x-ibm-client-id': "",
    'x-ibm-client-secret': "",
    'accept': "application/json"
    }

if today.hour > 6:
    print(today.hour)
    try:
        con = cx_Oracle.connect('username', 'password', dsn_tns)
        cur = con.cursor()
        #print(1)
        cur.execute("select id,latitude,longitude,location from Metoffice_rac1")
        records = cur.fetchall()
        #print(2)
        for row in records:
            id.append(row[0])
            lat.append(row[1])
            long.append(row[2])
            location.append(row[3])
        cur.close()
    except:
        print('Exception occured 1')

    for x in range(0,len(id)):
        longitude=long[x]
        latitude=lat[x]
        #print(longitude,latitude)

        conn.request("GET", "/metoffice/production/v0/forecasts/point/hourly?excludeParameterMetadata=false&includeLocationName=true&latitude="+str(latitude)+"&longitude="+str(longitude)+"", headers=headers)

        res = conn.getresponse()
        data = res.read()
        result_dic=json.loads(data)
        ans=result_dic['features'][0]['properties']['timeSeries'][0]['screenTemperature']
        print('Location :'+ str(location[x]) +', Temp: '+str(int(ans))+'.0 C')
        try:
            con2 = cx_Oracle.connect('username', 'password', dsn_tns)
            cur2 = con2.cursor()
            cur2.execute("update Metoffice_rac set temp="+str(int(ans))+", lastupdated=sysdate where id="+str(id[x])+"")
            con2.commit()
            cur2.close()
        except:
            print('Exception occured 2')
else:
    print('It is Sleep Time')