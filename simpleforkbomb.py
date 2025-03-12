import sys
import subprocess

x = 0
while True:
    x += 1
    print(f"Current X: {x}")
    try:
        subprocess.Popen([sys.executable] + sys.argv, creationflags=subprocess.CREATE_NEW_CONSOLE)
    except:
        #in case someone isnt using windows
        subprocess.Popen([sys.executable] + sys.argv)
