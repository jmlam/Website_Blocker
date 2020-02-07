import time
hosts_path = r'C:\Users\jiami\Desktop\Projects\Website_Blocker' #list of distracting site
redirect = "127.0.0.1" # redirect to different 
website_list = ['www.facebook.com', 'facebook.com']

while True:
    now = time.strftime("%a, %d %b %Y %H:%M:%S +0000")
    print(now)#checktime
    time.sleep(300)