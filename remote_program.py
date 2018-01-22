from pexpect import pxssh
from sys import argv

toggle = argv[1]

s = pxssh.pxssh()

if not s.login('192.168.0.15','pi','jojo') :
	print("SSH faield")
	print(str(s))
else :
	print("SSH succeed")
	if (toggle == 'on') :
		s.sendline('/var/www/html/rfoutlet/codesend  5526613 -p  0 -l 193')
	else :
		s.sendline('/var/www/html/rfoutlet/codesend  5526612 -p  0 -l 193')
	s.prompt()
	print(s.before)
	s.logout()
