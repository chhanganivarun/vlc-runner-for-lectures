#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    x=0
else:
    try:
        x=int(sys.argv[1])
    except:
        x=0
import shlex,subprocess
print(x)
fo = open('file_list','r')
a = fo.readlines()
a = [ x.strip() for x in a ]
fo.close()
a=a[x:]
b=''
for x in a:
    b+='"'+x+'" '
subprocess.call('vlc '+b,shell=True)
