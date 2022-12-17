# ==============================================================
# TOOL MADE BY Thành Vinh 
# TOOL TĂNG SHARE ẢO BẰNG TOKEN
# ZALO: 0927423139
# ==============================================================
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
tim = "\033[1;38m"
# Đánh Dấu Bản Quyền
vin_tool = trang + "~" + trang + "[" + do + "+" + trang + "] " + trang + "=> "
vin = trang + "~" + trang + "[" + do + "÷" + trang + "] " + trang + "=> "
# Config
__DEV__='VINZ'
__ZALO__ = '0927423139'
__ADMIN__ = 'NgThanhVinh'
__FACEBOOK__ = 'NgThanhVinhxDeath '
__VERSION__ = 'Legend'
count = 0
dem = 0
# import lib
import requests, random
import os,sys,requests,threading
from time import sleep
from datetime import datetime
try:
	import requests,pystyle
except:
	print (luc + "Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải ")
	os.system('pip install requests && pip install bs4 && pip install pystyle')
# ==========================[ FUNCTION ]===========================================
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def banner():
    banner = f"""
      \033[1;31m
   █████████  █████                                  
 ███░░░░░███░░███                                   
░███    ░░░  ░███████    ██████   ████████   ██████ 
░░█████████  ░███░░███  ░░░░░███ ░░███░░███ ███░░███
 ░░░░░░░░███ ░███ ░███   ███████  ░███ ░░░ ░███████ 
 ███    ░███ ░███ ░███  ███░░███  ░███     ░███░░░  
░░█████████  ████ █████░░████████ █████    ░░██████ 
 ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ░░░░░      ░░░░░░  
      
                       \033[0;93m TOOL SHARE ẢO MAX SPEED                    
                                                            
\033[1;38m~ \033[1;31mTeleeee : \033[0;93m{__WEB__}
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
{vin_tool}\033[1;37mCopyright By: \033[1;34m{__ADMIN__}
{vin_tool}\033[1;35mZalo: \033[1;34m{__ZALO__}
{vin_tool}\033[1;36mFacebook: \033[1;31mFb.com/{__ZALO__}
{vin_tool}\033[0;93mTool Tăng Share Ảo Bằng Page Pro5 Version {__VERSION__}
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""
    echo(banner)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
def vin_delay(o):
    while(o>1):
        o=o-1
        print(f'{trang}[\033[1;31mN\033[1;33mĐ\033[1;36mP\033[1;35mT\033[1;34mO\033[1;32mO\033[1;35mL\033[1;37m]\033[1;37m[\033[1;36m|\033[1;37m]\033[1;37m[.....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mN\033[1;32mĐ\033[1;34mP\033[1;35mT\033[1;36mO\033[1;33mO\033[1;31mL\033[1;37m]\033[1;37m[\033[1;31m/\033[1;37m]\033[1;37m[\033[1;32m>\033[1;37m....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mN\033[1;33mĐ\033[1;36mP\033[1;35mT\033[1;34mO\033[1;32mO\033[1;35mL\033[1;37m]\033[1;37m[\033[1;32m-\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;37m...]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mN\033[1;32mĐ\033[1;34mP\033[1;35mT\033[1;36mO\033[1;33mO\033[1;31mL\033[1;37m]\033[1;37m[\033[1;33m+\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;37m..]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mN\033[1;33mĐ\033[1;36mP\033[1;35mT\033[1;34mO\033[1;32mO\033[1;35mL\033[1;37m]\033[1;37m[\033[1;34m\{trang}]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;37m.]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mN\033[1;32mĐ\033[1;34mP\033[1;35mT\033[1;36mO\033[1;33mO\033[1;31mL\033[1;37m]\033[1;37m[\033[1;35m|\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;35m>\033[1;37m]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
def runshare(x, dem, id_post):
    token = listtaikhoan[x]
    rq = random.choice([requests.get, requests.post])
    time = datetime.now().strftime("%H:%M:%S")
    runshare = rq(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={token}').json()
    if 'id' in runshare:
        print('\033[1;31m[\033[0;93m'+str(dem)+'\033[1;31m] | \033[1;36m'+str(time)+' \033[1;31m| \033[1;37m'+str(runshare['id'])+' \033[1;31m| \033[0;93mSUCCESS')
    else:
        print('\033[1;31m[\033[0;93m'+str(dem)+'\033[1;31m] | \033[1;36m'+str(time)+' \033[1;31m| ERROR ')
# =================[ Clear + Thông Số Admin ]===========================
clear()
banner()
file = input(vin_tool+luc+'Vui Lòng Nhập Tên File Chứa List Token'+trang+': '+vang)
try:
    listtaikhoan = open(file+'.txt', 'r', encoding='utf-8').read().split('\n')
except:
    quit(vin_tool+do+'File Không Tồn Tai, Nhập Mỗi Tên File Thôi Nhes Không Cần .txt Đâu')
# NHẬP THÔNG SỐ RUN TOOL
clear()
banner()
for line in listtaikhoan:
    count+=1
print(vin_tool+luc+'Tổng Số Token Có Trong File Là'+trang+': ',count)
thanh()
linkpost = input(vin_tool+luc+'Vui Lòng Nhập Link Post'+trang+': '+vang)
get_id_post = requests.post('https://id.traodoisub.com/api.php',data={"link":linkpost,}).json()
if 'success' in get_id_post:
    id_post = get_id_post["id"]
else:
    thanh()
    exit(ndp+do+'CÓ VẺ LINK POST SAI VUI LÒNG KIỂM TRA LẠI!!')
thanh()
print(vin_tool+do+'['+vang+'SUCCESS'+do+']'+trang+': '+xnhac+'UID POST CỦA BẠN LÀ'+trang+': ',id_post)
thanh()
delay = int(input(vin_tool+luc+'Vui Lòng Nhập Delay Share'+trang+': '+vang))
thanh()
while True:
    for x in range(len(listtaikhoan)):
        dem = dem+1
        threading.Thread(target=runshare,args=(x, dem, id_post, )).start()
        vin_delay(delay)
