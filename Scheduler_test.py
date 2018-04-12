from apscheduler.schedulers.blocking import BlockingScheduler
import datetime as d
import requests as r
import json as j

def collect_data_job():
    print("Executed the job at : " , d.datetime.now())
    time = d.datetime.now()
    timestring = str(time)
    timestring_store = str(time)
    timestringnospace = timestring.replace(" ", "")
    newtime = timestringnospace.replace(":","")
    timewithoutdot = newtime.replace(".","")
    newtimeonlystrings = timewithoutdot.replace("-","")
    #print(newtimeonlystrings)
    url = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=<APIKEY TO BE GIVEN"
    response = r.get(url)
    #print("response", response)
    data = response.json()
    filename = "responseData_" + newtimeonlystrings+".json"
    with open(filename,'w') as outfile:
        #outfile.write(str(data))
        j.dump(data, outfile)
        outfile.close()
    with open("timestampstore.txt", "a") as filetime:
        filetime.write(newtimeonlystrings+" : "+timestring_store + "\n")
        filetime.close()

scheduler = BlockingScheduler()
print("Executed the job at : " , d.datetime.now())
scheduler.add_job(collect_data_job,'interval',hours = 1)
#scheduler.add_job(collect_data_job,'interval',minutes = 1)
scheduler.start()
