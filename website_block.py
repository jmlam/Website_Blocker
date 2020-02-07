import time
from datetime import datetime as dt
hosts_path = r'hosts' #list of distracting site
redirect = "127.0.0.1" # redirect to different 
website_list = ['www.facebook.com', 'facebook.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, hour = 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, hour = 16):
        print('Work is equppied from 8-4')
        with open(hosts_path, 'r+') as f:
            content = f.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write(redirect + '\t'+ website + '\n')
    else:
        print('Work is not equipped')
    time.sleep(300)