# -*- coding: utf-8 -*-
from pexpect import pxssh

def trigger(mode) :
    s = pxssh.pxssh()
    if not s.login('192.168.0.15','pi','jojo') :
        print("SSH Failed may be host is down or have changed")
        print(str(s))
    else :
        print("SSH Succeed")
        if(mode == 'on') :
            s.sendline('/var/www/html/rfoutlet/codesend  5526613 -p  0 -l 193')
        else :
            s.sendline('/var/www/html/rfoutlet/codesend  5526612 -p  0 -l 193')
            s.prompt()
            print(s.before)
            s.logout()
    return
