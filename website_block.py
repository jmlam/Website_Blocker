import time
from datetime import datetime as dt
hosts_path = r'hosts' #list of distracting site
redirect = "127.0.0.1" # redirect to different 
website_list = ['www.facebook.com', 'facebook.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, hour = 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, hour = 16):
        print('working hours are 8-4')
        with open(hosts_path, 'w') as f:
            for website in website_list:
                f.write(website + '\n')
    time.sleep(300)