import time
from datetime import datetime as dt
hosts_temp = r'hosts'
hosts_path = r'C:\Windows\System32\drivers\etc\hosts' #list of distracting site
redirect = "127.0.0.1" # redirect to different 
website_list = ['www.facebook.com', 'facebook.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, hour = 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, hour = 16):
        print('Work is equppied from 8-4')
        with open(hosts_temp, 'r+') as f:
            content = f.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write(redirect + '\t'+ website + '\n')
    else:
        print('Work is not equipped')
        with open(hosts_temp, 'r+') as f:
            content = f.readlines() #read contents
            f.seek(0) #put pointer at top of file
            for line in content:
                if not any(website in line for website in website_list):#any returns True if any website is in line any line of the content
                    f.write(line) #write contents of file without website
            f.truncate() #delete everything below
    time.sleep(60)