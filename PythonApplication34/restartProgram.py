import psutil
import os
import time
import threading
from threading import Thread,Timer

def func1():
  judgeprocess('文件删除v1.4.exe')
  global timer
  if signal == False:
    timer = threading.Timer(30, func1)
    timer.start()
  else:
      time.sleep(5)
      func1()

def judgeprocess(processname):
    global signal 
    signal = True
    pl = psutil.pids()
    try:
        for pid in pl:
            if psutil.Process(pid).name() == processname:
                signal = False
                break
        else:
            os.system("start /B "+restart_address)
            signal = False
    except:
        pass

if __name__ == '__main__':    
    restart_address = os.path.join(os.getcwd(),'文件删除v1.4.exe')
    signal = False
    time.sleep(5)
    func1() 
