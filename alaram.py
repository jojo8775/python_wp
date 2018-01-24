import datetime
import time as Time
import os
import rf_trigger
from sys import argv
#arg1, arg2, arg3 = argv

#print("first argument : ", arg1)
print("Number of argument passed : ", len(argv))

hrs = int(argv[1])
print("hour : ", hrs)

mins = int(argv[2])
print("min : ", mins)

switchOnHeater = argv[3]

def getSecondsFromTime(t1):
    val = (t1.hour * 3600)
    val += (t1.minute * 60)
    val += t1.second
    return val

def splitTime(sec):
    list = []
    # days
    list.append(int(sec / (24 * 3600)))
    sec %= (24 * 3600)
    # hours
    list.append(int(sec / 3600))
    sec %= 3600
    # mins
    list.append(int(sec / 60))
    sec %= 60
    # seconds
    list.append(sec)
    return list

def printRemaingTime(list):
    d,h,m,s = list
    remaingTime = ""
    if(d > 0) :
        remaingTime += (str(d) + "d ")
    if(h > 0) :
        remaingTime += (str(h) + "h ")
    if(m > 0) :
        remaingTime += (str(m) + "m ")        

    remaingTime += (str(s) + "s ")
    print("Remaining time : ", remaingTime) 
    return       


currentTime = datetime.datetime.now().time()
sofar = getSecondsFromTime(currentTime)

target = (hrs * 3600 ) + (mins * 60);
if(target < sofar) :
    target += (24 * 3600) # adding another day

heaterTriggerTime = target - 3600

printRemaingTime(splitTime(target - sofar))

# debug
# print("target : ", target)
# print("sofar : ", sofar)

count = 0
while(sofar < target) :
    # debug
    # print("target : ", target)
    # print("sofar : ", sofar)

    count += 1
    if(count > 9):
        printRemaingTime(splitTime(target - sofar))
        count = 0
            
    Time.sleep(60)
    sofar += 60
    
    if(switchOnHeater == 'yes' and sofar > heaterTriggerTime) :
        rf_trigger.trigger('on')
        switchOnHeater = 'no'
    
print("Time for some music on Iheart rario!!")
os.system("mplayer -nocache -afm ffmpeg http://c1icyelb.prod.playlists.ihrhls.com/4257_icy")
    
