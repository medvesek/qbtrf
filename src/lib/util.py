import sys
import os

def isRunningAsExe():
  return getattr(sys, 'frozen', False)

def getCliToExecuteCurrentProgram():
  if isRunningAsExe(): 
    return sys.executable
  else:
    interpreter = sys.executable
    script = os.path.abspath(sys.argv[0])
    return f"{interpreter} {script}"
  
def programRootDir(path):
  if isRunningAsExe(): 
    return os.path.join(os.path.dirname(sys.executable), path)
  else:
    return os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), path)