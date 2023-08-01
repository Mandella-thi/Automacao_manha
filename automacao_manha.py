import subprocess
import os
DETACHED_PROCESS= 0x00000008


programa1= subprocess.Popen([""],creationflags=DETACHED_PROCESS)

programa2= subprocess.Popen([""], creationflags= DETACHED_PROCESS)
programa3= subprocess.Popen([""], creationflags= DETACHED_PROCESS)

#programa1.wait()
#programa2.wait()
#programa3.wait()

os._exit(0)