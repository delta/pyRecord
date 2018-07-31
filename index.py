import os

import commands
x = commands.getstatusoutput("xdpyinfo | grep dimensions | awk '{print $2}'")
print(x[1])
print("Hello")
os.system("ffmpeg -f x11grab -s "+x[1]+" -r 30 -i :0.0+0,0 grab.avi")
