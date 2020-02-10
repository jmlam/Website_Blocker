import time
from datetime import datetime as dt
import re
hosts_temp = r'hosts'
hosts_path = r'C:\Windows\System32\drivers\etc\hosts' #list of distracting site
redirect = "127.0.0.1" # redirect to different 
website_list = ['www.facebook.com', 'facebook.com', 'youtube.com', 'www.youtube.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, hour = 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, hour = 16) and dt.today().weekday() not in (5, 6):
        print('Work is equppied from M-F, 8-4')
        with open(hosts_path, 'r+') as f:
            content = f.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write(redirect + '\t'+ website + '\n')
    else:
        print('Work is not equipped')
        with open(hosts_path, 'r+') as f:
            content = f.readlines() #read contents
            f.seek(0) #put pointer at top of file
            for line in content:
                if not re.match("^127.0.0.1\s(www.)*([a-z]|[A-Z])*.com$", line):
                    f.write(line) #write contents of file without website
            f.truncate() #delete everything below
    
    time.sleep(60)