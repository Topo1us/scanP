import socket
import smtplib
import os
def openports(ip):
    for port in [21, 22, 23, 25, 43, 45, 53, 68, 80, 110, 115, 119, 123, 135, 139, 143, 161, 179, 220, 389, 443, 445,
                 993, 1723, 2049, 3306, 3389, 5060, 8080, 9091, 9090, 1164]:
        try:
            sock = socket.socket()
            sock.settimeout(0.7)
            sock.connect((ip, port))
            print('\033[32mпорт:: %s' % port, ':: открыт')
            sock.close()
        except:
            print('\033[31mпорт:: %s' % port, ':: закрыт')
    xw=input('~ ')
def openports2():
    ip=input('IP: ')
    port=int(input('PORT: '))
    for lol in[port]:
        try:
            sock = socket.socket()
            sock.settimeout(0.7)
            sock.connect((ip, lol))
            print('\033[32mпорт:: %s' % lol, ':: открыт')
            sock.close()
        except:
            print('\033[31mпорт:: %s' % lol, ':: закрыт')
    xc=input('~ ')
print('''
\033[33mВыполнено........Termux Cod
\033[36mАвторы...........\033[31m\033[3mWolFak...\033[35m\033[3mTopo1us
\033[32m\033[0mСообщество вк...https://m.vk.com/termux_cod
''')
print('''
\033[37m[1]Сканирование стандартных портов.
\033[37m[2]Сканирование определенного порта. 

''')
x=input('\033[~ ')
if x=='1':
	openports(input('IP: '))
if x=='2':
	openports2()
