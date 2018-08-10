import subprocess
import sys

print('$ ping baidu.com')
try:  
    r = subprocess.call(['ping', '-c 3', 'baidu.com'])
    print('Exit code:', r)
except OSError as e:
    print (sys.stderr, "Execution failed:", e) 
