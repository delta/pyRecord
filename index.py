import os

print("Hello")
os.system("ffmpeg -f x11grab -s 1366x768 -r 30 -i :0.0 grab.avi")
