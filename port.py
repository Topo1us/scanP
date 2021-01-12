import os
import socket
import requests
import time
from time import sleep
os.system('clear')
sleep(2)
print('\033[31mавторы\n')
a=(' T', ' To', ' Top', ' Topo', ' Topo1', ' Topo1u', ' Topo1us', ' Topo1us-', ' Topo1us- -',' Topo1us- - P',' Topo1us- - P1',' Topo1us- - P1a',' Topo1us- - P1at',' Topo1us- - P1ato','  Topo1us- - P1aton')
b=0
while True:
    print(a[b % len(a)], sep='', end='\r')
    sleep(0.1)
    b+=1
    if b>15:
        print('')
        break
print('{версия 12.01.21}')
color_red='\033[31m'
color_green='\033[32m'
po='порт '
cl=color_red+' закрыт'
b=0
nm=0
try:
    requests.get("https://google.com", timeout=4)
    print('интернет подключен')
except:
    print('интернет отсутствует')
fg=[21, 22, 23, 25,31,41, 43, 45, 53,59, 68, 79, 80, 99, 110, 113, 115, 119, 121, 123, 135, 139, 143, 161, 179, 220, 389, 421, 443, 445, 456, 531, 555, 666, 911,
                         993, 999, 1001, 1010, 1011,1012,1015,1024,1024,1042,1045,1090,1170,1243,1245,1269,1492,1509,1600, 1723,1807,1981,1999,2023,2115, 2140, 2155, 2283, 2600, 2801, 3024,
                         2049, 3128, 3129, 3150, 3459, 3700, 3791, 4092, 3459, 3700, 3791,3306, 3389, 4321, 4567, 4590, 5000, 5001, 5011, 5031, 5321, 5400, 5401, 5550, 5555, 5556, 5060, 8080,
                         5569, 5631, 5742, 6400, 6669, 5631, 5742, 6400, 6669, 6670, 6771, 6776, 6912, 6939, 6970, 7000, 7300, 7301, 7306, 7307, 7308, 7789, 9091, 9400, 9090, 9872, 9873, 9874,
                         9875, 9876, 9878, 9989, 10101, 10520, 10607, 11000, 11225, 12076, 12223, 12345, 12346, 12361, 12362, 12631, 13000, 16969, 17300, 20000, 20001, 20203, 21544, 22222, 23456,
                         23476, 23477, 27374, 30029, 30100, 30101, 30102, 30103, 30999, 31336, 31337, 31339, 31666, 31785, 31787, 31789, 31791, 33333, 33911, 34324, 33911, 40412, 40421, 40422, 40423,
                         40426, 50505, 50766, 53001, 54320, 54321, 60000, 61466, 65000, 1349, 2989, 3801, 10067, 10167, 26274, 29891, 31337, 31338, 31789, 31791, 47262,54321]
def openports(ip):
    x=1
    port_open=0
    port_close=0
    op=[]
    ops=[]
    for port in fg:
        try:
            sock = socket.socket()
            sock.settimeout(0.3)
            sock.connect((ip, port))
            print('\033[32mport:: %s' % port, ':: открыт')
            port_open+=1
            op.append(port)
            sock.close()
        except:
            port_close+=1
            ops.append(port)
    print(color_red+'close ports '+str(port_close))
    print(color_green+'open ports ',op)
    if 80 not in op:
        print('\033[33mдля IP::',ip,'не открыт порт 80.\nсоветую перепроверить')
def openports2():
    ip=input('IP: ')
    port=int(input('PORT: '))
    for lol in[port]:
        try:
            sock = socket.socket()
            sock.settimeout(0.2)
            sock.connect((ip, lol))
            print('\033[32mпорт:: %s' % lol, ':: открыт')
            sock.close()
        except:
            print('\033[31mпортt:: %s' % lol, ':: закрыт')
            print('\033[32mготово')
print('''
[1] сканирование стандартных портов
[2] сканирование определенного порта 

''')
while True:
    x=input('~ ')
    if x=='1':
        openports(input('IP: '))
        break
    elif x=='2':
        openports2()
        break
    else:
        print('error 404.')
