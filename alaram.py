import datetime
import time as Time
import os
from sys import argv
#arg1, arg2, arg3 = argv

#print("first argument : ", arg1)
print("Number of argument passed : ", len(argv))

hrs = int(argv[1])
print("hour : ", hrs)

mins = int(argv[2])
print("min : ", mins)

print("Alarm set at ", hrs, " : ", mins)

def getSecondsFromTime(t1):
    val = (t1.hour * 3600)
    val += (t1.minute * 60)
    val += t1.second
    return val

currentTime = datetime.datetime.now().time()
hourAdjustment = 24 - currentTime.hour if hrs < currentTime.hour else 0
sec1 = getSecondsFromTime(currentTime)

targetTime = datetime.time(hour = (hrs + hourAdjustment), minute = mins)
sec2 = getSecondsFromTime(targetTime)

count = 0
while(sec1 < sec2) :
    count += 1
    if(count > 2):
        remainingSecs = (sec2 - sec1)
        remainingHrs = int(remainingSecs / 3600)
        remainingSecs %= 3600
        remainingMins = int(remainingSecs / 60)
        remainingSecs %= 60
        remaingTime = datetime.time(hour = remainingHrs, minute = remainingMins, second = remainingSecs)
        
        print("time left for alarm : ", str(remaingTime))
        count = 0
            
    Time.sleep(60)
    sec1 = getSecondsFromTime(datetime.datetime.now().time())
    
print("Time for some music on Iheart rario!!")
os.system("mplayer -nocache -afm ffmpeg http://c1icyelb.prod.playlists.ihrhls.com/4257_icy")
    
